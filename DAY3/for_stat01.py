# 기본 for문

arr = [1, 2, 3, 4, 5]

for i in arr:
    print(f'{i}')

print()

for i in arr:
    print(f'{i:2.1f}')

print()

arr = list(range(1,101)) # list[]와 range(,)를 이용해서 원하는 값을 더 쉽게 변수로 지정할 수 있다.
for i in arr:
    print(f'{i:2.1f}')

print()

arr = list(range(990,1001)) 
for i in arr:
    print(f'{i:2.1f}')

# 튜플로 for문
arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:
    print(f'{item}')

print()

for item in arr2:
    print(item)
    print(f'{item :>10}') # 오른쪽으로 보내라. 10칸. ':>10' 이렇게 합쳐서 적는 것 자체가 함수인듯

print()

for item in arr2:
    print(f'{item :>10}')
    print(item)

# 합계 for문
numbers = list(range(1, 21, 2)) # 1부터 20까지 홀수 계산.
print(numbers)
res = 0 # ?
for item in numbers:
    res += item # res에 ite를 합한것이다.

print(f'{numbers[-1]}까지의 총 합은 {res} 입니다.') # 다시 알아보기?

# 홀수, 짝수 구분
numbers = list(range(1, 21)) # 1부터 20까지

for item in numbers:
    if item % 2 == 0: # 짝수
        print(f'{item}은 짝수')

print()

for item in numbers:
    if item % 2 != 0: # 홀수/ if item % 2 == 1:
        print(f'{item}은 홀수')

# 13이상이면 탈출(break) 또는 계속(contiue)
numbers = list(range(1, 21)) # 1부터 20까지

for item in numbers:
    if item > 12:
        break # break문. 탈출. 더 이상 출력하지 않는다. 이 조건에 부합하면 더 이상 출력하지 않는 것을 포함하는 함수.

    if item % 2 == 1: # 홀수
        print(f'{item}은 홀수')

numbers = list(range(1, 21)) # 1부터 20까지

for item in numbers:
    
    if item % 2 == 1: # 홀수
        print(f'{item}은 홀수')

    if item > 12:
        break # break문. if문의 제일 먼저 적어야 원하는 출력값을 얻을 수 있을 것이다.

for item in numbers:
    
    if item % 2 == 1 and item < 12:
        print(f'{item}은 홀수') # 이것도 가능

numbers = list(range(1, 21)) # 1부터 20까지

for item in numbers:
    if item == 15:
        continue # 반복문을 수행하는데 15인 경우에는 아래 반복문을 수행하지 않고 다음 값으로 넘어간다. 그 조건값만을 빼고 반복문을 수행하고 싶을 때 사용하는 함수.

    if item % 2 == 1: # 홀수
        print(f'{item}은 홀수')

# 구구단. 이중 for문이 들어가야 한다. 삼중 for문으로 가면 출력 속도가 느려질 수 있다. 
print('구구단 프로그램')
for i in range(2, 10): # 2 ~ 9
    if i == 7:
        break # 6단 까지 출력
    # if i == 8:
    #     continue # 8단을 빼고 출력
   # print(f'{i}단 시작')
    for j in range(1, 10): # 1 ~ 9
        print(f'{i} X {j} = {i*j:2d}', end ='   ') # nd: 출력값을 n-1칸 띄어준다는 의미. 주로 줄을 맞춰줄 때 사용하는 함수.
        # "end =' '" 는 한 줄 내리는 것이 아니라 옆으로 ' '로 나누겠다는 함수.
    print('') # 첫번째 for문에 속하는 것. 2 ~ 9에서 한번 돌리고 한 줄 띄어주는 것. print()와 print('')는 같은 의미의 함수로 둘다 한줄 띄어주는 역할을 함.

# inline for 문
a = [1,2,3,4]
result = [i * 3 for i in a]
print(result)

# 기존 for 문 / 위의 쿼리 출력과 같은 출력이 나온다.
t = []
for i in a:
    t.append(i*3) # ?
print(t)