#!/usr/bin/python3

from selenium import webdriver

#browser = webdriver.Chromium()
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
