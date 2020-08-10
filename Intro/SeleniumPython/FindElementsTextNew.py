from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
#driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

cities = driver.find_elements_by_css_selector("p[class*='blackText']")

for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break
    #print(city.text)


