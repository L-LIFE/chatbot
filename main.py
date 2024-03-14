# 정수 계산
10+5
(10-5)*2
10/2

#실수 계산
2.2*5
1.0/0.2
3/2

# /, //, %
3/2
3//2
5/2
5//2
5%2

#거듭제곱
2**5
2**10

#변수 사용
a=10 # 변수명은 숫자로 시작과 특수 기호, 시스템 키워드도 사용할 수 없다.
b=20
a*b

#문자열 사용
'1234'
'hello'
'fffff'

#문자열 변수 사용
a='e'
a

#큰 따옴표 출력
a='"Remember"'
a

#작은따옴표 출력
a="I'm"
a

#줄바꿈
a="Hello\nMMM"
print(a)
a #print문 없이 출력하게 되면 'Hello\nMMM'이와 같이 출력이 된다.

#\n는 간단한 문장일 때만 자주 사용한다. 복잡한 문장이거나 긴 문장의 경우에는 작은따옴표나 큰따옴표 3개를 연속적으로 사용한다.

# a= '''Hello
# MMMM'''
#이 부분 오류 발생=> MMMM''' 왜 이런식으로 뒤에 끝나지 않는 문자가 출력이 되는 건가?
print(a)

#이스케이프 코드 !!
# \n 줄바꿈
# \t 탭
# \\ 문자 \출력
# \' 문자 '출력
# \" 문자 "출력

#리스트
numbers=[1,2,3,4,5]
numbers

#리스트 삽입
numbers.insert(1, 1.5) #리스트 1번 요소에 1.5 넣기
numbers

#리스트 삭제
numbers.pop() #맨 마지막 요소를 꺼내고 삭제
numbers

#리스트 2번째 요소를 꺼내고 삭제
numbers.pop(2)
numbers

#리스트 3번째 요소를 꺼내고 변수에 저장
a=numbers.pop(3)
numbers
a #꺼낸 변수가 저장되어 어떤 숫자가 삭제되어 있는 지를 변수를 저장할 수 있음

#pop 함수 대신 del함수로 이용한 삭제
numbers =[1,2,3,4,5]
del numbers[2] #리스트 2번째 요소 삭제
numbers
#여기서 중요한 점은 리스트 요소의 순서는 0부터 시작한다는 점을 주의해야 한다.
#3번째 요소이면 리스트는 0부터 시작하기에 리스트 4번째 자리의 숫자가 없어진다는 것이다.

#리스트 요소의 개수
numbers=[1,2,3,4,5]
len(numbers)

#튜플
numbers=(1,2,3,4,5)
numbers

#다양한 자료형의 튜플
numbers=(1,2,3,4,'six')
numbers

#튜플의 타입 확인
type(numbers)
#리스트와 유사하지만, 튜플은 요소를 변경하지 못한다는 점만 제외하면 리스트와 동일하다. =>
#튜플의 불변성을 제외하곤 리스트와 동일하다.

#인덱싱, 슬라이싱
numbers=(1,2,3,4,5)
numbers[1] #2
numbers[-1] #5, 음수는 뒤에서부터 순서가 시작된다.
numbers[2:] #2번째 요소부터 슬라이싱, 새로운 튜플로 반환한다
numbers[-2:] #뒤에서 2번째 요소부터 슬라이싱
numbers[1:-2] #1번째 요소에서 뒤에서 2번째 요소 앞까지 슬라이싱

#튜플 요소 수정
numbers=(1,2,3,4,5)
numbers[0]=8 #오류 발생
#튜플은 요소를 변경할 수 없다고
# " TypeError: 'tuple' object does not support item assignment " 이와 같은 문장이 출력이 된다.

#튜플 덧셈 연산 => 튜플끼리 더하게 되면 숫자가 더해지는 것이 아니라, 숫자 순서 연결이 된다.
numbers=(1,2,3,4,5)
numbers1=numbers+(9,9)
numbers1

#튜플 덧셈 연산 주의할 점
numbers=(1,2,3,4,5)
numbers1= numbers+(1) #오류
# "TypeError: can only concatenate tuple (not "int") to tuple" 이와 같이 문장 출력.
# 튜플과 덧셈 연산할 때 1개의 요소만 있어도 우리는 튜플임을 알지만, 파이썬 인터프리터에서는 구별할 수가 없어 튜플임을 표현해야 함

#1개의 요소를 덧셈 연산으로 표현할 때 => 쉼표를 통해 튜플 요소임을 알려준다.
numbers1= numbers+(1, )
numbers1

#딕셔너리 => 리스트, 튜플과 다르게 순차적으로 데이터를 검색하지 않고 key-value를 한 쌍으로 가지는 해시형태.
#해시: 단방향 암호화 기법으로 해시함수를 이용하여 고정된 길이의 비트열로 변경/
#즉, 단방향 암호화 기법은 암호화는 수행하지만, 복호화는 불가능한 알고리즘.

#그러나 순차적으로 데이터 검색을 하지 않지만, key를 이용하여 순차적으로 검색할 수 있음.
#key는 숫자와 문자열만 사용가능. 각각의 쌍은 쉼표로 구분.

user={'name':'홍길동', 'age':40, 'email': 'honghong@email.com'}
user
type(user)

#딕셔너리의 key가 문자열이면서 value값이 여러 개인 경우
dict1= {'key':[100, 'hi', 4.5]}
dict1['key']
#딕셔너리의 요소 출력
dict1['key'][1]

#딕셔너리의 key가 숫자인 경우
dict2={10:'ten'}
dict2[10]

#딕셔너리 데이터 쌍 추가
dict1={}
dict1['a']='A'
dict1['b']='B'
dict1

dict1[3]=[1,2,3] #주의할 점: 딕셔너리이므로 요소 3번째가 아닌 key임을 인지하고 있어야 한다.
dict1

dict1[4]={'name':'kei', 'age':35} #이 부분이 의문, 2개의 value를 저장할 수 있는 건가?
dict1

#딕셔너리 삭제
#하나의 키만 삭제하는 경우
del dict1['a']

#모든 데이터를 삭제하는 경우
dict1.clear()
dict1

#불리언=> 파이썬에서는 True, False를 사용해야 지 true와 false처럼 첫단어의 시작을 소문자로 적으면 오류 발생.
a=True #이때는 True가 문자형이지만, 파이썬에서 정해져 있는 파이썬 키워드라서 큰&작은따옴표를 사용하여 적지 않아도 됨.
a
type(a)

#if 조건문 => 주의할 점: 들여쓰기를 제대로 안하면 오류 발생. + 다른 언어와 다르게 꼭 쌍점이 필요하다.
check=True
if check: #check가 참이라면 실행할 문장을 if문을 통해 설정한 것.
    print('-'*13) #파이썬에서는 곱셈 연산을 통해 동일한 문장을 여러번 출력할 수 있다.
    print('check id true')
    print('-'*13)

#if문의 변수 검사
check=False
if check==False:
    print('-' * 13)
    print('check id false')
    print('-' * 13)

#조건문과 다르다면 출력할 문장
if check!=True:
    print('-' * 13)
    print('check id false')
    print('-' * 13)

#조건문에서 사용하는 연산자
A==B #A와 B가 동일하면 결과는 True
A!=B #A와 B가 동일하지 않으면 결과는 True
A and B #A와 B가 모두 True이면 결과는 True
A or B #A와 B중 하나라도 True이면 결과는 True
A #A가 True이면 결과는 True
not A #A가 True가 아니면 결과는 True
A>B #A가 B보다 크면 결과는 True
A>=B #A가 B보다 크거나 같으면 결과는 True
A<B #A가 B보다 작으면 결과는 True
A<=B #A가 B보다 작거나 같으면 결과는 True

#if문 제어문 사용
age=15
if age>=19:
    print('You are an adult')
else:
    print('You are not an adult')


#if-elif-else
score=84
if score>=90:
    print('Grade A')
elif score>=80:
    print('Grade B')
elif score>=70:
    print('Grade C')
else:
    print('Grade D')

#구간 별로 조건문 생성
dist=300
if dist>0 and dist<=50: #거리가 0~50일 때 실행
    print('1000won')
elif dist>50 and dist<=100: #거리가 51~100일 떄 실행
    print('2000won')
else: #거리가 101이상일 때
    print('Over 3000won')

#while문 : True인 동안 계속 코드를 실행한다.
#만약 False가 없다면 계속 실행되기 때문에 무한 루프가 돌게 된다. 만약 무한 루프 도는 경우 파이썬은 ctrl+c를 눌러 멈출 수 있다.
i=1
while i<=10:
    print('i=%d'%i) #%d가 i의 값으로 치환되어 반환
    i=i+1

#이때 문자열 출력 시 숫자 데이터로 치환하는 과정을 함. 이는 문자열 포매팅 기능이라고 한다.
#문자열 포매터는 변수의 자료형에 맞는 변수 내용을 표현할 수 있는 형식자를 의미함.
#종료
%d #10진수 출력
%x #16진수 출력
%o #8진수 출력
%f #실수 출력
%s #문자열 출력

#사용자의 입력을 받는 무한루프 코드
while True:
    print('input number: ')
    menu=int(input()) #input()은 사용자에게 입력을 받는다는 의미. int(input())이면 int형을 입력 받는 다는 것.
    if menu==0: break
    elif menu==1: print('number one')
    elif menu==99:
        continue
    elif menu==2:
        print('number two')
    else:
        print('another number')

#조건을 이용하여 반복적으로 작업을 하면 while문을 수행하고, 요소를 하나씩 꺼내서 사용할 때는 for 반복문을 사용한다.
#for문을 사용한 리스트 출력
numbers=[1,2,3,4]
for i in numbers:
    print(i)

#for문과 range()함수
numbers=range(1,6) #1부터 5까지의 숫자가 저장이 된다.
for n in numbers:
    print(n)

#여러 개의 변수에 자동으로 대입되는 for문
coord=[(0,0),(10,15),(20,25)] #x,y를 저장하는 리스트를 출력하는 예제, 루프를 돌 때마다 각 요소가 자동으로 변수 x,y에 대입된다.
for x,y in coord:
    print(x,y)

#user딕셔너리의 key만 모아서 dict_keys 객체로 반환하는 예쩨
user={'name':'Kei', 'age':35, 'nationally':'Korea'}
user.keys() #dict_keys(['name', 'age', 'nationally']) 결과 값

#딕셔너리의 key리스트 출력
for k in user.keys():
    print(k) #어떤 key의 이름을 가지고 있는 지 궁금하면 이 방식을 활용하여 알 수 있음.

#values()함수로 key의 값을 알아내기
user={'name':'Kei', 'age':35, 'nationally':'Korea'}
user.values()
#for문으로 value값을 출력
for k in user.values():
    print(k)

#딕셔너리의 items()함수로 key, value 내용을 모두 출력하기
user={'name':'Kei', 'age':35, 'nationally':'Korea'}
user.items()
#반복문으로 출력
for k,v in user.items():
    print(k,v) #key와 value값을 나타내기 위해 두가지 값이 출력할 수 있게 구성해줘야 한다.
