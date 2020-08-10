from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Mahnoor Ismail")
driver.find_element_by_css_selector("input[name='name']").send_keys("mahi")
driver.find_element_by_id("exampleCheck1").click()
# select class provide the option to handle the drop-down items
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_name("email").send_keys("mhnr@gmail.com")
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message

# regular expression //*[contains(@class,'alert-success')] xpath
# regular expression [class*='alert-success']
#//*[@id="experience-children"]/li/table/tr[4]/td[2]/value-addition/div/span/input[1]