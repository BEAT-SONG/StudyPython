#  변수. 파이썬의 변구에는 제약이 거의 없다. 
a = '헬로우'
print(a)

a = 3.141592
print(a)

a = 10
print(a)

a = 999999999999999999999999999999999999999999999999
print(a)

a = 1/10 # Left value(왼쪽 값): 값을 할당 받는 것 a
print(a) # Right value(오른쪽 값): 값을 지정하는 것 print(a)

# 변수값을 지정(할당) - assign(할당) 방법
# 3 = a # 왼쪽 값이 변수를 담을 수 있는 상자가 되어야하는데 숫자는 변수를 담을 수 없다.
b = 3.141592
c = 'python'
d = (1, 2, 3) #  튜플
e = [1, 2, 3, 4] # 리스트
f = [7,'8', '$', a] # 파이썬의 장점!! 어떠한 값도 변수값으로 할당할 수 있다. 

# 변수명
# 숫자, 특수문자로 시작할 수 없다. / 영어 또는 한글로 시작해야한다. / 변수명은 띄어쓸 수 없다.
# _(언더바)는 가능하다. 특수문자의 예외
# 변수명을 지정할 때 의미를 포함하는 단어, 적당한 길이가 좋다.
# 변수명 지정 불가
val = 10
val2 = 0
val4 = 30
# 4val = 40
# -val = 50
# *val = 60
val_of_reaction = 99
chain_reaction = 108
# chain Reaction = 109
# val- = 111
# val$ = 99
val_ = 999
Val_ = 9080 # 대소문자 구분함.
print(val_)
print(Val_)
MyAccountOfBank = 1
은행계좌금액 = 1

# id는 변수를 나타내는 유일한 값. 메모리상의 변수의 위치를 나타내는 값.
# 변수값이 동일한 것인지 확인할 때 사용.
print(id(val_))
print(id(Val_))

# 변수타입 확인 type는 변수의 지정된 형태가 무슨 타입인지 알려주는 것.
print(type(val_)) # int
print(type(c)) # str
print(type(d)) # tuple
print(type(e)) # list
print(type(f)) # list
print(type(a)) # float


