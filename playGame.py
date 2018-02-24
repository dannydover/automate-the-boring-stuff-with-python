#! /usr/bin/env python3
# playGame.py - Script to play 2048 online automatically
# https://automatetheboringstuff.com/chapter11/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')
comicCount = 0

while comicCount < 10:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

    comicCount = comicCount + 1


#try:
#    elem = browser.find_element_by_class_name('cover-thumb')
#    print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('Was not able to find an element with that name.')
