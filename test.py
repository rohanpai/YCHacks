#!/usr/bin/env python
from selenium import webdriver
from PIL import Image
from PIL import ImageChops
import time
import math
import os
import uuid
import subprocess
import threading

SCREENSHOT_DIRECTORY = "screenshots"
URL_TO_TEST = 'http://jsfiddle.net/EtW7d/show/'
URL_TO_TEST = "http://en.wikipedia.org/wiki/Y_Combinator_(company)"
SELECTOR_TO_TEST = "firstHeading"
CONTENT_TEST = ['hello', 'something', 'else', 'goes', 'here']

class UITest:
  
  def __init__(self):
    self.start_server();
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
    
    #start making modificatons
    print CONTENT_TEST 
    for content in CONTENT_TEST:
      browser.execute_script('monkeyTest.performTestWithSelector("'+SELECTOR_TO_TEST+'", "'+content+'")');
      time.sleep(1)
      browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/'+str(int(time.time()))+'.png')
    
    #browser.quit()
    self.stop_server();

  def find_outlier(self):
    print 'find outlier'
    self.nearest_k = []
    base_img = Image.open(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/base.png')
    for f in os.listdir(os.path.join(SCREENSHOT_DIRECTORY, self.folder_uuid)):
      if f.endswith(".png") and f != 'base.png':
        print f
      
def main():
  my_test = UITest()
  my_test.run_ui_test()
  my_test.find_outlier()

if __name__ == '__main__':
  main()
