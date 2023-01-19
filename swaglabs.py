import logging
import os
import string
import time
from datetime import date, datetime
from selenium.webdriver.support.ui import Select
from xmlrpc.client import boolean
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException,NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import re
from builtins import str
import glob
import csv
from pathlib import Path
directory_name = os.getcwd()
folder_path = directory_name +"\\data"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('disable-notifications')
chrome_options.set_capability('unhandledPromptBehavior', 'accept')
driver = webdriver.Chrome(options=chrome_options, executable_path=directory_name +'\\chromedriver.exe')
driver.implicitly_wait(10)
web = "https://www.saucedemo.com/"
driver.get(web)
driver.maximize_window()

#find elements
User_name = driver.find_element("xpath","//*[@id='user-name']")
Password = driver.find_element("xpath","//*[@id='password']")
Submit = driver.find_element("xpath","//*[@id='login-button']")

#click user name and send user name
User_name.click()
User_name.send_keys("standard_user")

#click password and send password
Password.click()
Password.send_keys("secret_sauce")
driver.get_screenshot_as_file("loginpage.png")
Submit.click()


if(driver.find_element("xpath","//*[@id='header_container']/div[2]/span")):
    driver.get_screenshot_as_file("loggedin.png")
    print("Log in successful!")

    

Filter = driver.find_element("xpath","//*[@id='header_container']/div[2]/div[2]/span/select")
Filter.click()

Element_1=driver.find_element("xpath","//*[@id='header_container']/div[2]/div[2]/span/select/option[2]")
Element_1.click()

driver.get_screenshot_as_file("sorted.png")


time.sleep(5)
time.sleep(3)
driver.close()