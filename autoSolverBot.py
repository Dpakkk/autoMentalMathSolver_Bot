#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:33:25 2023

@author: bikashpokharel
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import re

# browser code
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://arithmetic.zetamac.com/game?key=a7220a92')
question_element = browser.find_element(By.CLASS_NAME,"problem")

# before regex
#String question = wd.findElement(By.cssSelector("div[id^='customSelect'] span.problem")).getText();


while True:
    # regular expressin to generalize the mathematical expression
    # can change the expression according to usecase
    question = re.sub(r'[÷×+\-\u2013]', lambda m: {'÷': '/', '×': '*', '+': '+', '\u2013': '-', '-': '-'}[m.group(0)], question_element.text)
    answer = str(int(eval(question)))
    pyautogui.write(answer)