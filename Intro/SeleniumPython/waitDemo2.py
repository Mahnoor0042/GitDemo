from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
#driver.implicitly_wait(5)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
#driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
image = driver.find_element_by_css_selector("img[alt='Cart']")
image.click()
#cart = driver.find_element_by_xpath("//div[@class='action-block']/button")
#cart.click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

#driver.find_element_by_css_selector(".promoBtn").click()
