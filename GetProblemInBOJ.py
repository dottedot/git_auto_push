#-*- coding: utf-8 -*-

# TODO : if i solve by python -> save python
#        if i solve by cpp -> save cpp
#        select the language that i solve

# ['제출 번호','아이디','문제','결과','메모리','시간','언어','코드 길이','제출한 시간']

def problem(driver):
    tr_lst = []

    for tr in driver.find_elements_by_css_selector('#status-table > tbody'):
        lst = list(tr.text.split('\n'))     
        for i in lst:
            txt = i.split()

            if txt[3] == '맞았습니다!!' or txt[3] == '100점':
                tr_lst.append(txt[2])

    return tr_lst