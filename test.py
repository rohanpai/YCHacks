#!/usr/bin/env python
from selenium import webdriver

selectors = ['#name', '#title']

browser = webdriver.Chrome()
browser.get('http://www.google.com/')
browser.save_screenshot('screenie.png')
browser.quit()


