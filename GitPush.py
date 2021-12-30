from github import Github
from datetime import datetime

# generate access token
def push(file, text):
    access_token = "[GIT_ACCESSTOKEN]"
    login = Github(access_token)
    user = login.get_user()
    repository_name = "algorithm"
    repo = user.get_repo(repository_name)
    contents = repo.get_contents("baekjoon")

    lst = []
    for content in contents:
        lst.append(str(content)[:-2].split('baekjoon/')[1])

    if '{}'.format(file) in lst:
        git_file = repo.get_contents('baekjoon/{}'.format(file))
        if git_file.decoded_content.decode() != text:
            repo.update_file(git_file.path, 'update {}'.format(datetime.today().strftime('%Y/%m/%d')), text, git_file.sha)
            print('UPDATE [', file, '] problem!')
        else:
            print('[',file,'] has no difference...')
    else:
        repo.create_file('baekjoon/{}'.format(file), 'upload {}'.format(datetime.today().strftime('%Y/%m/%d')), text)
        print('UPLOAD [', file, '] problem!')