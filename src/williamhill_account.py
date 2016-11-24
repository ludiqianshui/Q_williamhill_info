
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class williamhill_account(object):

    def __init__(self):
        return
    
    def  __del__(self):
        return
    
    def get_williamhill_balance(self, user_name, user_password):
        driver = webdriver.Firefox()

        driver.get("http://sports.williamhill.com/bet/en-gb")
        sleep(2)
        elem=driver.find_element_by_id("yesBtn")
        elem.click()
        sleep(5)
        elem = driver.find_element_by_xpath('//*[@id="tmp_username_div"]/input')  # username element
        elem.send_keys(user_name)
        sleep(5)
        elem = driver.find_element_by_xpath('//*[@id="tmp_pwd_div"]/input') # password element
        elem.send_keys(user_password)
        sleep(5)
        elem=driver.find_element_by_id("signInBtn")  # login
        elem.click()
        sleep(5)
        elem=driver.find_element_by_id("userBalance")  # get balance
        willamhill_balance = elem.text
        willamhill_balance = willamhill_balance[1:]
        print (willamhill_balance)
        driver.close()
        return  willamhill_balance
    
    
class Test(unittest.TestCase):

    def test_username(self):
        QSONG_williamhill = williamhill_account()
        balance  = QSONG_williamhill.get_williamhill_balance("qidizhihuizh", "Songqg1981")
        print( balance)

        return
        