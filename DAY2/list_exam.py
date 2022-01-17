# 리스트 연산. 리스트를 만드는 방법. range를 이용하면 원하는 범위내의 list를 보다 쉽게 만들 수 있다.
from pprint import pp


arr = list(range(5)) # range를 이용하면 빠르게 list를 만들 수 있다.
print(arr)

arr = list(range(1, 6)) # 내가 원하는 숫자가 5까지이면은 1을 더해서 6이라고 입력해야한다.
print(arr)

arr = list(range(2, 101, 2)) # range(시작 숫자, 마지막 숫자 + 1, 증감양)
print(arr)

print(arr[0] + arr[5]) # 인덱스 0번째 값과 인덱스 5번째 값의 합을 출력. []는 리스트라는 의미.

# 2차원 배열(리스트)
print() # 한 줄 띄어준다.
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])
print(arr2[2]) # ['Hi', 'My', 'Friend'] 배열이 나옴.
print(arr2[2][1]) # 2번째 리스트에 인덱스 1번에 있는 문자열을 출력.
print(arr2[2][1][0]) # 2번째 리스트에 인덱스 1번에 있는 문자열에서 인덱스 0에 있는 문자를 출력.

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)
# print(arr3 + 3) # can only concatenate list. 오류.
print(arr3 + arr)
print(len(arr)) # arr의 갯수
print(len(arr3)) 

# 리스트 함수
print('--리스트 내장함수')
del(arr3[1]) # arr3에서 인덱스 1번 값을 지운다. 인덱스로 지워야할 경우에 사용.
print(arr3) 

arr3 .remove(1) # arr3에서 1값을 지운다. 값을 지워야 하는 경우에 사용.
print(arr3)

arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5] # 규칙이 없는 값을 경우에는 입력해야하는 경우가 많다.
arr4 .remove(3) # 값을 지우는데 중복된 값이 있으면 앞의 값만 제거한다. / 값을 찾아서 삭제
print(arr4)
del(arr4[8]) # 리스트 인덱스로 삭제.
print(arr4)

# sort(): 리스트에 있는 값을 오름차순으로 정렬.
arr4.sort()
print(arr4)

# reverse(): 리스트에 있는 값을 내림차순으로 정렬.
arr4.reverse()
print(arr4)

arr4.insert(2, 10) # .insert(추가할 인덱스의 값, 추가할 값) 인덱스가 2인 곳에 10을 추가하여라.
print(arr4)

arr4[0] = 108
print(arr4)

print()
print( '--튜플')
tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# 'tuple' object does not support item assignment. 튜플에서는 값을 할당할 수 없다. 튜플은 수정, 추가, 삭제가 불가능한 함수이다. 
# tup1[0] = 99
# print(tup1) 

# 딕셔너리. 값을 마음대로 지정할 수 있다. 
print()
print('--딕셔너리')
dic1 = {1 : 'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'Huge'
print(dic1)
print(type(dic1))

del dic1['name']
print(dic1)

print(dic1.keys()) # 앞에꺼
print(dic1.values()) # 뒤에꺼
print(dic1.items())

# 리스트를 큐플로 변환
print()
print('--리스트/튜플 변화')
print(arr4)
tup2 = tuple(arr4) # 튜플로 변환. 값의 수정, 추가, 삭제 불가능
print(tup2)

arr4.sort()
# tup2.sort() # 불가능

print()
print(tup1)
arr5 = list(tup1) # tuple을 list로 변환.
print(arr5)
arr5.append(6) # list에서 append를 통해 '6'값을 추가할 수 있다.
print(arr5)
tup1 = tuple(arr5) # list를 tuple로 변환.
print(tup1)

