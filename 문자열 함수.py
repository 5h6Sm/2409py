'''h = "  Happy Programming! "
print(len(h))       # 21
print(h.count("p")) # 2  
print(h.upper())    #  HAPPY PROGRAMMING!
print(h.lower())    #  happy programming!
print(h.strip())    #Happy Programming!
print(h.replace("Happy", "Funny"))  #  Funny Programming!
print(h.find("app")) # 3
print(h.rfind("app")) # a를 찾는데 오른쪽부터 찾아서 Programming의 a를 찾는다. 인덱스값은 왼쪽부터 세고, 결과는 13이다
print(h.find("zoo"))    #찾지 못하면 -1 리턴'''

'''h = "  Happy Programming! "
print("a" in h)         #True : h 문자열에 'a'가 있는지 확인
print("amp" in h)       #False :h 문자열에 'amp'가 있는지 확인

x = "01::23::ab::&&"
y = x.split("::")

print(y)            #['01', '23', 'ab', '&&']
print(", ".join(y)) #01, 23, ab, &&'''

'''s = "name:{}, number : {}, soccer : {}"
print(s.format("Ronaldo", 7, True))
print("name : {name}, number : {num}".format(name = "Jordan", num = 23))

print("{:d}".format(515))
print("{:5d}".format(515))
print("{:+5d}".format(515))
print("{:=+5d}".format(515))
print("{:05d}".format(515))
print("{:+05d}".format(515))

print("{:f}".format(11.17))
print("{:23f}".format(11.17))
print("{:12.1f}".format(11.17))

print("{:=+6.1f}".format(11.17))'''

# . format 함수
# 형식 : '{인덱스0}, {인덱스1}',format(값0, 값1)
'''a = 2
b = 3
s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)
print(s)

#직접 대입하기
s1 = 'name:{0}'.format('BlockDMask')
print(s1)

#변수로 대입 하기
age = 55
s2 = 'age : {0}'.format(age)
print(s2)

#이름으로 대입하기
s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='남')
print(s3)

#인덱스를 입력하지 않으면?
s4 = 'name : {}, city : {}'.format('BlockDMask', 'seoul')
print(s4) #인덱스를 입력하지 않으면 format 인자 순서대로 들어간다.

#인덱스 순서가 바뀌면?
s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
print(s5) #인덱스 순서가 바뀌어도 인덱스 번호가 있기 때문에 번호에 맞는 인자 값들이 들어가게 된다.

#인덱스를 중복해서 입력하면?
s6 = 'test : {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')
print(s6) #인덱스를 중복해서 입력하면 해당하는 인자 값이 또 들어간다. 중복해도 OK.

#중괄호 출력
s7 = 'Format example. {{}}, {}'.format('test')
print(s7) #중괄호를 두 번 겹치면 원래의 중괄호 문자가 나오게 된다.

#중괄호로 겹쳐진 인자값
s8 = 'This is value {{{0}}}'.format(1212)
print(s8) #출력할 값을 중괄호로 겹쳐서 출력하려 하면 이렇게 중괄호를 세 개로 겹치면 된다.

#문자열 정렬하기

#왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} | '.format('left', 'a')
print(s9)

#오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} | '.format('right', 'b')
print(s10)

#가운데 정렬
s11 = 'thgis is {0:^10} | done {1:^5} | '.format('center', 'c')
print(s11)

#문자열에 공백이 아닌 값 채우기

#왼쪽 정렬
s12 = 'this is {0:-<10} | done {1:o<5} | '.format('left', 'a')
print(s12)

#오른쪽 정렬
s13 = 'this is {0:+>10} | done {1:0>5} | '.format('right', 'b')
print(s13)

#가운데 정렬
s14 = 'this is {0:.^10} | done {1:@^5} | '.format('center', 'c')
print(s14)

#자리수와 소수점 표현하기

#정수 N자리
s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(s15) #정수의 자리수를 표현할 때는 '0Nd' 로 표현. N에 원하는 자릿수를 입력. 자릿수가 부족한 경우는 자동으로 0으로 채워짐

#소수점 N자리
s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1254567, 3.14)
print(s16) #실수의 자리수를 표현할 때는 '0.Nf' 로 표현 '''

a = 2
b = 1
s = '구구단 {0} x {1} = {2}'.format(a, b, a*b)
print(s)
