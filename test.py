#!/usr/bin/env python
from selenium import webdriver
import time
import math
import os
import uuid
from PIL import Image
from PIL import ImageChops

SCREENSHOT_DIRECTORY = "screenshots"

class UITest:

  def run_ui_test(self):
    selectors = ['#name', '#title']
    self.folder_uuid= str(uuid.uuid4())


    if not os.path.exists(SCREENSHOT_DIRECTORY):
      os.makedirs(SCREENSHOT_DIRECTORY)
    
    os.makedirs(os.path.join(SCREENSHOT_DIRECTORY, self.folder_uuid));
    
    browser = webdriver.Chrome()
    #take a base screenshot first
    browser.get('http://www.google.com/')
    browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/base.png')

    #start making modificatons
    #browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/'+str(int(time.time()))+'.png')
    browser.quit()

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
