# bookrentalshop.py
# divtbl, membertbl

from __future__ import division
import email
import cx_Oracle as ora

def myconn(): # DB가 하나이므로 매개변수를 지정해주지 않아도 된다.
    dsn = ora.makedsn('localhost', 1521, service_name= 'orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding= 'utf-8')
    return conn

# divtbl에서 모든 정보 가져오기
def getAllDataFromDivtbl(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query):
        print(row)

# divtbl에서 정보 입력하기
def setDataIntoDivtbl(conn, tup):
    cur = conn.cursor()
    query = '''INSERT INTO divtbl (division, names) 
                VALUES (:1, :2)''' # divtbl에 새로운 데이터 입력한다는 쿼리문.
    cur.execute(query, tup) # 실행
    cur.close() # 커서를 종료한다. 없어도 잘 된다. 아마 python이라서 가능한듯. 다른 프로그래밍에서는 꼭 필요할 경우도 있다.
    conn.commit() # COMMIT; = DB에서 커밋과 같은 쿼리. / 이 쿼리가 없으면 실행은 되다 커밋(저장)이 되지 않는다.

# membertbl에서 일부 정보 가져오기
def getSomeDataFromMembertbl(conn):
    cur = conn.cursor()
    query = '''SELECT names, levels, addr, mobile, email 
                FROM membertbl
                WHERE addr LIKE '서울%'
                AND UPPER(email) LIKE '%@NAVER.COM'
                ORDER BY idx DESC'''
    for row in cur.execute(query):
        print(row)
    cur.close()

# membertbl에서 신규회원 입력하기
def setNewMemberIntoMembertbl(conn, tup):
    # idx를 찾기위해서 
    cur = conn.cursor()
    query = '''SELECT ROWNUM, idx
                FROM (
                    SELECT idx FROM membertbl
                    ORDER BY idx DESC  
                        ) 
                WHERE ROWNUM = 1'''
    cur.execute(query)
    idx = cur.fetchone()[1] # Data가 없을 때 [1]인덱스가 1인 것을 읽어달라고 하면 None Error가 발생한다. 예외가 발생하기 때문에 아래의 if 문을 추가해서 작성해야 한다.
    if idx is None:
        idx = 0
    else:
        idx = idx[1]

    # 입력값을 만들어줌
    intup = (idx + 1, tup[0], tup[1], tup[2], tup[3])
    
    query = '''INSERT INTO membertbl 
                       (idx, names, levels, userid, password) 
                VALUES (:1, :2, :3, :4, :5)'''
    cur.execute(query,intup)
    # cur.close()
    conn.commit()

# membertbl에서 데이터 수정하기
def setChangeMemberFromMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''UPDATE membertbl
                SET addr = :1
                    , mobile = :2
                    , email = :3
                WHERE idx = :4''' 
    cur.execute(query, tup)
    cur.close()
    conn.commit()

# division에서 데이터 삭제 # 다른 테이블에서 사용하고 있는 데이터는 삭제가 불가능.
def delectDivision(conn, division):
    cur = conn.cursor()
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur.execute(query, (division,)) # 데이터가 하나면 튜플로 만들어 주면서 ,(쉼표)를 반드시 추가해야한다! / tuple은 하나짜리라도 (division, )으로 만들어줘야한다. 이거는 문법이다. 
    conn.commit()

if __name__ == '__main__':
    print('책대여점 프로그램 시작')
    scott_con = myconn() # DB 접속
    # # 1. divtbl에서 데이터 조회
    # print('책 장르 정보조회')
    # getAllDataFromDivtbl(scott_con)

    # # 2. divtbl에 새로운 데이터 입력
    # print('책 장르 정보입력')
    # division = input('구분코드 입력 :')
    # names = input('장르명 입력 :')
    # tup = (division, names)
    # setDataIntoDivtbl(scott_con, tup)
    # print('정보 입력 성공')
    
    # # 3. membertbl에서 데이터 조회
    # getSomeDataFromMembertbl(scott_con)

    # # 4. membertbl에 새 데이터 입력
    # print('신규회원 등록')
    # names = input('이름 입력 :')
    # levels = input('레벨 입력 (A ~ D) :')
    # userid = input('아이디어 입력 (최대 20자) :')
    # password = input('패스워드 입력(최대 20자) :')
    # tup = (names, levels, userid, password)
    # setNewMemberIntoMembertbl(scott_con, tup)
    # print('신규회원 저장 성공')
    
    # # 5. membertbl에 새 데이터 수정
    # print('기존회원 수정')
    # idx = input('변경회원 번호 :')
    # addr = input('주소 입력 :')
    # mobile = input('폰번호 입력(-포함) :')
    # email = input('이메일 입력: ')
    # tup = (addr, mobile, email, idx)
    # setChangeMemberFromMembertbl(scott_con, tup)
    # print('기존회원 수정 완료')

    # 6. divtbl에 임의 데이터 삭제
    print('책장르 정보 삭제')
    division = input('삭제할 정보코드 입력 :')
    delectDivision(scott_con, division)
    print('삭제 성공')
