# Vehicle.py
class Car:
    차량번호 = '45나 4565'
    __제조사 = '현대' # '__제조사'는 변수로 활용되지 않았다. 즉 연동되지 않았다.
    색상 = '흰색'
    연료 = '가솔린'
    출고년도 = 2018

    def __init__(self, 차량번호, 색상) -> None:
        self.차량번호 = 차량번호
        self.색상 = 색상

    # '__str__'를 아래와 같이 재정의하였음.
    def __str__(self) -> str: # 문자열을 retrun 해줘야한다는 것이다.
        return f'제 차는 {self.출고년도}년도에 만들어진 {self.연료} 차량입니다.'
  
    # private
    def set제조사(self, 제조사):
        self.__제조사 = 제조사
  
    def 제조사확인(self):
        print(f'제조사는 {self.__제조사}이다.')

    def 전진한다(self, level):
        print(f'{self.차량번호} {self.색상}의 차가 {level}단으로 앞으로 달린다.')

    def 후진한다(self):
        print('뒤로 달린다.')

    def 좌회전한다(self):
        print('왼쪽으로 달린다.')

    def 우회전한다(self):
        print('오른쪽으로 달린다.')

    def 멈춘다(self):
        print('멈춘다.')


