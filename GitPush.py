#-*- coding: utf-8 -*-

from github import Github
from datetime import datetime
import priv_user

def push(file, text, algo_lang):                                            # algo_lang : [boj_python, boj_cpp, leetcode_cpp]
    now_date = datetime.today().strftime('%Y/%m/%d')
    user = Github(priv_user.GIT_ACCESS_TOKEN).get_user()                    
    repo = user.get_repo(priv_user.GIT_REPO_NAME)
    
    if algo_lang == 'boj_python':
        content_dir = "BOJ/Python"
    elif algo_lang == 'boj_cpp':
        content_dir = "BOJ/C++"
    elif algo_lang == 'leetcode_cpp':
        content_dir = "LeetCode/C++"

    contents = repo.get_contents(content_dir)
    lst = []

    for content in contents:                                               
        lst.append(str(content)[:-2].split('{}/'.format(content_dir))[1])   
    
    if '{}'.format(file) in lst:                                            # Find if the file is in the repository 
        git_file = repo.get_contents('{}/{}'.format(content_dir, file))     # If the file is in the repository
                                                                            # Update or no difference.
        if git_file.decoded_content.decode() != text:                       # If the code different
            repo.update_file(git_file.path,                                 # Update and git push!
                'update {}'.format(now_date), text, git_file.sha)           # else print no differences
            print('UPDATE [', file, '] problem!')
        else:
            print('[',file,'] has no differences...')
    else:                                                                   # If the file is not in the repository
        repo.create_file('{}/{}'.format(content_dir, file),                 # Upload the file
            'upload {}'.format(now_date), text)
        print('UPLOAD [', file, '] problem!')