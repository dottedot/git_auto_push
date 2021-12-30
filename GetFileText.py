import os

def file_text(filenum):
    os.chdir('../../algorithm/baekjoon')
    path = os.getcwd()
    file_lst = os.listdir(path)
    # print(file_lst)
    file = ''
    for i in file_lst:
        if filenum in i:
            file = i
            break
    else:
        return '0', '0'
        
    data = open(file, 'r', encoding='UTF-8')
    lines = data.readlines()
    line = ''
    for i in lines:
        line += i
    return file, line