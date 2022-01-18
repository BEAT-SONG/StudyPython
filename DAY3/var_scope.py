# 변수 라이프스코프
a = 1 # 매개변수 a 는 전역변수. 전체에서 쓰이는 변수.
# res = 0 # 프로그래밍을 할때는 원래 변수를 지정해 줘야한다. 그런데 파이썬에서는 변수를 지정 없이 사용이 가능하다.
# 아래는 '함수의 선언'이다. 함수를 만들었으니 다음에 쓸 수 있다는 것을 나타내는 것이다. 이 함수는 9번에서 사용하였다.
def vartest(a): # 매개변수 a 는 지역변수. 4,5,6에서의 a 
    a = a +1
    return a

res = vartest(a) # 선언된 함수가 나오는 순간 '함수의 선언'이 된 곳으로 가서 함수를 수행하고 다시 돌아와서 값을 수행한다.
print(res)

# a = 1 # 매개변수 a 는 전역변수. 전체에서 쓰이는 변수.

# def vartest(x): # 매개변수 x 는 지역변수. 4,5,6에서의 x
#     x = x +1
#     return x

# a = vartest(a)
# print(a)

# 변수는 값을 할당할 수도 값으로 사용될 수도 있다.

a = 10 # 전역변수.

def vartest(a): # 지역변수.
    a = a +1
    return a

a = vartest(a) 
print(a)

a = 10 # 전역변수.
res = '송은' # 변수를 지정하는 것. = 변수의 상자를 만들어 주는 것이라고 생각하면 된다. 파이썬에서는 변수를 지정할 때 숫자나 '글자'를 사용하는 것 둘 다 가능하다. 그런데 다른 언어에서는 '글자'를 변수로 지정하는 것이 불가능하다.

def vartest(x): # 지역변수.
    x = x +1
    return x # 반환. 함수를 사용한 곳으로 다시 돌아가서 사용될 것이다. 

res = vartest(a) 
print(res)

