from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
#iframe, frameset, frames
driver.get("https://the-internet.herokuapp.com/iframe")
# this method accpets either frame id, frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Test Automation")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)