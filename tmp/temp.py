from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("http://sports.williamhill.com/bet/en-gb")

sleep(2)
elem=driver.find_element_by_id("yesBtn")
elem.click()
sleep(5)
elem = driver.find_element_by_xpath('//*[@id="tmp_username_div"]/input')  # username element
elem.send_keys("qidizhihuizh")
sleep(5)
elem = driver.find_element_by_xpath('//*[@id="tmp_pwd_div"]/input') # password element
elem.send_keys("Songqg1981")
sleep(5)
elem=driver.find_element_by_id("signInBtn")  # login
elem.click()
sleep(5)
elem=driver.find_element_by_id("userBalance")  # get balance
willamhill_balance = elem.text
willamhill_balance = willamhill_balance[1:]
print (willamhill_balance)
sleep(5)
driver.close()

