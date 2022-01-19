# 부산 버스 노선별 이용건수
import csv

file_name = '부산버스정보.csv' # 파일이름을 할당한다. 
f = open(file_name, mode = 'r', encoding='utf-8') 

reader = csv.reader(f, delimiter = ',') # ,(쉼표)는 구분자(delimiter) 중 하나이다. 쉼표를 구분자로해서 csv를 읽어라.(입력)
next(reader) # 제일 앞 줄(헤더)를 없애주는 역할을 한다.
for line in reader: # reader을 line이라는 변수로 지정
    print(line)

f.close

