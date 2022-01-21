# Person.py
# Person Class
# 우선 무엇을 넣어야 할지 모르겠으면 'pass'를 넣어둬라. 아무것도 안 넣어두면 오류가 나기때문이다.
class Person:
    name = '무명이' # 아직 이름이 없다.
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''

    # 생성자. / '__init__': 초기화 / 필수는 아니다. 이것이 없으면 실행되지 않으므로 python이 스스로 만들어서 실행한다.
    def __init__(self, name, age) -> None: # '__000__': '매직매소드'라고 부른다. / retrun 값이 없다는 것을 의미
        self.name = name
        self.age = age
        print('Person이 생성되었습니다.')

    # 함수는 다 return 값이 있다. / 생략이 가능. return (None)
    def 소개한다(self) -> None: # '-> None':retrun 값이 없다는 것을 정확하게 명시해준 것이다.
        greeting = f'''안녕하세요. 저는 {self.name}입니다. 
        {self.gender}이구요. {self.age} 입니다.'''
        print(greeting)

    def 먹는다(self, food): # self를 넣는 이유는 class안에서 사용하는 함수임을 나타내는 문법.
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다.')


if __name__ == '__main__':
    # p = Person() # p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p)) # id 값

    # p2 = Person() #p2라는 이름의 Person 객체 생성
    # print(type(p2))
    # print(id(p2))
# Class의 객체이기 때문에 아래와 같이 쓴다.
    song = Person('박송은', 24) # (class명(Person)에 ()를 추가하는 것) = __init__(self, name, age)
    # 아래의 쿼리는 변수를 넣기위해 초기화를 하는 과정이라고 생각하면 된다. 
    # 생성자[__init__(self, , )]를 만들게 되면 이 쿼리는 생략이 가능하다. / 보안상의 문제로 이 쿼리처럼 정보가 나타나는 것보다 입력을 하면서 바로 입력될 수 있는 '생성자'를 사용하는 것이 더 선호된다.
    # song.name = '박송은' # 이거는 위에 함수에 포함되어 있으므로 중복된 것이다. 만약 그래로 둔다면 처음에 입력되고 그 뒤에 43, 44번이 입력되어 뒤에 것이 출력되어 나온다.
    # song.age = 100
    song.height = 168
    song.gender = 'female'
    song.feetsize = 250
    song.bloodtype = 'RH+ B'

    song.소개한다()
    song.먹는다('본죽')
    song.일한다('핫식스')
    
    # hgd = Person()
    # hgd.name = '홍길동'
    # hgd.age = 490
    # hgd.height = 150
    # hgd.gender = 'male'
