# Oracle_data.py
# cx_oracle 설치 :  pip install cx_oracle

import cx_Oracle as ora

# makedsn('호스트명/ip주소', portnum, '서비스명') # portnum(포트) = 연결 호스(길) = 프로그램에 따라 포트가 다양하다.
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 내 컴퓨터에 있는 Oracle(DB)을 가져올 것이라서 'localhost'를 이용하는 것이다.

# connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding= 'utf-8')

# 'cur = conn.cursor()'= 마우스의 커서와 비슷하다. = 무언가를 가르킨다. 주로 테이블을 가르킨다. 
cur = conn.cursor()

# execute = cursor를 실행한다. / SELECT * FROM emp = enp에서 모든 정보를 선택해줘. / for문 계속 돈다. = 다 셀때까지 돈다.
try:
    for row in cur.execute('SELECT * FROM emp'): # 모든 데이터를 가져오는 쿼리.
        print(row) # 한 줄씩 출력해줘. 커서가 한 줄씩 내려간다. 
    # cur.execute('SELECT COUNT(*), \'SELECT\' FROM emp') #cur.execute('SELECT COUNT(*) FROM emp') / COUNT(): 간단하게 데이터의 수가 맞는지 확인할 때 사용하는 함수.
    # result = cur.fetchone() # fetchone(): 하나의 줄을 출력해준다. 하나의 값을 출력해 준다. 
    # print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 17번 라인 확인요. : {e}')

finally:
    cur.close() # 커서부터 닫고
    conn.close() # 접속을 닫아야한다. (python에서는 가능하지만 다른 프로그래밍적으로 필수적이다.)

# >>> tuple(튜플)로 결과가 나온다. / 튜플은 수정, 삭제, 추가 불가능. 



