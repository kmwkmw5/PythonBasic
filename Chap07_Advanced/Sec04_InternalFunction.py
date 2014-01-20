# -*- coding:utf-8 -*-
"""
4) 내장함수
""""""

	abs : 숫자값을 입력값으로 받았을 때, 그 숫자의 절대값을 돌려주는 함수이다.

"""
print(abs(3))
print(abs(-3))
print(abs(1+2j))
print('')
"""

	chr : 정수 형태의 아스키코드값을 입력으로 받아서 그에 해당하는 문자를 출력하는 함수이다.

"""
print(chr(65))
print(chr(97))
print('')
"""

	dir : 객체가 가지고 있는 변수나 함수를 리스트 형태로 보여준다.

"""
print(dir([1,2,3]))
print(dir({'key':'value'}))
import mod2
print(dir(mod2))
from Sec01_Class import *
print(dir(Dog('doggy')))
print('')
"""

	divmod(a,b) : 두 개의 숫자를 입력값으로 받았을 때 그 몫과 나머지를 터플의 형태로 반환하는 함수이다.

"""
print(divmod(7,3))
print(divmod(1.3, 0.2))
print('')
"""

	enumerate : 입력값으로 시퀀스자료형(리스트, 터플, 문자열)을 입력으로 받아 enumerate객체를 리턴한다.
				  (인덱스(숫자), 값)의 형태로 반환.(딕셔너리에서는 인덱스, 키를 리턴하므로 사용의미가 없음)
"""
for i, name in enumerate(['boby', 'foo', 'bar']):
	print(i, name)
print('')
"""

	eval :  입력값으로 실행가능한 문자열을 입력으로 받아서 문자열을 실행한 결과값을 반환하는 함수이다.

"""
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))
print('')
"""

	hex(x) : 입력으로 정수값을 받아서 그 값을 십육진수값(hexadecimal)로 변환하여 돌려주는 함수이다.

"""
print(hex(234))
print(hex(3))
print('')
"""

	id(object) : 객체를 입력값으로 받아서 객체의 고유값(레퍼런스)을 반환하는 함수이다.

"""
# 전부 같은 객체
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print('')
"""

	input([prompt]) : 사용자 입력을 받는 함수이다. 입력 인수로 문자열을 주면 그 문자열은 프롬프트가 된다.
	#python2.7 : 문자열은 raw_input([prompt])
"""
#a = raw_input('string : ')
#print a
"""

	int(x[, y진법]) : 스트링 형태의 숫자나 소수점 숫자 등을 정수의 형태로 반환시켜 돌려준다.
						y진법의 수 x를 10진수의 값으로 돌려준다.

"""
print(int('3'))
print(int(3.4))
print(int('1A', 16))
print('')
"""

	isinstance(object, class) : 입력값으로 인스턴스와 클래스 이름을 받아서 입력으로 받은 인스턴스가
							그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 반환한다.
							
"""
class Person: pass
a = Person()
b = 3
print(isinstance(a, Person))
print(isinstance(b, Person))
print('')
"""

	len(s) : 인수로 시퀀스 자료형(문자열, 리스트, 터플)을 입력받아 그 길이(요소의 개수)를 돌려주는 함수이다.

"""
print(len('python'))
print(len([1,2,3]))
print(len((1,'a')))
print('')
"""

	list(s) : 인수로 시퀀스 자료형을 입력받아 그 요소를 똑같은 순서의 리스트로 만들어 돌려주는 함수이다.
				리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
"""
print(list("python"))
print(list((1,2,3)))

a = [1,2,3]
b = list(a)
print(id(a) == id(b))
print('')
"""

	lambda : 함수를 생성할 때 사용되는 예약어로 def와 동일하나 보통 한줄로 간결하게 만들어 사용할 때 사용한다.
			  lambda 인수1, 인수2, ...  : 인수를 이용한 표현식
"""
sum = lambda a, b: a+b
print(sum(3,4))
print('')
"""
lambda는 def 대신 간결하게 사용할 수 있고 def로 쓸 수 없는 곳에 lambda는 쓰일 수 있다.
리스트 내에 lambda가 들어간 경우를 살펴보자.
"""
l = [lambda a,b:a+b, lambda a,b:a*b]
print(l)
print(l[0](3,4))
print('')
"""
프로그래밍을 하다 보면 lambda 함수의 사용용도는 무궁무진함을 알게 될 것이다.
""""""

	filter(function, list) : 함수와 리스트를 입력으로 받아서 리스트의 값이 하나씩 함수에 인수로 전달될 때,
								 참을 반환시키는 값만을 따로 모아서 리스트의 형태로 반환하는 함수이다.
"""
#positive.py 
def positive_bad(l): 
	result = [] 
	for i in l: 
		if i > 0: 
			result.append(i) 
	return result

print(positive_bad([1,-3,2,0,-5,6]))
"""
filter함수를 이용하면 아래와 같이 위의 내용을 간단하게 쓸 수 있다.
"""
#filter1.py 
def positive(x): 
	return x > 0

print(filter(positive, [1,-3,2,0,-5,6])) # 파이썬3에서는 list()로 변환해서 사용해야함
"""
lambda를 쓰면 더욱 간편하게 쓸 수 있다. (lambda함수는 잠시 후에 설명한다.)
"""
#lambda
print(filter(lambda x: x > 0, [1,-3,2,0,-5,6])) # 파이썬3에서는 list()로 변환해서 사용해야함
print('')
"""

	map(function, list) : 함수와 시퀀스 자료형(리스트, 터플, 문자열)을 입력으로 받아서 시퀀스 자료형의
				각각의 요소가 함수의 입력으로 들어간 다음 나오는 출력값을 묶어서 리스트로 돌려주는 함수이다.

"""
# 리스트를 입력받아서 각각의 요소에 2를 곱한 결과값을 돌려주는 함수
def two_times_bad(l): 
	result = [] 
	for i in l: 
		result.append(i*2) 
	return result

result = two_times_bad([1,2,3,4]) 
print(result)
"""
이것을 다음과 같이 해보자.
"""
def two_times(x): return x*2
print(map(two_times, [1,2,3,4])) # 파이썬3에서는 list()로 변환해서 사용해야함
"""
위의 예는 lambda를 쓰면 다음처럼 간략화된다.
"""
print(map(lambda x: x*2, [1,2,3,4])) # 파이썬3에서는 list()로 변환해서 사용해야함
print('')
"""

	max(s) : 인수로 시퀀스 자료형(문자열, 리스트, 터플)을 입력받아 그 최대값을 돌려주는 함수이다.
	min(s) : max와는 반대로 시퀀스 자료형을 입력받아 그 최소값을 돌려주는 함수이다.

"""
print(max([1,2,3]))
print(max('python'))
print(min([1,2,3]))
print(min('python'))
print('')
"""

	oct(x) : 정수 형태의 숫자를 *8진수 문자열*로 바꾸어 돌려주는 함수이다.
			  python2.7 : 042형태, python3 : 0o42형태

"""
print(oct(34))
print(oct(12345))
print('')
"""

	open(filename, [mode]) : 파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수이다.
			읽기 방법(mode)이 생략되면 기본적으로 읽기 전용 모드('r')로 파일객체를 만들어 돌려준다.

	mode		설명
	  w		쓰기 모드로 파일 열기
	  r		읽기 모드로 파일 열기
	  a		추가 모드로 파일 열기
	  b		바이너리 모드로 파일 열기
	w+, r+, a+ 는 파일을 업데이트할 용도로 사용된다.
	b는 w, r, a와 함께 사용된다.
""""""
f = open("binary_file", "rb") 
fwrite = open("write_mode.txt", 'w') 
fread = open("read_mode.txt", 'r') 
fread2 = open("read_mode.txt")
fappend = open("append_mode.txt", 'a')
""""""

	ord(c) : 문자의 아스키 값을 돌려주는 함수이다.

"""
print(ord('a'))
print(ord('A'))
print('')
"""

	pow(x, y) : x의 y승을 한 결과값을 돌려주는 함수이다.

"""
print(pow(2,4))
print(pow(3,3))
print('')
"""

	range([start,] stop [,step]) : for문과 잘 사용되는 것으로 인수로 정수값을 주어
					그 숫자에 해당되는 범위의 값을 iteratable의 형태로 돌려주는 함수이다.

"""
print(range(5))
print(range(5, 10))
print(range(1, 10, 2))
print(range(0, -10, -1))
print('')
"""

	str(object) : 객체를 출력할 수 있는 문자열 형태로 변환하여 돌려주는 함수이다.
					단 문자열 그 자체로만 돌려주는 함수이다. 위의 repr함수와의 차이점을 살펴보자.

"""
print(str(3))
print(str('hi'))
print(str('hi'.upper()))
print('')
"""

	repr(object) : 객체를 출력할 수 있는 문자열 형태로 변환하여 돌려주는 함수이다.
			이 변환된 값은 주로 eval 함수의 입력으로 쓰인다. str 함수와의 차이점이라면
			str으로 변환된 값은 eval의 입력값이 될 수 없는 경우가 있다는 것이다.

"""
print(repr('hi'.upper()))
print(eval(repr('hi'.upper())))
#print(eval(str('hi'.upper()))) # error
print('')
"""

	sorted : 입력으로 받은 시퀀스 자료형을 소트한 후 그 결과를 리스트로 리턴하는 함수이다.

"""
print(sorted([3,1,2]))
print(sorted(['a','c','b']))
print(sorted('zero'))
print(sorted((3,2,1)))
print('')

a = [3,1,2]
result = a.sort()
print(result)
print(a)
print('')
# sort 메소드는 이미 할당된 리스트를 재배열하는 것이고
# sorted 함수는 재배열된 새로운 리스트를 반환한다.
"""

	tuple(sequence) :  인수로 시퀀스 자료형을 입력받아 터플 형태의 자료로 바꾸어 돌려준다.
						  터플형이 입력으로 들어오면 그대로 돌려준다.

"""
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))
print('')
"""

	type(object) : 인수로 객체를 입력받아 그 객체의 자료형이 무엇인지 알려주는 함수이다.

"""
print(type("abc"))
print(type([]))
print(type(()))
print(type(open("main.py", 'r')))
print('')
"""

	zip : 동일한 갯수의 요소값을 갖는 시퀀스 자료형을 묶어주는 역할을 한다.

"""
print(zip([1,2,3], [4,5,6]))
print(zip([1,2,3], [4,5,6], [7,8,9]))
print(zip("abc", "def"))