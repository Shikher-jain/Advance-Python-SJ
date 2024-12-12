import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from zmq import OUT_BATCH_SIZE

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/s?k=laptop&crid=1ERF41KBXZZUQ&sprefix=laptop%2Caps%2C273&ref=nb_sb_noss_1")
elem = driver.find_element(By.CLASS_NAME, "puisg-row")
print(elem.get_attribute("outerHTML"))
print(elem.text)
time.sleep(1)
driver.close()