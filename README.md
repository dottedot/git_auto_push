# GIT AUTO PUSH



### Tech Stack

![Python](https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white) &nbsp;

![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white) &nbsp;





## 만든 이유 (v1.0)

> 1일 1잔디를 위해 백준 문제를 풀어 올리고싶었습니다. 
>
> 하나하나 깃 푸시 하는게 너무 귀찮았습니다. 
>
> Selenium도 공부하고, git api도 공부해볼겸 만들어 보았습니다. 
>
> git api는 사용하지 못했습니다. => 공부해서 발전시켜볼 생각입니다.



## GIT AUTO PUSH 실행 설명

- 실행파일 이름 : main.py



## GIT AUTO PUSH 기능 설명

1. 백준 사이트에서 개인 그룹을 하나 만들어 준다. -> 해당 그룹을 url로 설정해 프로그램 실행

2. git repo 만들고 token 발급받는다.

3. 코드의 GitPush.py와 Login.py에 자신의 Token, ID, PASSWD를 넣는다.

- GitPush.py

- TOKEN  

  ```access_token = "[GIT_ACCESSTOKEN]"```

- Login.py

  - ID  

    ```action.send_keys('[BAEKJOON_ID]').perform()```

  - PASSWD  

    ```driver.find_elements_by_css_selector('.form-control')[1].send_keys('[BAEKJOON_PASSWD]')```
  

4. 백준에서 문제를 푼다.

5. 문제를 다 풀었으면 main을 실행 -> 가끔가다가 캡챠에 걸릴때가 있는데 직접 풀어줘야한다.



----

----



## Update (v1.01)

- Make `.gitignore`, `secrete file`, `cppmain.py`
- Make the code clean
- Write the remark



### 1. gitignore

- Fill the **priv user file** => hide priv file!
- Fill the test file



### 2. secrete file

- To hide user privacy.
  - BOJ ID
  - BOJ PWD
  - URL
  - GIT TOKEN
  - GIT REPOSITORY
  - etc..



### 3. cppmain.py

- A Quick Fix