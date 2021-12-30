def problem(driver):
    tr_lst = []
    for tr in driver.find_elements_by_css_selector('#status-table > tbody'):
    # print(tr.text)
        lst = list(tr.text.split('\n'))
    # print(len(lst), lst)
        for i in lst:
            txt = i.split()

            if txt[3] == '맞았습니다!!':
                tr_lst.append(txt[2])
    return tr_lst