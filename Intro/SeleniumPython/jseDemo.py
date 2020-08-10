#JS Dome can access any element on web page like how selenium does
# Selenium has a method to run JS code in it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("It's Mahi")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
shopButton=driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script('arguments[0].click();',shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
