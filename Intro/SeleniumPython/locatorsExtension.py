from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
# driver.find_element_by_css_selector("#user_email").send_keys("misbahshahwar44@gmail.com")
# driver.find_element_by_css_selector("#user_password").send_keys("Austin_060")
# driver.find_element_by_css_selector("span#signin").click()
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")
driver.find_element_by_css_selector("div[id='usernamegroup'] label")
driver.find_element_by_xpath("//form[@name='login']/div[1]/label")
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
