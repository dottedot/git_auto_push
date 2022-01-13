#-*- coding: utf-8 -*-

from selenium import webdriver
import priv_user

# chromeoption.add_argument('--headless')
# chromeoption.add_argument('--no-sandbox')
# chromeoption.add_argument('--disable-dev-shm-usage')

def driver():
    chromeoption = webdriver.ChromeOptions()
    driver = webdriver.Chrome('chromedriver', options = chromeoption)
    driver.get(priv_user.BOJ_URL)

    return driver
