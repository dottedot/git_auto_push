#-*- coding: utf-8 -*-

import os, priv_user


def file_text(problem_num, algo_lang):                  # algo_lang : [boj_python, boj_cpp, leetcode_cpp]
    
    if algo_lang == 'boj_python':                       # git push file name shape
        os.chdir(priv_user.CODE_DIR+'/BOJ/Python')      # head + problem_num + file_extension
        head, lang = '[Python]BOJ_', '.py'              # head : head
    elif algo_lang == 'boj_cpp':                        # lang : file_extension
        os.chdir(priv_user.CODE_DIR+'/BOJ/C++')
        head, lang = '[C++]BOJ_', '.cpp'
    elif algo_lang == 'leetcode_cpp':
        os.chdir(priv_user.CODE_DIR+'/LeetCode/C++')
        head, lang = '[C++]LeetCode_', '.cpp'

    path = os.getcwd()
    file_lst = os.listdir(path)
    file, file_name = '', ''

    for i in file_lst:                                  # To find the problem that i solved
        if problem_num in i:                            # if the problem in file_list
            file_name = head + i.split()[0] + lang      # file = i and break
            file = i                                    # else; return '0', '0'
            break                                       # '0', '0' filter in "main.py"
    else:
        return '0', '0'

    data = open(file, 'r', encoding='UTF-8')
    lines = data.readlines()
    line = ''

    for i in lines:
        line += i

    return file_name, line