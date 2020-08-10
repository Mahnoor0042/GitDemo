from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
# driver.get("https://www.familysearch.org/en/")
#
# action = ActionChains(driver)
# # for multiple chains of actions put .build() before .perform()
# action.move_to_element(driver.find_element_by_css_selector("button[aria-controls='search']")).perform()
# driver.find_element_by_css_selector("button[aria-controls='search']").click()
# action.move_to_element(driver.find_element_by_xpath("//ul[@id='search']/li[4]")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)

action.context_click(driver.find_element_by_css_selector("#double-click")).perform()
action.double_click(driver.find_element_by_css_selector("#double-click")).perform()
alert = driver.switch_to.alert
alert.accept()