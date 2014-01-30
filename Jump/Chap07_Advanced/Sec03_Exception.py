# -*- coding:utf-8 -*-
"""
3) 예외처리

	except [발생에러 [as 에러메시지변수]]:

첫 번째
	
	try:
	    ...
	except:
	    ...
	
두 번째
	
	try:
	    ...
	except 발생에러:
	    ...
	
세 번째
	
	try:
	    ...
	except 발생에러 as 에러메시지변수:
	    ...

세 번째 방법의 예를 잠시 들어 보면 다음과 같다.
"""
try: 
	4 / 0 
except ZeroDivisionError as e: 
	print(e)
"""
>>> try: 
...     f = open("나없는파일.txt", 'r') 
... except IOError: 
...     print "쓰기모드로 파일을 엽니다." 
...     f = open("나없는파일.txt", 'w') 
... 

에러 발생시키기(raise)
좀 이상하긴 하지만 에러를 일부러 발생시켜야 할 경우도 생기게 된다. 파이썬은 raise라는 명령어를 이용하여 에러를 강제로 발생시킨다. 
예를 들어 Bird라는 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하게 만들고 싶은 경우(강제로 그렇게 하고 싶은경우)가 있을 수 있다.
"""
class Bird:
	def fly(self):
		raise NotImplementedError
"""
만약 위 Bird클래스를 상속받는 자식 클래스가 fly라는 함수를 구현하지 않은 상태에서 fly함수가 호출되면 반드시 위 에러가 발생하게 될 것이다.

Bird클래스의 fly함수를 구현한 자식클래스를 보자.
"""
class Eagle(Bird):
	def fly(self):
		return "very fast"