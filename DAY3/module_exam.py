# module_exam.py
# import math
# print(math.pi)

# from math import * # 이런 쿼리를 사용할 경우, 함수명이 충돌하는 것을 예방할 수 없다.
# print(pi)

from math import pi, sqrt, sin, cos # *(all)로 가져오는 것보다 필요한 함수만 가져와서 사용한다면 쿼리의 경량화가 가능하다. 
print(sin(3))
print(cos(4))
# print(tan(4)) # *(all)이라고 두지 않고 위와 같이 모듈에서 사용할 것을 지정할 경우에는 지정되지 않은 함수는 실행(출력)이 되지 않는다. 