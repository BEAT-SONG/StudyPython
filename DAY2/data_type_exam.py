# 자료형
print(None)
print(type(None))

print(0 == None)
a = None # a를 None으로 지정할 수 있다. 
print(a)
print(type(a))

# 숫자형 
금액 = 12_345_666 # _(언더바)는 우리가 입력할 때 편하기 위해서 사용하는 것이고, 출력되지 않는다.
print(금액)

# 문자형
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

bruce_eckel = 'Life is short.\nYou need Python' # \n (탈출문자): 새로운 줄에서 출력하겠다.
print(bruce_eckel)

bruce_eckel = 'Life is short.\\You need Python' # \\ : \(역슬래시)를 사용하고 싶을때 두번 적어야한다.
print(bruce_eckel)

# ''' ''' : 여러줄을 적고 싶을 때 사용하는 것. 이때 \n을 사용하면 두줄이 띄어진다.
bruce_eckel = '''Life is short.
You need Python.
난 필요없는데... 파이썬...''' 
print(bruce_eckel)

# 불형(Boolean, Bool)
val_sum = 1000
print(val_sum == 1000) # True
print(val_sum == 999) # False
# print(val_sum = 10) # 이런 입력을 할 수 없다는 것을 알려줌. 오류.

bl_true = True # True도 하나의 값으로 입력할 수 있다.
print(bl_true)
print(type(bl_true))
# 아래 두개의 함수는 같은 출력을 나타낸다.
print(bl_true == True) # True
print(bl_true is True) # True

print(a is None) # True
print(val_sum is 1000) # True

# 의미가 있는 Bool
print(bool(1)) # 1은 True
print(bool(2)) # 1이상은 모두 True. 주로 1로  True를 표현.
print(bool(0)) # 0은 False

# list []. 어떤 특정 값들이 들어간 것을 반복적으로 처리할 때 사용. 1차원 배열
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

arr2 = ['Life', 'is', 'short', 'U', 'need', 'Python', 3]
print(arr2)

# 이차원 배열. 행렬에 활용 가능. 3차원 배열은 거의 사용하지 않는다. 거의 2차원 배열까지만 사용함.
arr3 = [[1,2,3], [4,5,6]] 
print(arr3)

# 빈 리스트 생성. 빈 리스트는 None이 아니다.
arr4 = list()
print(arr4)

# 튜플
tuple = (1,2,3,4,5)
print(tuple)

# 딕셔너리
spiderman = {'name' : '피터파크', 
             'age' : 18, 
             'weapon' : '웹슈터'}
print(spiderman)

# 집합. 중복되는 요소를 제거할 때 사용하는 것.
set_int = set([1,2,3,4,5,4,6,7,1,2,3,4])
print(set_int)


