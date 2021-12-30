import time
def Check(driver):
    flag = 1
    while flag:
        time.sleep(1)
        if driver.current_url == 'https://www.acmicpc.net/status?group_id=13131':
            flag = 0
        else:
            print('Getchar 푸는중...')