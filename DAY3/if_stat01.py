# if구문 _ 흐름제어
# name = '태경'
name = ('송은', '태경', '은송', '다원') # 리스트, 튜플 사용 가능.

# if name == '송은' or name == '태경'
if '송은' in name: # if 구문이 끝난다는 것을 알려주는 표시.
    print('의사를 만나러 갑니다.') # 참(Ture)가 아닌 경우 어떠한 출력도 나타나지 않는다. 
    print('의사선생님께 인사합니다.')
elif name == '다원': # 참일 조건을 2개 만드는 느낌.
    print('주사실로 갑니다.')
else:
    print('호출할때까지 대기합니다.') # 거짓(False)인 경우에 어떠한 출력을 나타낼 것인지 else를 이용해서 나타낸다.




