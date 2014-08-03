#!/usr/bin/env python
from selenium import webdriver
from itertools import izip
from PIL import Image
from PIL import ImageChops
import time
import math
import os
import uuid
import subprocess
import threading

import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average


SCREENSHOT_DIRECTORY = "screenshots"
URL_TO_TEST = 'http://jsfiddle.net/EtW7d/show/'
URL_TO_TEST = "http://en.wikipedia.org/wiki/Y_Combinator_(company)"
SELECTOR_TO_TEST = "firstHeading"
CONTENT_TEST = ['hello', 'something', 'else', 'goes', 'here', 'A very long string that is likely to mess everything up so this will just go here and see what happens to the entire webpage']

class UITest:
  
  def __init__(self):
    self.start_server()
    self.screenshots = []
    self.nearest_k = []
    self.diffs = []
    print 'x'
  
  def start_server(self):
    self.server_process = subprocess.Popen(["Python", "-m", "SimpleHTTPServer"]);    

  def stop_server(self):
    os.killpg(self.server_process)

  def run_ui_test(self):
    selectors = ['#name', '#title']
    self.folder_uuid= str(uuid.uuid4())

    if not os.path.exists(SCREENSHOT_DIRECTORY):
      os.makedirs(SCREENSHOT_DIRECTORY)
    
    os.makedirs(os.path.join(SCREENSHOT_DIRECTORY, self.folder_uuid));
    
    browser = webdriver.Chrome()
    #take a base screenshot first
    browser.get(URL_TO_TEST)
    browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/base.png')

    script_inc = '(function() { var js = document.createElement("script"); js.type = "text/javascript"; js.src= "http://localhost:8000/monkey_test.js"; document.body.appendChild(js); })()'
    browser.execute_script(script_inc)
    time.sleep(1)
    counter = 0
    #start making modificatons
    for content in CONTENT_TEST:
      counter += 1
      file_name = str(counter)
      self.screenshots.append(file_name)
      browser.execute_script('monkeyTest.performTestWithSelector("'+SELECTOR_TO_TEST+'", "'+content+'")');
      time.sleep(1)
      browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/'+file_name+'.png')
    #browser.quit()
    #self.stop_server();

  def find_outlier(self):
    print 'find outlier'
    file_loc = SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/'
    i1 = Image.open(file_loc+'base.png')
    for screenshot in self.screenshots:
      i2 = Image.open(file_loc+screenshot+'.png')
      self.diffs.append(self.compare_images(i1, i2))
    print self.diffs

    '''
    base_img = Image.open(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/base.png')
    for f in os.listdir(os.path.join(SCREENSHOT_DIRECTORY, self.folder_uuid)):
      if f.endswith(".png") and f != 'base.png':
        #commence nearest k or some sort of algo
        
        print f
    '''

  def generate_web_report():
    img_divs = ''
    for screenshot in self.screenshots:
      img_divs = '<img src="http://localhost:8000/'+SCREENSHOT_DIRECTORY+'/'+self.folderuuid+'/'+content+'.png'
      print img_divs
    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type">
    <title>Hello</title>
    </head>
    <body>
      Hello, World!
    </body>
    </html>
    '''
    print 'generate a web report'


  def compare_images(self, i1, i2):
    #i1 = Image.open(file1)
    #i2 = Image.open(file2)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = izip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
      # for gray-scale jpegs
      dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
      dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    return  (dif / 255.0 * 100) / ncomponents

      
def main():
  my_test = UITest()
  my_test.run_ui_test()
  my_test.find_outlier()
  

if __name__ == '__main__':
  main()
