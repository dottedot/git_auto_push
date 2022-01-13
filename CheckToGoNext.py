#-*- coding: utf-8 -*-

import time, priv_user

def check(driver):
    flag = 1

    while flag:
        time.sleep(1)

        if driver.current_url == priv_user.BOJ_CAPTCHA:
            flag = 0
        else:
            print('CAPTCHA 푸는중...')
    
    print('\n######### START #########\n')