# 웹페이지 긁어오기
from urllib.request import Request, urlopen # from, import 개념 다시 찾아보기 # from에서 import를 가져온다.

req = Request('https://www.naver.com') # 네이버 웹페이지를 요청하는 것.
res = urlopen(req)

# status ? / >>> 200이라는 출력은 웹페이지를 찾았다. / >>> 404라는 출력은 웹페이지를 찾지 못했다는 것이다.
print(res.status) 

# 외부 request 패키지 추가 설치
# 'pip install requests'를 터미널창에 입력하면 설치된다.
# import requests
# url = 'https://www.naver.com'
# res = requests.get(url)

# # print(res.status_code)
# print(res.text)

