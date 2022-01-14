# 주석입니다. 소스 코드 처리에 아무 영향을 주지 않는다.
# 문자열 표현 방법.
print('"Hellow, World"')
print("'Hellow, World'")
# print(''Hellow, World'') # 문법이 맞지 않는다. 따움표 사이에 표현하고자 하는 글이 없어서 안됨.

# 숫자 연산 출력
# print()를 활용.
print('3+4')

# 변수사용.
# 변수는 값을 담는 그릇
a = '안녕하세요'
b = '방갑습니다'
print(a)
print(b)
print(a, b)
print(a, b, '정말?')

# 수학 연산.
print(5+6)
print(5-6)
print(5*6)
print(5/3) # 5를 3으로 나눈 정확한 값.
print(5//3) # 5를 3으로 나누고 나머지는 버린다. 정수로 나눈다.
print(5%3) # 5를 3으로 나누고 나머지 값. 원래 값이 어떤 배수인지 확인하기 위해 사용.
print(2**10)

print(int (5/3)) #..?
print(int('10'))
#print(int('십')) # 오류가 난다. int는 숫자를 이용한 함수 이다. 형변환이 안됨

print(float(5)) # float는 소수점을 나태내는 함수. 형변환

# type 확인
# ..? 아마 정수인지 실수인지 타입을 확인해주는 함수인듯.
print(type(10)) # 정수(int)가 나옴.
print(type(10.0)) # 실수(float)가 나옴.

# 괄호 (연산자 우선순위)
# 어떠한 연산자를 사용하든 괄호가 1순위이다.
print((2+3)*5)
print(2+(3*5))

