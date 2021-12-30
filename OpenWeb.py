from selenium import webdriver

def driver():
    chromeoption = webdriver.ChromeOptions()
# chromeoption.add_argument('--headless')
# chromeoption.add_argument('--no-sandbox')
# chromeoption.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('chromedriver', options = chromeoption)
    url = 'https://www.acmicpc.net/login?next=%2Fstatus%3Fgroup_id%3D13131'
    driver.get(url)
    return driver
