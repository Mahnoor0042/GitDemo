from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
#radiobuttons = driver.find_elements_by_xpath("//input[@type='radio']")
radiobuttons = driver.find_elements_by_name("radioButton")

radiobuttons[2].click()
assert radiobuttons[2].is_selected()
#for radiobutton in radiobuttons:
#    if radiobutton.get_attribute("value") == "radio3":
#       radiobutton.click()
#       assert radiobutton.is_selected()
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()
driver.find_element_by_css_selector("#hide-textbox").click()
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()