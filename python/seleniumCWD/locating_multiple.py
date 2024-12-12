import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from zmq import OUT_BATCH_SIZE

driver = webdriver.Chrome()
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k=laptop&page={i}&crid=1ERF41KBXZZUQ&sprefix=laptop%2Caps%2C273&ref=nb_sb_noss_1")

    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")

    # print(elems)

    print(f"{len(elems)} items found ")
    for elem in elems:
        print(elem.text)

    # print(elem.get_attribute("outerHTML"))
    # print(elem.get_attribute("text")) #   method 1

    # print(elem.text)                  #   method 2
    time.sleep(1)
    driver.close()
    