# -*- coding:utf-8 -*-
"""
1) 함수

	파이썬 함수의 구조
	
def 함수명(입력 인수):
    <수행할 문장1>
    <수행할 문장2>
    ...

가장 간단하지만 많은 것을 설명해 주는 다음의 예를 보도록 하자.

def sum(a, b): 
    return a + b

위와 같이 sum함수를 먼저 만들자.

>>> a = 3 
>>> b = 4 
>>> c = sum(a, b) 
>>> print(c)
7
""""""

함수의 입력값과 리턴값

	평범한 함수(입력값, 리턴값이 있는 함수)
"""
def sum(a, b): 
	result = a + b 
	return result

a = sum(3, 4) 
print(a)
"""

	입력값이 없는 함수
"""
def say(): 
	return 'Hi'

a = say() 
print(a)
"""

	리턴값이 없는 함수
"""
def printSum(a, b): 
	print("%d, %d의 합은 %d입니다." % (a, b, a+b))
a = printSum(3, 4)
print(a)
"""
	a의 값이 None이다. 이 None이란 것은 거짓을 나타내는 자료형이라고 언급한 적이 있었다.
	sum함수처럼 돌려주는 값이 없을 때 a = sum(3, 4)처럼 쓰게 되면 함수 sum은 돌려주는 값으로
	a변수에 None을 돌려주게 된다. 그렇다고 이것이 돌려주는 값이 있다는 걸로 생각하면 곤란하다.
""""""

	입력값도 리턴값도 없는 함수
"""
def printSay(): 
	print('Hi')
printSay()
print()
"""

		입력값이 몇 개가 될 지 모를 때는 어떻게 해야 할까?
	
	입력값을 주었을 때 그 입력값들을 모두 더해주는 함수를 생각해 보자.
	하지만 몇 개가 입력으로 들어올지 알 수 없을 때는 어떻게 해야 할지 난감할 것이다.
	이에 파이썬에서는 다음과 같은 것을 제공한다.
	
		def 함수이름(*입력변수): 
		    <수행할 문장>
		    ...
	입력인수 부분이 “*입력변수”로 바뀌었다.
"""
def sum_many(*args): # args: 터플
	sumArgs = 0 
	for i in args: 
		sumArgs = sumArgs + i 
	return sumArgs

result = sum_many(1,2,3) 
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10) 
print(result)
print()
"""
	위에서 만든 sum_many라는 함수는 입력값이 몇 개든지 상관이 없다.
	그 이유는 args라는 변수가 입력값들을 전부 모아서 터플로 만들어 주기 때문이다.
	만약 sum_many(1, 2, 3)처럼 이 함수를 쓴다면 args는 (1, 2, 3)이 되고
	sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)처럼 하면 args는 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이 된다.
	여기서 *args라는 것은 임의로 정한 변수명이다. *pey, *python처럼 아무이름으로 해도 된다.
	단 args라는 것은 입력인수를 뜻하는 영어단어인 arguments라는 영어의 약자로 관례적인 표기법임을 알아두도록 하자.
	
	def sum_many(*args) 처럼 *args만이 입력 인수로 올 수 있는 것은 아니다. 다음의 예를 보도록 하자.
"""
def sum_mul(choice, *args): 
	# sum
	if choice == "sum": 
		result = 0 
		for i in args: 
			result = result + i 
	# mul	
	elif choice == "mul": 
		result = 1 
		for i in args: 
			result = result * i 
	return result 

result = sum_mul('sum', 1,2,3,4,5) 
print(result) 

result = sum_mul('mul', 1,2,3,4,5) 
print(result)
print()
"""
함수의 리턴값은 언제나 하나이다.

먼저 다음의 함수를 만들어 보자.
"""
def sum_and_mul(a,b): 
	return a+b, a*b	# 리턴값이 2개인 것이 아닌 터플!!! 주의!!!

a = sum_and_mul(3,4)
print(a)

s, m = sum_and_mul(3, 4) # 두 개의 변수로도 받을 수 있다.
print("%d %d" % (s,m))
print()
"""
	리턴값은 a+b와 a*b 두 개인데 리턴값을 받아들이는 변수는 a 하나만 쓰였으니 에러가 나지 않을까? 당연한 의문이다.
	하지만 에러는 나지 않는다. 그 이유는 리턴값이 두 개가 아니라 하나라는 데 있다. 함수의 리턴값은 터플값 하나로 돌려주게 된다.
	
	즉 a 변수는 위의 sum_and_mul 함수에 의해서 다음과 같은 값을 가지게 된다.
	
	a = (7, 12)
	즉, 리턴값으로 (7, 12)라는 터플 값을 갖게 되는 것이다. 이것을 두 개의 리턴값처럼 받고 싶다면 다음과 같이 호출하면 될 것이다.
	
	>>> sum, mul = sum_and_mul(3, 4)
	이렇게 호출한다면 이것의 의미는 sum, mul = (7, 12)가 되어서 sum은 7이 되고 mul은 12가 될 것이다.
""""""
또, 다음과 같은 의문이 생길 수도 있다.

>>> def sum_and_mul(a,b): 
...     return a+b 
...     return a*b # 무시
... 
>>>
위와 같이 하면 두 개의 리턴값을 돌려주지 않을까? 하지만 파이썬에서 위와 같은 함수는 참 어리석은 함수이다.

위의 함수는 다음과 완전히 동일하다.

>>> def sum_and_mul(a,b): 
...     return a+b 
... 
>>>
즉, 함수는 return문을 만나는 순간 return값을 돌려준 다음에 함수를 빠져나가게 된다.
""""""

		입력값에 초기치 설정하기
		
	이젠 좀더 다른 함수의 인수 전달 방법에 대해서 알아보자. 인수에 초기치를 미리 설정해 주는 경우를 보자.
"""
def say_myself(name, old, sex=1): 
	print("나의 이름은 %s 입니다." % name) 
	print("나이는 %d살입니다." % old) 
	if sex: 
		print("남자입니다.")
	else: 
		print("여자입니다.")
		
say_myself("김민우", 23)
print()
"""

		함수 입력값 초기치 설정시 주의사항
	
	함수의 초기치를 설정할 때 주의해야 할 것이 하나 있다.
	만약 위의 함수를 다음과 같이 만들면 어떻게 될까?
	
	def say_myself(name, sex=1, old): 
	    print("나의 이름은 %s 입니다." % name) 
	    print("나이는 %d살입니다." % old) 
	    if sex: 
	        print("남자입니다.") 
	    else: 
	        print("여자입니다.")
	위의 함수와 바뀐 부분은 초기치를 설정한 인수의 위치이다. 결론을 미리 말하자면 이것은 실행시에 에러가 난다.
	그냥 얼핏 생각하기에 위의 함수를 호출하려면 다음과 같이 하면 될 것 같다.

	say_myself("박응용", 27)
	하지만 위와 같이 함수를 호출한다면 name변수에는 "박응용“이 들어가겠지만 파이썬 인터프리터는
	sex에 27을 대입해야 할지 old에 27을 대입해야 할지 알 수 없을 것이다.
	
	에러메시지를 보면 다음과 같다.
	
	SyntaxError: non-default argument follows default argument
	위의 에러메시지는 초기 치를 설정해 놓은 입력 인수 뒤에 초기 치를 설정해 놓지 않은 입력 인수는 사용할 수 없다는 말이다.
	즉 입력인수로 (name, old, sex=1)은 되지만 (name, sex=1, old)는 안된다는 것이다.
	결론은 초기화 시키고 싶은 입력 변수들은 항상 뒤쪽에 위치시키라는 것이다.

""""""
	
	함수 내에서 선언된 변수의 효력 범위
"""
a = 1 
def vartest(a): 
	a = a +1 # 2

vartest(a)
print(a) # 1
"""
다음의 예를 보면 더욱 정확하게 이해할 수 있을 것이다.

def vartest(a): 
    a = a + 1

vartest(3) 
print(a)	# error

그렇다면 vartest라는 함수를 이용해서 함수 외부의 a를 1만큼 증가시킬 수 있는 방법은 없을까? 라는 의문이 떠오르게 된다.

두 번째 방법
"""
a = 1 
def globalTest(): 
	global a 
	a = a+1 # 2

globalTest()
print(a) # 2
"""
두 번째 방법은 global이라는 명령어를 이용하는 방법이다.
위의 예에서 보듯이 vartest안의 global a라는 문장은 함수 안에서 함수 밖의 a변수를 직접 사용하겠다는 말이다.
보통 프로그래밍을 할 때 global이라는 것은 쓰지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다.
외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다. 독자는 가급적 이 global을 쓰는 방식을 피해야 할 것이다.
따라서 당연히 두 번째 방법보다는 첫 번째 방법(리턴)이 좋다.
"""