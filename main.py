import time
from GetFileText import file_text
from OpenWeb import driver
from Login import login
from GetProblem import problem
from CheckToGoNext import Check
from GitPush import push

# generate driver
driver = driver()

# login
login(driver)

# if CAPTCHA -> you will solve it!
Check(driver)

print('\n######### START #########\n')

while True:
    # get problem number list
    problem_lst = problem(driver)

    for num in problem_lst:
        # get problem code 
        # text '0' : not solve this problem 
        file, text = file_text(num)

        if text != '0':
            push(file, text)

    print('\n waiting.. \n')
    time.sleep(5)