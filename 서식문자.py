'''문자열 포매팅이란? 문자열을 만들때 원하는 위치에 특정한 값(변수)를 삽입해서 문자열을 그때그때 이쁘게 출력하는 것을 의미'''
# ex) print('%s 왔나요?') % name[i]
''' 정수 출력 시 : %d   
    문자열 : %s
    실수 : %f
    8진수 : %o
    16진수 : %x
    문자 % 출력 : %%
'''

'''num = 50
s = 'my age %d' % num
print(s)'''

# 문자열, 정수,실수를 %로 포매팅 해보기
'''
# % 기호 문자 출력
names = ['kim', 'park', 'lee']
for name in names:  # 요소가 names에는 3개 있으므로 세바퀴를 돎.
    print('my name is %s' % name)

# % 기호 정수 출력
money = 10000
s2 = 'give me %d won' % money
print(s2)

# % 기호 실수 출력
d = 3.141592
print('value %f' % d)
'''

# 포매팅 해야할 변수 값이 두 개 이상일 때는
'''
# 출력해야할 값이 두개 이상인 경우 ()를 이용합니다
s1 = 'my money is %s, age : %d' % ('mirim', 100)
print(s1)

# 출력해야할 값이 점점 많아 질수록 - 출력이 많을때는 ()를 넣어 순서대로 대입해준다
age = 78
money = 200000
name = 'Jang'
weight = 63.12
etc = 'abcde'
s2 = 'my name is %s, age : %d, wight : %f, money : %d, etc : %s' % (
    name, age, weight, money, etc)
print(s2)
'''

# %는 타입을 정해주기 때문에 정확해 보이지만, 타입을 정해야 하기 때문에 불편한 점도 존재
# 이를 개선하기 위해 str.format 형식 등장. 그 이후에 f-string 방법 등장

# f-string
# string formating - 문자열 포매팅(문자열에서 특정 부분반 바꾸고 나머지 부분은 일정하다고 할 때, 문자열 포매팅을 이요해서 보기 좋게 출력)
'''
month = 1
while month <= 12:
    print(f'2022년 {month}월')
    month = month + 1
    '''
# 변해야 하는 값이 있는 위치를 포매팅 할 위치로 잡아서 설정

# f-string이란?
''' f-string 모매팅은 파이썬 버전 3.6이상부터 사용 가능
    f-string의 모양은 f와 {}만 알면 됨
    문자열 맨 앞에 f를 붙여주고, 중괄호 안에 직접 변수 이름이나 출력하고 싶은 것을 바로 넣으면 됨.
    == f'문자열 {변수} 문자열'

    ex) 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다.
    s = 'coffee'
    n = 5
    result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
    paint(result)
'''

# f-string과 왼쪽 정렬, 오른족 정렬, 가운데 정렬
'''
# f-srting 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)

# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)

# f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

# f-string 중괄호 출력
num = 10
# 중괄호 세개와 두개의 차이점을 알기. 중괄호 두개는 중괄호를 보여주는 처리. 변수처리를 하려면 {}를 하나 더 써주기.
result = f'my age {{{num}}}, {{num}}'
print(result)
'''

# f-string와 딕셔너리
''' 
d = {'name':'Mirim', 'gender':'female', 'age':18}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)
'''
'''
d = {'name': 'Mirim', 'gender': 'female', 'age': 18}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)
'''

# f-string과 리스트
n = [100, 200, 300]

print(f'list : {n[0]}, {n[1]}, {n[2]}')

for v in n:
    print(f'list with for : {v}')
