# a = [1,2,3,4]
# print(type(a))
# print(len(a))

a = [[1,2], [2,3,4], [5,6,7,8]]
print(type(a))
print(len(a))
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))

# print(a*2) 

# # 리스트와 행렬의 차이점
# # 행렬주고에 특화된 numpy 모듈에 대해서 먼저 학습
# # 행렬은 반드시 행과 열의 갯수가 인덱스마다 같아야하고, 연산이 가능함... 자료의 성격이 같아야한다.
# # 행렬에 특화되어 있는 모듈은 numpy이다. 
# ## list 자제를 2배하는 것이 아니라 그 안의 값에 사칙연산을 하고 싶은 경우에는 행렬을 만들어 내야한다.
# a = [1,2,3,4]
# b = [10,20,30,40]
# val = 3
# cc =[]
# for x1, x2 in zip(a,b):
#     cc.append(x1+x2)
# print(cc)

# # 자릿수가 다른 경우에는 하나의 list가 있다고 취급되서 계산이 안된다.
# # numpy로 만든 경우에는 행과 열이 같게 만드는 것을 권장하고 이것을 array를 이용해서 사용.
# # 이렇게 하나가 안에 들어가서 하나씩 계산이 되는 것을 '브로드캐스팅'이라고 한다.
# # np.shape()이라는 명령어는 list에서만 사용한다.
# # 변수.shape 이라는 명령어는 array구조에서만 사용된다.
import numpy as np
x = [[1,2,3], [22,33,44]]
val = 100
x2 = np.array(x) # list를 배열로 바꿔줌
x3 = x2 + 100 # x2 + [[100,100,100], [100,100,100]]
x2 + [[5,7,10]] 
print(x3)

# # 1개의 픽셀에 0-255이 값이 들어가면 그레이드스케일(0은 검정, 255은 흼색)
# # 차트 그리는 전문적이 프롯 matplotlib
# import matplotlib.pyplot as mp
# x=[[0,255,100], [255,0,200]]

# x2 = np.array(x)
# x3= x2-300
# print(x3)
# plt.imshow(x,cmap='grey') 


