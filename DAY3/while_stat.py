# While 문
hit = 0 # 컴퓨터는 0에서 부터 시작한다. 

while hit < 100: # 이 값이 참인 동안
    hit += 1 # 'hit = hit + 1'와 같은 함수이다. # 사람은 보통 1에서 부터 시작한다. 
    
    if hit > 10:
        break

    print(f'나무를 {hit}번 찍습니다.')

# for 문 
for hit in range(1, 101):
    print(f'나무를 {hit}번 찍습니다.')

for hit in range(0, 100):

    if hit >9:
        break

    print(f'나무를 {hit+1}번 찍습니다.')



