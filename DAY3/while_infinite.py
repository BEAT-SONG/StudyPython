# 무한루프. 콘솔프로그램을 만들때 사용.
# 비정상 종료를 통해 종료가 가능하다.
# 회원정보 프로그램을 제작할 수 있는 가장 기초적인 쿼리.
# val = 0

# print('회원정보 프로그램')

# while True:
#     print(''' 작업할 번호를 입력하세요.
#     1. 회원입력
#     2. 회원검색
#     3. 회원수정
#     4. 회원삭제
#     5. 종료
#     숫자입력 : ''', end='')
#     val = int(input()) # 입력. 숫자 입력은 int()이다.

#     if val == 1:
#         print('회원입력화면으로 전환') 
#     elif val == 2:
#         print('회원검색화면으로 전환')
#     elif val == 3:
#         print('회원수정화면으로 전환')
#     elif val == 4:
#         print('회원삭제화면으로 전환')
#     elif val == 5:
#         break
#     else:
#         print('1~5사이의 수를 입력하세요.')
#         continue

# print('회원정보 프로그램 종료')

# *로 나무 만들기
a = '*'
b = '**'
c = '***'
d = '****'
e = '*****'
print(a)
print(b)
print(c)
print(d)
print(e)

for a in range(0, 10):
    print('*' * (a+1))

a = 0
while a < 10:
    a +=1
    print('*' * (a))





    
