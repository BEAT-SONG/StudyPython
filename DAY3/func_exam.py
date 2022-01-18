# 함수 선언 및 사용

# 더하기 함수 선언
from audioop import mul


def add(a, b):
    res = a+b

    return res # 값을 반환해 주는 것. 값을 되돌려 주는 것.

# 함수 선언
print(add(3, 4))
print(add(2464, 879))

mid_val = add(3, 4)
print(mid_val)
print(mid_val * 3)

# print(add(6)) # 오류. 함수 add(a, b)로 지정되었는데 하나의 값만 입력했기 때문에

# 함수종류
# 매개변수(입력값) 없는 형태
def say_hello():
    return 'Hello~' # return 뒤의 값으로 변환되어 출력된다고 생각하면 된다. 

print(say_hello())
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o~', '')) # '~o'를 ''로 대체해라! .replace('o~', '')

# 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')
   # return None # None 값을 되돌려줘도 아무 관련이 없으므로 생략이 가능하다. 

say_hello('Song')

# 둘다 없는 경우
def say_goodbye():
    print('Bye bye~')
   # return None # None 값을 되돌려줘도 아무 관련이 없으므로 생략이 가능하다. 

say_goodbye()

# 매개변수를 지정하는 경우
def multi(a, b):
    return a*b

print(multi(2, 9))

# 매개변수 개수가 가변적인 경우. 하이파이트! 생소하다.
def plus(*args): # *args: 매개변수의 개수가 얼마인든 결과값이 잘 나온다.
    res = 0
    for i in args:
        res +=i

    return res
print(plus(1,2,3))
print(plus(1,2,3,4,5,6,7,8,9,10))
print(plus())

# 리턴값이 2개 이상
def mul_and_div(x,y):
    mul = x*y
    div = x/y

    return (mul, div) # 튜플

(res1, res2) = mul_and_div (7,8)
print(res1, res2)

def 사칙연산(x,y):
    return (x+y, x-y, x*y, x/y)

(res1, res2, res3, res4) = 사칙연산(9,5)

print(res1, res2, res3, res4)
print(type(사칙연산(1,2)))
