"""
2) 입력과 출력

	사용자 입력
	
어떤 변수에 사용자로부터 입력받은 값을 대입하고 싶을 때는 어떻게 해야 할까?

	input의 사용

>>> a = input() 
Life is too short, you need python 
>>> a 
Life is too short, you need python 
>>>
input은 입력되는 모든 것을 문자열로 취급한다.
"""
a = input()
print(a)
"""

	input(prompt)

사용자로부터 입력을 받을 때 “숫자를 입력하세요.”라던지 “이름을 입력하세요”라는 질문을 포함하고 싶을 것이다.
input 함수를 이용하면 된다. 다음의 예를 따라해 보자.

>>> number = input("숫자를 입력하세요: ") 
숫자를 입력하세요:

"""
num = input("숫자를 입력하세요: ")
print(num)
"""

	print 자세히 알기

따옴표(")로 둘러싸인 문자열은 + 연산과 동일

>>> print("life" "is" "too short") -------------------- ① 
lifeistoo short 
>>> print("life"+"is"+"too short") -------------------- ② 
lifeistoo short
위에서 ①과 ②는 완전히 동일한 결과값을 보여준다. 즉, 따옴표로 둘러싸인 문자열을 연속해서 쓰면 '+'연산을 한 것과 마찬가지이다.

	문자열 띄어쓰기는 콤마로

>>> print("life", "is", "too short") 
life is too short
콤마(,)를 이용하면 문자열간에 띄어쓰기가 된다.
"""
print("life" "is" "too short")		# 띄어쓰기 안됌
print("life" + "is" + "too short")	# 띄어쓰기 안됌
print("life","is","too short")		# ,로 띄어쓰기
"""

	한 줄에 출력하기

앞서 보았던 구구단 프로그램에서 보았듯이 한 줄에 결과값을 계속 출력하려면 end파라미터를 이용하여 끝문자를 지정해야 한다.

>>> for i in range(10): 
...     print(i, end=' ')
... 
0 1 2 3 4 5 6 7 8 9
"""
for i in range(10):
	print(i, end=' ')