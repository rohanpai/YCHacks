#!/usr/bin/env python
from selenium import webdriver
import time
import math
import os
import uuid

SCREENSHOT_DIRECTORY = "screenshots"

def run_ui_test():
  selectors = ['#name', '#title']
  folder_uuid= str(uuid.uuid4())


  if not os.path.exists(SCREENSHOT_DIRECTORY):
    os.makedirs(SCREENSHOT_DIRECTORY)
  
  os.makedirs(os.path.join(SCREENSHOT_DIRECTORY, folder_uuid));

  browser = webdriver.Chrome()
  browser.get('http://www.google.com/')
  browser.save_screenshot(SCREENSHOT_DIRECTORY+'/'+folder_uuid+'/'+str(int(time.time()))+'.png')
  browser.quit()


def main():
  run_ui_test()


if __name__ == '__main__':
  main()
