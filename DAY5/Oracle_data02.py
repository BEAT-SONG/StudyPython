# 커서에 접근하는 코드를 함수로 작성
# 변수를 지정할 때 영어이든 한글이든 상관이 없다.
# ()(괄호)가 뒤에 있는거는 함수이다. 함수는 정해진 것으로 마음대로 바꾸면 안되고 그대로 사용해야한다. But, 함수도 어떠한 과정을 거쳐서 한글로 변환할 수 있다. 

import cx_Oracle as ora

# 함수 선언은 메인함수(프로그램 시작 함수) 위에 작성한다. / 아무리 함수 선언이 많아도 프로그램의 시작은 메인함수이다. / 함수 선언은 선언만 되어있는 것이고 실행이 되는 것은 아니다. 
def myconn(): # 오라클 접속 함수.
    dsn = ora.makedsn('localhost', 1521, service_name= 'orcl') # 오라클 접속(conn)할 때 사용하는 매개변수(dns) / 오라클에 접속하기 위한 매개변수.
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding= 'utf-8') # 색이 약하면 쓰이지 않았다는 것을 의미. 
    return conn # conn을 다시 돌려달라! 라는 것이 myconn()함수 이다.

def getAlldata(conn): # conn객체(connect객체/ 연결객체)를 매개변수로 받아서 쿼리를 실행할 함수.
    cur = conn.cursor() # 커서를 conn에 생성.
    query = 'SELECT * FROM emp' # 'emp 테이블에서 모든 데이터를 가져와라'를 의미하는 변수 생성.
    for row in cur.execute(query): # 'emp 테이블의 최상단에 커서가 위치라하면서 모든 데이터를'
        print(row) # '한줄씩 출력'

# 하나의 결과를 다양한 함수로 표현할 수 있다. 
def getNameAndJobData(conn):
    cur = conn.cursor() # 커서를 conn에 생성.
    query = 'SELECT ename, job FROM emp' # emp 테이블에서 ename, job을 가져오겠다. 
    # for row in cur.execute(query):
    #     print(row)
    cur.execute(query) # 실행
    while True: # 무한 반복인데 if문을 추가하여 빠져나올 수 있게 만들어야 한다. 
        row = cur.fetchone() # 한 row(레코드) 읽기
        if row is None: # 만약에 row(레코드)를 읽었으때 데이터가 아무것도 없다면 = None이라면
            break # 무한 루프에서 빠져 나오겠다.
        else:
            print(row)

# def getDeptName(conn, no): # 여기서 no은 숫자 하나가 아니라 tuple이다. 
#     cur = conn. cursor()
#     query = 'SELECT * FROM dept WHERE deptno = :1' # 오라클에서는 1번 부터 시작된다. / 값을 받아서 전환할 때 사용하는 문법 ':1'이다. / ':1'은 '매개변수'이다. 이것은 no의 값을 받는 값이 변동적인 '매개변수'이다.
#     cur.execute(query, no) # no에 값이 들어가면 위의 함수에 값이 들어가진다. / 커서의 파라미터를 통해 값을 ':1"에 값을 넣는다.

# def getDeptName(conn, no): 
#     cur = conn. cursor() # 커서를 conn에 생성.
#     query = f'SELECT * FROM dept WHERE deptno = {no}' # dept 테이블에서 deptno = {no}인 값을 가져오겠다. / deptno = {no} 아래 56번 'print(f'{no}이 번호의 부서명')'이 나올때 알고 싶은 번호를 입력해서 아래의 쿼리를 실행한다.
#     cur.execute(query) # 한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 
#     row = cur.fetchone() # 한줄씩 읽어라!
#     print(row)

# def getDeptName(conn, no, loc): # loc는 글자이다. / 파라미터수 = 검색할 정보의 수 + 1(conn) 
#     cur = conn. cursor() # 커서를 conn에 생성.
#     query = f"SELECT * FROM dept WHERE deptno = {no} AND loc = '{loc}'"  # loc가 글자이므로(문자열이므로) 쿼리를 ""로 표현하여 사용하는 경우가 있다. 또는 \(역슬래시)['\'\]를 사용할 수도 있다.
#     cur.execute(query) # 한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 
#     row = cur.fetchone() # 한줄씩 읽어라!
#     print(row)

# def getDeptName(conn, tup): # tup 변수는 tuple이므로 원하는 정보의 수가 아무리 늘어나도 변수 하나로 표현할 수 있다. 
#     cur = conn. cursor() # 커서를 conn에 생성.
#     query = f"SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = '{tup[1]}'"  # tuple인 변수 tup를 이용하여 원하는 자리[인덱스]의 값으로 표현할 수 있다. # loc가 글자이므로(문자열이므로) 쿼리를 ""로 표현하여 사용하는 경우가 있다. 또는 \(역슬래시)['\'\]를 사용할 수도 있다.
#     cur.execute(query) # 한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 
#     row = cur.fetchone() # 한줄씩 읽어라!
#     print(row)

def getDeptName(conn, tup): # tup 변수는 tuple이므로 원하는 정보의 수가 아무리 늘어나도 변수 하나로 표현할 수 있다. / tuple은 여러 Data의 집합이라고 할 수 있으므로 그 자체를 '.upper()'를 할 수 없다.
    cur = conn. cursor() # 커서를 conn에 생성.
    query = "SELECT * FROM dept WHERE deptno = :1 AND loc = :2" # Oracle(DB)에서는 1부터 시작해서 0이 아닌 1을 사용한다. 
    # query = "SELECT * FROM dept WHERE deptno = :0 AND loc = :1" # 0도 가능하긴 하지만 여기서만 가능한거지 굳이 사용하지 않기!
    cur.execute(query, tup) # 한줄씩 읽기 위해 execute를 이용해서 실행시킨다. 이때 tuple인 변수 tup을 추가하여 실행하면 위의 Data의 type을 확인하지 않아도 (숫자인지 문자열인지) 쿼리가 실행할 수 있게 해준다.
    row = cur.fetchone() # 한줄씩 읽어라!
    print(row)

if __name__ == '__main__': # 언더바 2개씩 = 시스템 변수 # __name__ = '__main__' 이면 프로그램을 시작하겠다 라는 의미. = 시작 포인트를 지정해주는 쿼리(코드) / 시작 지점이라는 약속이라고 생각하면 편하다. / '메인함수'
    print('프로그램 시작')
    # 함수호출
    scott_con = myconn() # dsn, connect() 후 접속개체 conn을 return. / 오라클 접속 함수(myconn()=conn)가 scott_con 변수로 호출되었다.
    
    # print('emp 테이블 전체 조회(SELECT *)')
    # getAlldata(scott_con)
    # print('emp 테이블에서 2개 칼럼 조회')
    # getNameAndJobData(scott_con)
    
    # no = input('1. 검색할 부서번호를 입력하세요. :')
    # loc = input('2. 지역명을 입력하세요. :').upper()
    # print(f'부서번호 :{no}, 지역 :{loc}') # print는 우리 눈으로 확인하기 위해서 출력하는 것이지 쿼리에서 중요한 것은 아니다. 
    # getDeptName(scott_con, no, loc) 
    # scott_con = 오라클에 접속한다.
    # 62번의 no 값이 65번의 함수의 값으로 들어가고 63번의 loc 값이 65번의 함수의 값으로 들어간다. 그 뒤에 함수를 정의한 45번으로 가서 함수를 실행해서 쿼리를 실행한다. 
    # loc.upper() = 함수이다. 입력하는 값을 대문자로 취급하여 읽는다. / 함수를 통해 프로그램을 실행할 때 대소문자 구분없이 대문자로 취급해서 읽는다. 
    
    no = input('1. 검색할 부서번호를 입력하세요. :')
    loc = input('2. 지역명을 입력하세요. :').upper()
    tup = (no, loc) 
    # print(f'부서번호 :{no}, 지역 :{loc}') # print는 우리 눈으로 확인하기 위해서 출력하는 것이지 쿼리에서 중요한 것은 아니다. 
    getDeptName(scott_con, tup) 

    print('프로그램 종료')



