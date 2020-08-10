from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Mahnoor Ismail")
driver.find_element_by_css_selector("input[name='name']").send_keys("mahi")
driver.find_element_by_name("email").send_keys("mahi")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_css_selector("div[class*='alert-success']").text)
#//*[contains(@class, 'alert-success')] -Xpath REGUlar
print(driver.find_element_by_class_name("alert-success"))
# Seolect class provides the method to handle the options in the static dropdown

