from github import Github
from datetime import datetime

# generate access token
def push(file, text):
    access_token = "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"
    login = Github(access_token)
    user = login.get_user()
    repository_name = "algorithm"
    repo = user.get_repo(repository_name)
    contents = repo.get_contents("baekjoon")

    # 해당 디렉토리에 있는 파일 다 가져와서
    # 거기 안에 있으면 업데이트
    # 거기 안에 없으면 새파일 푸시
    lst = []
    file_name = file
    for content in contents:
        lst.append(str(content)[:-2].split('baekjoon/')[1])

    if '{}'.format(file_name) in lst:
        # 파일을 불러와서 바뀐게 있으면 업데이트 하는 방식으로 수정
        git_file = repo.get_contents('baekjoon/{}'.format(file_name))
        if git_file.decoded_content.decode() != text:
            repo.update_file(git_file.path, 'update {}'.format(datetime.today().strftime('%Y/%m/%d')), text, git_file.sha)
            print('UPDATE [', file, '] problem!')
        else:
            print('[',file,'] has no difference...')
    else:
        repo.create_file('baekjoon/{}'.format(file_name), 'upload {}'.format(datetime.today().strftime('%Y/%m/%d')), text)
        print('UPLOAD [', file, '] problem!')
    # print(lst)


# Delete test (폴더 안에 있으면 디렉토리를 옮겨줘야함.)
# contests = repo.get_contents('baekjoon/test1.py')
# repo.delete_file(contests.path, 'remove test', contests.sha)
# contests = repo.get_contents('test.py')
    # repo.delete_file(contests.path, 'remove test', contests.sha)