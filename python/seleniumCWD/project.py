import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from zmq import OUT_BATCH_SIZE
driver = webdriver.Chrome()

file=1
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k=laptop&page={i}&crid=1ERF41KBXZZUQ&sprefix=laptop%2Caps%2C273&ref=nb_sb_noss_1")
    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f"{len(elems)} items found ")
    for elem in elems:
        d=(elem.get_attribute("outerHTML"))
        with open(f"Shikher-jain/python/seleniumCWD/data/laptop_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1
time.sleep(1)
driver.close()