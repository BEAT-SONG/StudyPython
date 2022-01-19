# 파일 쓰기
f = open('writefile.txt', 'w', encoding='utf-8') # 처음으로 쓸때는 w를 써야한다. 

f.write('저는 한국사람입니다. \n')

texts = ['저는 한국사람이죠.\n', '이번에 2022년이 되었습니다.\n'] # list
f.writelines(texts)

f.close

f = open('writefile.txt', 'a', encoding='utf-8') # a를 이용해서 내용을 추가할 수 있다. + r을 이용해서 읽어올 수 있다.
f.write('내용 추가할께요!')
f.close

