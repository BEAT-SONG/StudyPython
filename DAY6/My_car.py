# My_car.py

# import Class_Vehicle 
from Class_Vehicle import Car # Class_Vehicle 이 파일에서 Car을 가져와서 쓴다는 것을 의미.

if __name__ == '__main__':
    mycar = Car('25라 5600', '흰색')
    # mycar.차량번호 = '25라 5600'
    # mycar.색상 = '흰색'
    mycar.연료 = '경유'
    # mycar.__제조사 = '기아'
    mycar.출고년도 = 1999
    # mycar.기어단수 = 7 # Class_Vehicle에 '기아단수'가 없어도 여기서 변수를 지정할 수 있다.


    # print(mycar.__제조사)
    # print(mycar.연료)
    # print(mycar.기어단수)

    mycar.set제조사('쌍용')
    mycar.제조사확인() # import에서 불러온 Class_Vehicle과 연동되지 않아 '__제조사'가 새로운 변수로 생성되어 잘 연동된거처럼 보이지만 연동되지 않았음.
    
    mycar.전진한다(2)
    print(mycar)