# 연산자
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 2
print(a % b) # 3

# 문자열 연산. 문자열 연산에서는 +와 *만 있다.
stat1 = 'Hello'
stat2 = 'World'
res = stat1 + stat2
print(res)
res = stat1, stat2
print(res) # 튜플
print(stat1 + stat2) # 두 문자열의 합. 오라클에서는 ||의 기능.
print(stat1, stat2) # 두 문자열의 나열
# print(stat1 - stat2) # 문자열의 경우 -(빼기)는 불가능
print(stat1 * 5) # 문자열의 곱
# print(stat1 * stat2) # 두 문자열의 *(곱)은 불가능
# print(stat1 / 3) # 문자열의 경우 /(나누기)는 불가능

# 문자열 길이. len(): 문자열의 길이를 나타내는 것. 
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업[]
# 문자열 = 문자의 배열. 문자의 순번 = 인덱스. 0부터 시작한다. 배열 5개(0, 1, 2, 3, 4)
# 오라클이 예외로 1부터 시작한다. 
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])
# print(stat3[5]) # string index out of range: 5번째가 없는데 입력했다는 것을 표현. 오류

# stat3[0] = '저'
# stat3[1] = '리'
# print(stat3)

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기. 원하는 것만 뽑아 출력하기.
일시 = '2022-01-17 14:39:25'

print(일시[:4], '년')
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:13], '시')
print(일시[14:16], '분')
print(일시[17:], '초')

print(일시[-5:-3], '분')

list_a = [1,2,3,4,5]
list_a[1] = 19 # 숫자열의 경우는 값을 수정할 수 있다. 
print(list_a)

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

# 문자열 포맷팅
str1= "I'm so happy {0} U".format('to') # 문자열 객체 . format()
print(str1)

str1= "I'm so happy {0} U. are {1}?".format('to', 'you' ) # 문자열 객체 . format()
print(str1)

첫번째단어 = '투'
두번째단어 = '유'
str1= "I'm so happy {0} U. are {1}?".format(첫번째단어, 두번째단어)
print(str1)

# 제일 최신의 포맷팅이다. 제일 효율적인 포맷팅 쿼리.
str2= f"I'm so happy {첫번째단어} U. are {두번째단어}?"
print(str2)

# 숫자 천단위 콤마 (',d)
money = 10000000000000
print(format(money, ',d'))

from datetime import datetime
from time import strftime

now = datetime. now() # 현재 일시 생성
print(now)
print(now. strftime('%Y년 %m월 %d일 %H:%M:%S'))
print(now, strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math

myPi = math.pi
print(myPi)

print('{0}'.format(myPi))
print('{0:0.6f}'.format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}')
print(f'{myPi:0.2f}')

fullname = 'Park Song Eun'
age = 24
greeting = '''안녕하세요, 저는 {0}입니다. 
나이는 {1}이구요.''' .format(fullname, age)
print(greeting)

fullname = 'Park Song Eun'
age = 24
greeting = f'''안녕하세요, 저는 {fullname}입니다. 
나이는 {age:0.1f}이구요.'''
print(greeting)

part_name = fullname. split() # split() 띄어쓰기를 기준으로 fullname을 나눈다.
print(type(part_name)) # split을 통해서 문자열을 3개로 나누었다. 이것이 3개로 나열이 되므로 문자열의 타입은 리스트가 된다.
print(part_name)

test = 'Hey, guys'
print(test. split(','))

#|
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|') # |를 기준으로 나눈다.
print(split_codes)

# 단어교체 replace
fullname.replace('Song Eun', 'Andy')
print(fullname.replace('Song Eun', 'Andy'))

#
aaa = '        Hello, World         '
print(aaa. lstrip())
print(aaa. rstrip())
print(aaa. strip())

print(fullname. index('P')) # 0
print(fullname. index('a')) # 1
print(fullname. index('r')) # 2
print(fullname. index('k')) # 3
# print(fullname. index('x')) # substring not found. 예외. fullname에서 x를 찾을 수 없다.

print(fullname. find('x')) # -1 이 나오면 fullname에는 x가 없다는 것을 의미한다.
print(fullname. find('ark')) # fullname에서 ark는 index 1에서 시작된다는 것을 의미한다.

print(fullname. count('a')) # fullname에서 a는 1번 나온다는 것을 의미한다. 

print('-'. join(fullname)) # fullname에 모든 글자 사이에 -를 추가하는 것을 의미한다. 

print(fullname. upper()) # fullname에 모든 글자를 대문자로 만든다.
print(fullname. lower()) # fullname에 모든 글자를 소문자로 만든다.


