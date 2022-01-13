#-*- coding: utf-8 -*-

###                   ###
###    A Quick Fix    ###
###                   ###

# TODO : if i solve by python -> save python
#        if i solve by cpp -> save cpp
#        select the language that i solve 


from GetFileText import file_text
from GitPush import push

print('\n######### START #########\n')

problem = '1 Two Sum.cpp'
file, text = file_text(problem, 'leetcode_cpp')

if text != '0':
    push(file, text, 'leetcode_cpp')
else:
    print('Check the problem [', problem, ']')