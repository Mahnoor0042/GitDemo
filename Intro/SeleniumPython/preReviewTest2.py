import itertools
import os
import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://v1.test.digitalrisk.proofpoint.com/prereview/")
driver.implicitly_wait(15)
driver.find_element_by_xpath("//a[text()='Sign in to Linkedin']").click()
driver.find_element_by_css_selector("#username").send_keys("report.161@outlook.com")
driver.find_element_by_css_selector("#password").send_keys("Austin_09")
driver.find_element_by_css_selector("button[type='submit']").click()
driver.find_element_by_css_selector("a[href='update_v2']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div#basic-container")))
driver.find_element_by_css_selector("div#basic-container").click()
driver.find_element_by_xpath("//ul[@id='basic-children']/li[6]/table/tr/td[2]/value-edition/div[2]/i[@title='Edit Field']").click()
image_path = os.path.abspath('C:\\Users\\Dell\\Pictures\\Saved Pictures\ike.jpg')

driver.find_element_by_css_selector("input#tw_banner_picture_upload").clear()
driver.find_element_by_css_selector("input#tw_banner_picture_upload").send_keys(image_path)
driver.find_element_by_xpath("//span[text()='Upload']").click()
time.sleep(7)
driver.find_element_by_css_selector("span[can-click='submit_review']").click()
driver.find_element_by_xpath("//span[text()='Continue']").click()

#***********************************************************************************************************
#assert len(associations)==len(nameInputs)
# driver.implicitly_wait(15)
#driver.execute_script("window.open('https://v1.test.digitalrisk.proofpoint.com/users/sign_in')")
driver.get("https://v1.test.digitalrisk.proofpoint.com/users/sign_in")
driver.find_element_by_css_selector("input#user_email").send_keys("mahnoorismail8@gmail.com")
driver.find_element_by_css_selector("input#user_password").send_keys("Austin_14")
driver.find_element_by_xpath("//span[text()='Sign In']").click()
driver.get("https://v1.test.digitalrisk.proofpoint.com/patrol/profile_reviews")
driver.find_element_by_xpath("//td[text()='Hansell Gretal']").click()
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[can-click='approve_items']")))
driver.find_element_by_css_selector("span[can-click='approve_items']").click()
driver.find_element_by_xpath("//span[text()='Approve']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Finalize']")))
driver.find_element_by_xpath("//span[text()='Finalize']").click()
time.sleep(7)
print(driver.find_element_by_xpath("//div[@class='dialog_wrapper ui-dialog-content ui-widget-content']/p").text)
driver.find_element_by_xpath("//span[text()='Close']").click()
#//ul[@id='basic-children']/li[6]/table/tr/td[2]/value-edition/div[2]/i[@title='Edit Field']