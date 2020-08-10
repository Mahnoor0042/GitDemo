from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
textname = "option3"
driver.find_element_by_css_selector("#name").send_keys(textname)
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
assert textname in alert.text
print(alert.text)
alert.accept()
#alert.dismiss()
