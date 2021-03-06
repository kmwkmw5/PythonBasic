# -*- coding:utf-8 -*-
"""
3) 리스트 (List)

>>> odd = [1,3,5,7,9]
리스트를 만들 때는 위에서 보는 것과 같이 대괄호([ ])로 감싸주고 안에 들어갈 값들은 쉼표로 구분해준다.

여러 가지 리스트의 생김새를 살펴보면 다음과 같다.

	>>> a = []
	>>> b = [1, 2, 3]
	>>> c = ['Life', 'is', 'too', 'short']
	>>> d = [1, 2, 'Life', 'is']
	>>> e = [1, 2, ['Life', 'is']]
a 처럼 리스트는 아무 것도 포함하지 않는 빈 리스트([])일 수도 있고
b처럼 숫자를 그 요소 값으로 가질 수도 있고,
c처럼 문자열을 요소값으로 가질 수 있고
d처럼 숫자와 문자열을 함께 요소값으로 가질 수 있으며
e처럼 리스트 자체를 그 요소 값으로 가질 수 도 있다. 즉, 리스트 내에는 어떠한 자료형도 포함시킬 수 있다.
""""""
	리스트의 인덱싱과 슬라이싱
리스트의 경우에도 문자열처럼 인덱싱과 슬라이싱이 가능하다. 백문이 불여일견. 말로 설명하는 것보다
직접 예를 따라해보면서 리스트의 기본 구조를 이해하는 것이 쉽다. 대화형 인터프리터로 예를 따라하며 알아보자.

	리스트의 인덱싱
a 변수에 [1, 2, 3] 이라는 값을 세팅한다.

>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
리스트 역시 문자열에서처럼 인덱싱이 적용된다.

	a[-1]은 문자열에서와 마찬가지로 리스트 a의 마지막 요소를 말한다.
	
	>>> a[-1]
	3

이번에는 아래의 예처럼 리스트 a를 숫자 1, 2, 3과 또다른 리스트인 ['a', 'b', 'c']를 포함하도록 만들어 보자.

>>> a = [1, 2, 3, ['a', 'b', 'c']]
다음의 예를 따라해 보자.

>>> a[0]
1
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
예상한 대로 a[-1]은 마지막 요소값인 ['a', 'b', 'c']를 나타낸다.
a[3]는 리스트 a의 네 번째 요소를 나타내기 때문에 마지막 요소를 나타내는 a[-1]과 동일한 결과값을 보여준다.
""""""
그렇다면 여기서 리스트 a에 포함된 ['a', 'b', 'c']라는 리스트의 'a'라는 값을 인덱싱을 이용하여 끄집어 낼 수 있는 방법은 없을까?

다음의 예를 보도록 하자.

>>> a[-1][0]
'a'
위처럼 하면 'a'를 끄집어 낼 수가 있다. a[-1]은 ['a', 'b', 'c']이고 다시 이것의 첫 번째 요소를 불러오기 위해서 [0]을 붙여준 것이다.

아래의 예도 역시 마찬가지 경우이므로 이해가 될 것이다.

>>> a[-1][1]
'b'
>>> a[-1][2]
'c'
""""""
조금은 복잡하지만 다음의 예를 따라해 보자

	>>> a = [1, 2, ['a', 'b', ['Life', 'is']]]
	리스트 a안에 리스트 ['a', 'b', ['Life', 'is']]라는 리스트가 포함되어 있고
	그 리스트 안에 역시 리스트 ['Life', 'is']라는 리스트가 포함되어 있다. 삼중 리스트 구조이다.
	
	'Life'라는 문자열만을 끄집어 내기 위해서는 다음과 같이 해야 한다.
	
	>>> a[2][2][0]
	'Life'
	즉 위의 예는 리스트 a의 세 번째 요소인 리스트['a', 'b', ['Life', 'is']]의
	세 번째 요소인 리스트 ['Life', 'is']의 첫 번째 요소를 말하는 것이다.
	이렇듯 리스트를 중첩해서 쓰면 혼란스럽기 때문에 자주 사용되지는 않지만 알아두는 것이 좋을 것이다.
"""
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])
print("")
"""
	리스트의 슬라이싱 알아보기
문자열에서와 마찬가지로 리스트에서도 슬라이싱 기법이 적용된다.
슬라이싱이라는 것은 “나눈다”라는 뜻이라고 했었다. 자, 그럼 리스트의 슬라이싱에 대해서 살펴보도록 하자.

>>> a = [1, 2, 3, 4, 5]
>>> a[0:2]
[1, 2]
이것을 문자열에서 했던 방법과 비교해서 생각 해보자.

>>> a = "12345"
>>> a[0:2]
'12'
두 가지가 완전히 동일하게 사용됨을 독자는 이미 눈치 챘을 것이다. 문자열에서 했던 것과 사용법이 완전히 동일하다.

몇가지 예를 더 들어 보도록 하자.

>>> a = [1, 2, 3, 4, 5]
>>> b = a[:2]
>>> c = a[2:]
>>> b
[1, 2]
>>> c
[3, 4, 5]
b라는 변수는 리스트 a의 처음 요소부터 2번째 요소까지를 나타내는 리스트이다.
여기서는 a[2] 값인 '3'이 포함되지 않는다. c라는 변수는 리스트 2번째 요소부터 끝까지를 나타내는 리스트이다.
""""""
리스트가 포함된 리스트역시 똑같이 적용된다.

>>> a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
>>> a[2:5]
[3, ['a', 'b', 'c'], 4]
>>> a[3][:2]
['a', 'b']
위의 예에서 a[3]은 ['a', 'b', 'c']를 나타내기 때문에 a[3][:2]는 ['a', 'b', 'c']의
a[0]에서 a[2]까지의 값 즉, ['a', 'b']를 나타내는 리스트가 된다.
"""
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[3][:2])
print("")
"""
	리스트를 더하고(+) 반복하기(*)

리스트 역시 + 기호를 이용해서 더할 수가 있고 * 기호를 이용해서 반복을 할 수가 있다.
문자열과 마찬가지로 리스트에서도 되는지 한번 직접 확인해 보도록 하자.

예 1) 리스트 합치기

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a + b
[1, 2, 3, 4, 5, 6]
두 개의 리스트를 ‘+’ 기호를 이용해 합치는 방법이다. 리스트 사이에서 ‘+’ 기호는 두 개의 리스트를 합치는 기능을 한다.
문자열에서 "abc" + "def" = "abcdef"가 되는 것과 같은 이치이다.

예 2) 리스트 반복

>>> a = [1, 2, 3]
>>> a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
위에서 보듯이 [1, 2, 3]이란 리스트가 세 번 반복되어 새로운 리스트를 만들어 내는 것을 볼 수 있다.
문자열에서 "abc" * 3 = "abcabcabc" 가 되는 것과 같은 이치이다.
"""
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
print("")
"""
	리스트의 수정 변경과 삭제

참고 - 다음의 예들은 서로 연관되어 있으므로 따로따로 실행해 보지 말고 예 1부터 예 4까지 차례대로 진행해 나가야 한다.

예 1) 리스트 수정1

	>>> a = [1, 2, 3]
	>>> a[2] = 4
	>>> a
	[1, 2, 4]

예 2) 리스트 수정2

	>>> a[1:2]
	[2]
	>>> a[1:2] = ['a', 'b', 'c']
	>>> a
	[1, 'a', 'b', 'c', 4]
	
	참고 - 여기서 a[1] = ['a', 'b', 'c']라고 하는 것과는 전혀 다른 결과값을 갖게 되므로 주의 하도록 하자.
	a[1] = ['a', 'b', 'c']는 리스트 a의 두 번째 요소를 ['a', 'b', 'c']로 바꾼다는 말이고
	a[1:2]는 a[1]에서 a[2]사이의 리스트를 ['a', 'b', 'c']로 바꾼다는 말이다.
	따라서 a[1] = ['a', 'b', 'c']처럼 하면 위와는 달리 리스트 a가 [1, ['a', 'b', 'c'], 4]라는 값으로 변하게 된다.
"""
"""
예 3) 리스트 요소 삭제1

	>>> a[1:3] = []
	>>> a
	[1, 'c', 4]

예 4) 리스트 요소 삭제 2

	>>> a
	[1, 'c', 4]
	>>> del a[1]
	>>> a
	[1, 4]
	del a[x]는 x번째 요소값을 삭제한다. del 함수는 파이썬이 자체적으로 가지고 있는 내장 함수로 다음과 같이 사용된다.
"""
a = [1, 2, 3]
print(a)
#1
a[2] = 4
print(a)
#2
a[1:2] = ['a', 'b', 'c']
print(a)
#3
a[1:3] = []
print(a)
#4
del a[1]
print(a)
print("")

#2-참고
a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print(a)

b = [1, 2, 3]
b[1:2] = ['a', 'b', 'c']
print(b)
print("")
"""
	del 객체
	(참고 - 객체란 파이썬에서 사용되는 모든 자료형을 말한다.)
	
	del a[x:y]는 x번째부터 y번째 요소 사이의 값을 삭제한다. 예 4에서는 a[1]을 삭제하는 방법을 보여준다.
""""""
	[참고] 초보가 범하기 쉬운 리스트 연산 오류
	우선 다음과 같은 예를 먼저 만들어보자.
	
	>>>a = [1, 2, 3]
	>>>a[2] + "hi"
	Traceback (innermost last):
	File "", line 1, in ?
	a[2] + "hi"
	TypeError: number coercion failed
	TypeError 에러가 발생했다. 에러의 원인은 무엇일까?
	
	a[2]는 3이라는 정수인데 "hi"는 문자열이다. 
	두 값(정수와 문자열)을 더한다는 것은 상식적으로 맞지 않는 방법이다. 
	그래서 Type 에러가 발생하는 것이다. 숫자와 문자열을 더할 수는 없다.
	
	만약 숫자와 문자열을 더해서 '3hi'처럼 만들고 싶다면 숫자 3을 문자 '3'으로 바꾸어 주어야 한다.
	
	다음과 같이 할 수 있다.
	>>>str(a[2]) + "hi"
	
	str 함수로 정수를 문자열로 바꾸어 주는 방법이다.
""""""
############################## 리스트 관련 메소드 ##############################

	리스트 정렬(sort)
	
	sort 함수는 리스트의 요소를 순서대로 정렬하여 정렬된 값을 돌려준다.
	
	>>> a = [1, 4, 3, 2]
	>>> a.sort()
	>>> a
	[1, 2, 3, 4]
	문자 역시 마찬가지로 알파벳 순서로 정렬이 가능하다.
	
	>>> a = ['a', 'c', 'b']
	>>> a.sort()
	>>> a
	['a', 'b', 'c']
"""
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)
print("")
"""
	리스트 뒤집기(reverse)
	
	reverse 함수는 리스트를 역순으로 뒤집어준다.
	하지만 이것이 의미하는 것이 먼저 순서대로 정렬한 다음에 다시 역순으로 정렬하는 것은 아니다.
	그저 리스트 그대로를 거꾸로 뒤집는 일을 할 뿐이다.
	
	>>> a = ['a', 'c', 'b']
	>>> a.reverse()
	>>> a
	['b', 'c', 'a']
"""
a = ['a', 'c', 'b']
a.reverse()
print(a)
print("")
"""
	위치 반환 (index)
	
	index(x) 함수는 리스트에 x라는 값이 있으면 그 위치를 돌려준다.
	
	>>> a = [1,2,3]
	>>> a.index(3)
	2
	>>> a.index(1)
	0
	위의 예에서 리스트 a에 있는 3이라는 숫자는 a[2]이므로 2를 돌려주고, 1이라는 숫자는 a[0]이므로 0을 돌려준다.
	
	아래의 예에서 0 이라는 값은 a 리스트에 존재하지 않기 때문에 에러가 난다.
	
	>>> a.index(0) 
	Traceback (innermost last):
	File "", line 1, in ?
	a.index(0)
	ValueError: list.index(x): x not in list
	Tracebace이란 문장부터 ValueError라는 문장까지가 에러메시지이다.
"""
a = [1,2,3]
print(a.index(3))
#print(a.index(0)) # error
print("")
"""
	갯수세기 (count)
	
	count(x)는 리스트 중에서 x가 몇 개 있는지를 조사하여 그 갯수를 돌려주는 함수이다.
	
	>>> a = [1,2,3,1]
	>>> a.count(1)
	2
	위의 예에서는 1이라는 값이 리스트 a에 두 개가 들어 있으므로 2를 돌려준다.
"""
a = [1,2,3,1]
print(a.count(1))
print("")
"""

	리스트 확장(extend)
	
	extend(x)에서 x에는 리스트만 올 수 있다. 원래의 a 리스트에 x 리스트를 더하게 된다.
	
	>>> a = [1,2,3]
	>>> a.extend([4,5])
	>>> a
	[1, 2, 3, 4, 5]
	a.extend([4,5])는 a = a + [4,5]와 동일하다.
"""
a = [1,2,3]
a.extend([4,5])
a += [6,7]
print(a)
"""
	리스트에 요소 추가 (append)
	
	append의 뜻이 무엇인지 안다면 아래의 예가 금방 이해가 될 것이다. append(x)는 리스트의 맨 마지막에 x를 추가시키는 함수이다.
	
	>>> a = [1, 2, 3] 
	>>> a.append(4)
	>>> a
	[1, 2, 3, 4]
	리스트내에는 어떤 자료형도 추가시킬 수가 있다. 아래의 예는 리스트에 다시 리스트를 추가시킨 결과를 보여준다.
	
	>>> a.append([5,6])
	>>> a
	[1, 2, 3, 4, [5, 6]]
"""
a = [1, 2, 3]
a.append(4)
a.append([5,6])
print(a)
print("")
"""
	리스트에 요소 삽입 (insert)
	
	insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다.
	
	>>> a = [1,2,3]
	>>> a.insert(0, 4)
	[4, 1, 2, 3]
	위의 예에서는 0번째 자리 즉 첫 번째 자리에 4 라는 값을 삽입하라는 뜻이 된다.
	
	아래의 예는 리스트 a의 a[3], 즉 네 번째 자리에 5라는 값을 삽입하라는 뜻이다.
	
	>>> a.insert(3, 5)
	[4, 1, 2, 5, 3]
"""
a = [1,2,3]
a.insert(0, 4)
print(a)
print("")
"""
	리스트 요소 제거 (remove)
	
	remove(x)는 첫번째 나오는 x 를 삭제하는 함수이다. 아래의 예는 a가 3이라는 값을 두개 가지고 있을경우
	첫번째 3만을 제거하는 것을 보여준다.
	
	>>> a = [1,2,3,1,2,3]
	>>> a.remove(3)
	[1, 2, 1, 2, 3]
	다시 또 3을 삭제한다.
	
	>>> a.remove(3)
	[1, 2, 1, 2]
"""
a = [1,2,3,1,2,3]
print(a)
a.remove(3)
print(a)
a.remove(3)
print(a)
print("")
"""
	리스트 요소 끄집어내기(pop)
	
	pop() 함수는 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
	
	>>> a = [1,2,3]
	>>> a.pop()
	3
	>>> a
	[1, 2]
	위의 예에서 보듯이 a 리스트 [1,2,3]에서 3을 끄집어내어서 최종적으로 [1, 2]만 남는 것을 볼 수 있다.
	
	pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.
	
	>>> a = [1,2,3]
	>>> a.pop(1)
	2
	>>> a
	[1, 3]
	위의 예에서 보듯이 a.pop(1)는 a[1]의 값을 끄집어낸다.
"""
a = [1,2,3,4,5]
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
print("")