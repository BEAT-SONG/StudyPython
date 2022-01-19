# 파일 입출력

# 파일 출력. open 했으면 반드시 close 해야한다. 
# f = open('newfile.txt', 'w') # w: write 쓴다. 파일 출력. 
# f.close()

# 특정경로에 파일 생성
# f = open('c:/Sources/Sample/test.txt', 'w')
# f.close()
# print('파일이 생성되었습니다.)

# # newfile.txt 파일 입력(읽어오기)
# f = open('newfile.txt', 'r', encoding='utf-8') 
# while True: # 무한 루프(반복). 
#     line = f.readline() # 안의 내용을 한 줄씩 읽을 것이다.(입력) 
#     if line == '': # if line is '': # if not line: '다 같은 출력을 표현한다.' # 값이 없으면 빠져나간다. = 줄에 글이 있으면 다시 돌아가서 읽고 다 읽고 줄에 글이 없으면 무한루프를 빠져나간다.
#         break # 무한 루프를 빠져나간다.
    
#     print(line) # 우리 눈에 보이게 출력

# f.close

# # for 문으로 표현
# f = open('newfile.txt', 'r', encoding='utf-8') 
# lines = f.readlines()
# for line in lines:
#     print(line)

# f.close

f = open('newfile.txt', 'r', encoding='utf-8') 

for line in f:
    print(line.replace('\n', ''))

f.close