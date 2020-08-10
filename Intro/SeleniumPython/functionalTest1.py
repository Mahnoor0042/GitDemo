from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
list = []
driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
#driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list)
#driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
# selected_items = driver.find_elements_by_css_selector("h4.product-name")
image = driver.find_element_by_css_selector("img[alt='Cart']")
image.click()
cart = driver.find_element_by_xpath("//div[@class='action-block']/button")
cart.click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
list2 = []
items_in_cart = len(driver.find_elements_by_css_selector("p.product-name"))
print(items_in_cart)
#amounts = driver.find_elements_by_xpath("//div[@class='products']/table/tr/td[5]/p")
amounts = driver.find_elements_by_xpath("//div[@class='products']/table/tr/td[5]/p")
sum = 0
for amount in amounts:
    print(amount.text)
    sum = sum + int(amount.text)

print(sum)

# for item in items_in_cart:
#     print (item.text)
#print(list2)
#assert list == list2

#assert list == items_in_cart
 #for (sitem,citem) in zip(selected_items,items_in_cart):
#     if(sitem.text == citem.text):
#         print(sitem.text)




