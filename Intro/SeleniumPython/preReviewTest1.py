import itertools
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
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='accomplishment-container']/div/h4")))
driver.find_element_by_xpath("//div[@id='accomplishment-container']/div/h4").click()
driver.find_element_by_xpath("//div[@id='accomplishment-content']/ul/li[2]").click()
nameInputs = driver.find_elements_by_css_selector("input.course-name-field")
numbers = driver.find_elements_by_css_selector("input.number-field")
associations = (driver.find_elements_by_css_selector("select[can-value='ui_new_value.occupation']"))
savebuttons = driver.find_elements_by_xpath("//*[@id='accomplishment-children']/li[2]/table/tr/td[2]/value-addition/div/span/span[1]")
for (coursename, number) in zip(nameInputs, numbers):
    if (coursename.is_displayed() and number.is_displayed()):
        coursename.send_keys("PythonSelenium")
        number.send_keys("PY-99897")
        break
for ass in associations:
    if (ass.is_displayed()):
        Select(ass).select_by_index(1)
        break

for save in savebuttons:
    if (save.is_displayed()):
        save.click()
        break
time.sleep(5)
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
driver.find_element_by_xpath("//span[text()='Finalize']").click()
time.sleep(5)
print(driver.find_element_by_xpath("//div[@class='dialog_wrapper ui-dialog-content ui-widget-content']/p").text)
driver.find_element_by_xpath("//span[text()='Close']").click()



#add postion icon: //div[@id='experience-content']/ul/li[@id='2021']
# //*[@id="accomplishment-children"]/li[2]/table/tr[2]/td[2]/value-edition/div[2]/i[1]
# //*[@id="accomplishment-children"]/li[2]/table/tr[4]/td[2]/value-addition/div/span/span[1]