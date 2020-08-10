import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
time.sleep(10)
driver.find_element_by_id("fromCity").click()

driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(10)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()
#print(city.text)