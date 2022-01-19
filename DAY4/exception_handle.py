# exception_handle.py
# 예외처리!! 가장 중요한 내용!!!!!!!!!

def add(a, b): # 지역변수
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    res = a/b
    return a / b

print('사칙연산 시작')

a, b = 4, 1 # 전역변수
numbers = [3, 6, 9] # list 생성

try:
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 8 
    num = int(input('수를 입력하세요'))


except ZeroDivisionError as e: # ZeroDivisionError(Exception도 가능)를 e로 줄려서 쓰기 위함. # 모든 Error를 포함하는 가장 높은 등급의 Exection이댜.
    print(f'나누기 예외!, 추가처리1 {e}') # 예외가 무엇인지 출력하는 기능.
except IndexError as e: # 예외에 따라서 예외처리의 방법이 다르게 해야할 경우도 있다.
    print(f'인덱스 예외!, 추가처리2 {e}')
except ValueError as e:
    print(f'제발! 좀 숫자만 넣으라고!!!!')
except Exception as e:
    print(f'알수없는 예외!, 추가처리3 {e}')
finally:
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')


print('사칙연산 종료') # 정상적으로 종료되었는지 확인할 수 있는 쿼리. / 이 문장이 안 나오면 예외이다. 



