from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def login(driver):
    action = ActionChains(driver)
    action.send_keys('[BAEKJOON_ID]').perform()
    time.sleep(1)
    driver.find_elements_by_css_selector('.form-control')[1].send_keys('[BAEKJOON_PASSWD]')
    driver.find_element_by_css_selector('.btn-u.pull-right').click()