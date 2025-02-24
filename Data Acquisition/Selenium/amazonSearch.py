from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = "https://www.amazon.com/s?k=phone&crid=3230YKE7MMYT9&sprefix=phone%2Caps%2C995&ref=nb_sb_noss_1"
driver.get(url)
elements = driver.find_elements(By.CLASS_NAME, "a-size-medium")
print(len(elements))
for ele in elements:
    print(ele.text)

