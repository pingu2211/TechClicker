from selenium import webdriver
import time
import random
from datetime import datetime

while datetime.now().month == 12:
    if datetime.now().hour in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        time.sleep(random.randint(1, 15))
        driver.get("https://www.greater.com.au/greaternewengland#section-3")
        time.sleep(random.randint(1, 15))
        iframe = driver.find_element_by_id("stack-widget-embed-64356")
        time.sleep(random.randint(1, 15))
        driver.switch_to.frame(iframe)
        time.sleep(random.randint(1, 15))
        vote = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[4]/span[1]/a')
        time.sleep(random.randint(1, 15))
        vote.click()
        driver.close()
    time.sleep(60*(60+random.randint(1, 15)))

