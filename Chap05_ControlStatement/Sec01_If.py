"""
1) if문

	if문의 기본 구조

if <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
else:
    <수행할 문장A>
    <수행할 문장B>
    ...
	    
[참고] ':'을 잊지 말자
	
	조건문이란 무엇인가?

if <조건문>에서 사용되는 조건문이란 참과 거짓을 판단하는 문장을 말한다.
자료형의 참과 거짓에 대해서는 이미 알아 보았지만 몇가지만 다시 알아보면 다음과 같은 것들이 있다.

	자료형의 참과 거짓

자료형	참			거짓
숫자		3			0
문자열	"abc"		""
리스트	[1,2,3]		[]
터플		(1,2,3)		()
딕셔너리	{"a":"b"}	{}


		and, or, not

		연산자		설명
		x or y		x와 y 둘중에 하나만 참이면 참이다
		x and y	x와 y 모두 참이어야 참이다
		not x		x가 거짓이면 참이다
	
	>>> money = 2000
	>>> watch = 1
	>>> if money >= 3000 or watch:
	...     print("택시를 타고 가라")
	... else:
	...     print("걸어가라")
	...
	택시를 타고 가라
	>>>
	
	money는 2000이지만 watch가 1이기 때문에 money >= 3000 or watch
	라는 조건문이 참이 되기 때문에 if문 다음의 문장이 수행된다.

"""
money = 2000
watch = True
if money >= 3000 or watch:
	print("택시를 타고 가라")
else:
	print("걸어가라")
print()

if not watch:
	print("시계가 없네")
else:
	print("시계가 있네")
print()
"""

		in, not in

	더 나아가서 파이썬에서는 조금 더 재미있는 조건문들을 제공한다. 바로 다음과 같은 것들이다.
	
		in				not in
		x in 리스트		x not in 리스트
		x in 터플		x not in 터플
		x in 문자열		x not in 문자열
	
	'in' 이라는 영어단어가 '~안에'라는 뜻을 가졌음을 상기해 보면 다음의 예들이 쉽게 이해가 될 것이다.
	
	>>> 1 in [1, 2, 3]
	True
	>>> 1 not in [1, 2, 3]
	False
	
""""""
	다음은 터플과 문자열의 적용예를 보여준다.
	
	>>> 'a' in ('a', 'b', 'c')
	True
	>>> 'j' not in 'python'
	True
	
	>>> pocket = ['paper', 'handphone', 'money']
	>>> if 'money' in pocket:
	...     print("택시를 타고 가라")
	... else:
	...     print("걸어가라")
	...
	택시를 타고 가라
	>>>

"""
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a','b','c'))
print()
"""

	elif (다중 조건 판단)

if, elif, else의 기본 구조는 다음과 같다.

If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ...

""""""
		pass의 사용

	가끔 조건문을 판단하고 참 거짓에 따라 행동을 정의 할 때
	아무런 일도 하지 않게끔 설정을 하고 싶을 때가 생기게 된다. 다음의 예를 보자.
	
	"지갑에 돈이 있으면 가만히 있고 지갑에 돈이 없으면 시계를 끌러라“
	
	위의 예를 pass를 적용해서 구현해 보자.
	
	>>> pocket = ['paper', 'money', 'handphone']
	>>> if 'money' in pocket:
	...     pass 
	... else:
	...     print("시계를 끌른다")
	...
	
	pocket이라는 리스트 안에 'money'란 문자열이 있기 때문에 if문 다음문장인 pass가 수행되었고
	아무런 결과값도 보여주지 않는 것을 확인 할 수 있다.
"""
pocket = ['paper', 'money', 'handphone']
if 'money' in pocket:
	pass
else:
	print("시계를 끌른다.")
"""

		한줄 짜리 if문
	
	위의 예를 보면 if문 다음의 수행할 문장이 한줄이고 else문 다음에 수행할 문장도 한줄이다.
	이렇게 수행할 문장이 한줄일때 조금 더 간편한 방법이 있다. 위에서 알아본 pass를 사용한 예는 다음처럼 간략화 할 수 있다.
	
	>>> pocket = ['paper', 'money', 'handphone']
	>>> if 'money' in pocket: pass
	... else: print("시계를 끌른다")
	...
	if문 다음의 수행할 문장을 ':'뒤에 바로 적어 주었다. else문 역시 마찬가지이다.
	이렇게 하는 이유는 때때로 이렇게 하는 것이 보기에 편하게 때문이다.
"""
pocket = ['paper', 'money', 'handphone']
if 'money' in pocket: pass
else: print("시계를 끌른다.")