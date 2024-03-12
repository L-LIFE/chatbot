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