#!/usr/bin/env python
from selenium import webdriver
import time
import math
import os
import uuid

SCREENSHOT_DIRECTORY = "screenshots"

class UITest:

  def run_ui_test(self):
    selectors = ['#name', '#title']
    self.folder_uuid= str(uuid.uuid4())


    if not os.path.exists(SCREENSHOT_DIRECTORY):
      os.makedirs(SCREENSHOT_DIRECTORY)
    
    os.makedirs(os.path.join(SCREENSHOT_DIRECTORY, self.folder_uuid));
    
    browser = webdriver.Chrome()
    browser.get('http://www.google.com/')
    browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+self.folder_uuid+'/'+str(int(time.time()))+'.png')
    browser.quit()


def main():
  my_test = UITest()
  my_test.run_ui_test()


if __name__ == '__main__':
  main()
