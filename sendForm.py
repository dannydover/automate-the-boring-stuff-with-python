#! /usr/bin/env python3
# sendForm.py - selenium template for sending forms
# https://automatetheboringstuff.com/chapter11/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
browser.get('https://mail.yahoo.com')

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')

nextButton = browser.find_element_by_id('login-signin')
nextButton.click()


#try:
#    elem = browser.find_element_by_class_name('cover-thumb')
#    print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('Was not able to find an element with that name.')
