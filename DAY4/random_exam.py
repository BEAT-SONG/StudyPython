# random 함수
import random

print(random.choice(range(1, 7))) # 주사위

# lottery(lott)
numbers = list(range(1, 46))
lottery = [] # list

for i in range(6): # 6번 반복한다는 내용을 담은 for문
    lottery.append(random.choice(numbers)) # append 함수 찾아보기 # numbers 변수에서 랜덤하게 lottery list에 나타내라.

print(lottery)


# lottery(lott)
from random import*
numbers = list(range(1, 46))
lottery = [] # list

for i in range(6):
    lottery.append(choice(numbers))

# print(lottery)

# 중복을 없애보자 완성 못함.. 이해 안된
# import random
# numbers = random.randrange(1, 46)
# lottery = [] # list

# for i in range(6): # 6번 반복한다는 내용을 담은 for문
#     while numbers in lottery: # 중복될 경우 다시 실핼
#         numbers = random.randrange(1, 46)) #랜덤 수 생성
#     lottery.append(numbers) # 중복되지 않는 경우에만 추가

# print(lottery)


