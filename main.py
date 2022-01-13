#-*- coding: utf-8 -*-

# TODO : if i solve by python -> save python
#        if i solve by cpp -> save cpp
#        select the language that i solve 

import time
import OpenWeb, Login, CheckToGoNext
from GetFileText import file_text
from GetProblemInBOJ import problem
from GitPush import push

driver = OpenWeb.driver()                                   # Generate driver
Login.login(driver)                                         # Login to BOJ
CheckToGoNext.check(driver)                                 # If CAPTCHA -> you will solve it!
problem_lst = problem(driver)                               # Get problem number, return list

for problem_num in problem_lst:
    file, text = file_text(problem_num, 'boj_python')       # Get problem 'NAME', 'CODES'
                                                            # boj_python // boj_cpp // leetcode_cpp
    if text != '0':                                         # If text '0' not solve this problem
        push(file, text, 'boj_python')                      # or my filename is different
    else:                                                   # so check this.
        print('Check the problem [', problem_num, ']')