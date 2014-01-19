# -*- coding:utf-8 -*-
"""
5) 딕셔너리 (Dictionary)

Key이용하여 Value얻기

다음의 예를 따라해 보도록 하자.

>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99
리스트나 터플이나 문자열은 요소값을 얻어내기 위해서 인덱싱이나 슬라이싱이라는 기법을 사용했지만
딕셔너리는 단 한가지의 방법만이 있을 뿐이다. 바로 Key를 이용해서 Value를 얻어내는 방법이다.
위의 예에서처럼 Value를 얻기 위해서는 "딕셔너리변수[Key]" 와 같이 하여 Value를 얻을 수 있다.
"""
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
print()
"""
몇가지 예를 더 보도록 하자.

>>> a = {1:'a', 2:'b'}
>>> a[1]
'a'
>>> a[2]
'b'
먼저 a라는 변수에 {1:'a', 2:'b'}라는 딕셔너리를 대입하였다. 위의 예에서 보듯이 a[1]은 'a'라는 값을 돌려준다.
여기서 a[1]이 의미하는 것은 리스트나 터플의 a[1]과는 아주 다른 것이다.
여기서 [ ] 안의 숫자 1은 몇번째 요소를 뜻하는 것이 아니라 Key에 해당하는 1을 나타낸다.
딕셔너리는 리스트나 터플의 인덱싱 방법이란 것이 존재하지 않는다.
따라서 a[1]은 딕셔너리 {1:'a', 2:'b'}에서 Key가 1인것의 Value인 'a'를 돌려주게 된다. a[2] 역시 마찬가지이다.
"""
a = {1:'a', 2:'b'}
print(a[1])
print(a[2])
print()
"""
>>> a = {'a':1, 'b':2}
>>> a['a']
1
>>> a['b']
2 
이번에는 a라는 변수에 위에서 사용했던 딕셔너리의 Key와 Value를 뒤집어 놓은 딕셔너리를 대입해 보았다.
역시 a['a'], a['b']처럼 Key를 이용해서 Value를 얻을 수 있다.
이상 정리해 보면 딕셔너리 a 는 a[Key] 처럼 해서 Key에 해당하는 Value를 얻을 수 있다.
""""""
	딕셔너리 쌍 추가, 삭제하기

딕셔너리 쌍을 추가하는 방법은 Key를 이용해 Value를 호출했던 것처럼 새로운 Key에 Value를 설정하면 바로 딕셔너리에 추가된다.
예 1부터 예 3까지는 딕셔너리를 추가하는 예를 보여준다. 딕셔너리는 순서를 따지지 않는다.
예에서 알 수 있듯이 추가되는 순서는 원칙이 없다. 중요한 것은 “무엇이 추가되었는가” 이다.

다음의 예를 함께 따라해 보자.

예 1) 딕셔너리 쌍 추가1

	>>> a = {1: 'a'}
	>>> a[2] = 'b'
	>>> a
	{2: 'b', 1: 'a'}
	{1: 'a'}라는 딕셔너리에 a[2] = 'b'와 같이 사용해서 2 : 'b' 라는 딕셔너리 쌍을 추가하였다.

예 2) 딕셔너리 쌍 추가2

	>>> a['name'] = 'pey'
	{'name':'pey', 2: 'b', 1: 'a'}
	딕셔너리 a에 'name': 'pey'라는 쌍을 추가한 모습이다.

예 3) 딕셔너리 쌍 추가3

	>>> a[3] = [1,2,3]
	{'name': 'pey', 3: [1, 2, 3], 2: 'b', 1: 'a'}
	Key는 3 Value는 [1, 2, 3]을 가지는 한 쌍을 또 추가하였다.

예 4) 딕셔너리 요소 삭제 1

	>>> del a[1]
	>>> a
	{'name': 'pey', 3: [1, 2, 3], 2: 'b'}
	예 4는 딕셔너리의 요소를 지우는 방법을 보여준다. del a[key]하면 그에 해당하는 key:value 쌍이 삭제된다.
"""
a = {1: 'a'}
print(a)
#1
a[2] = 'b'
print(a)
#2
a['name'] = 'pey'
print(a)
#3
a[3] = [1,2,3]
print(a)
#4
del a[1]
print(a)
print()
"""
	딕셔너리 주의사항
	
	딕셔너리를 만들때 주의해야 할 사항은 Key는 고유한 값이므로
	중복되는 값을 설정해 놓으면 하나를 제외한 나머지의 것들은 무시된다는 점이다.
	다음 예에서 보듯이 Key가 동일한 것이 존재할 경우 1:'a'라는 쌍이 무시된다.
	이때 꼭 딕셔너리를 만들 때 앞에 썼던 것이 무시되는 것은 아니고 어떤 것이 무시될지는 예측이 불가능하다.
	결론은 중복되는 Key를 사용하지 말라는 것이다.
	
	>>> a = {1:'a', 1:'b'}
	>>> a 
	{1: 'b'}
	이렇게 중복되었을 때 한 개를 제외한 나머지의 Key:Value값이 무시되는 이유는
	딕셔너리는 Key를 통해서 Value를 얻게 되는데 만약 동일한 Key가 존재 한다면
	어떤 Key에 해당하는 Value를 불러야 할지 알 수가 없기 때문이다.
"""

"""
############################################################################################
	또 한 가지 주의해야 할 사항으로는 Key에 리스트는 쓸 수가 없다는 것이다.
	하지만 터플은 Key로 쓸 수가 있다.
	딕셔너리의 Key로 쓸 수 있고 없고의 구별은
	Key가 변하는 값인지 변하지 않는 값인지에 달려 있다.
	리스트를 Key로 사용한다면 그 값이 변할 수 있기 때문에 리스트를 Key로 쓸 수 없는 것이다.
	아래 예처럼 리스트를 Key로 설정하면 TypeError가 난다.
	
	>>> a = {[1,2] : 'hi'}
	Traceback (most recent call last):
	File "", line 1, in ?
	TypeError: unhashable type
	따라서 딕셔너리의 Key를 딕셔너리로 할 수 없음은 당연한 얘기가 될 것이다.
	Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다.
############################################################################################
"""
a = {(1,2) : 'hi', (3,4) : 'c'}
print(a)
print()
"""
############################## 딕셔너리 관련 메소드 ##############################
딕셔너리를 자유자재로 사용하기 위해 딕셔너리가 자체적으로 가지고 있는 관련 함수들을 사용해 보도록 하자.

	Key리스트 만들기(keys)
	
	>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
	>>> a.keys()
	dict_keys(['name', 'phone', 'birth'])
	a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체로 만든다.

	※ 파이썬 2.7 버전까지는 a.keys() 호출 시 리턴값으로 dict_keys 가 아닌 list 를 리턴한다.
	list 를 리턴하기 위해서는 메모리의 낭비가 발생하는데
	파이썬 3.0 이후버전에서는 이러한 메모리 낭비를 줄이기 위해서 dict_keys 라는 객체를 리턴하게 되었다.
	아래 소개될 dict_values, dict_items 역시 마찬가지로 파이썬 3.0 이후에 추가된 것들이다.
	만약 파이썬 2.7에서와 같이 list 가 필요한 경우에는 list(a.keys()) 로 리스트 형태로 변환하여 사용하면 된다.
	dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도
	기본적인 iterate성 구문(예: for문)들을 실행 할 수 있다.
""""""
	dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 차이가 없다.
	(※ 리스트 고유의 메소드인 append, insert, pop, remove, sort등의 메소드를 수행 할 수는 없다.)
	
	>>> for k in a.keys():
	...     print(k)
	...
	phone
	birth
	name
""""""
	dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
	
	>>> list(a.keys())
	['phone', 'birth', 'name']
"""
#dict_keys
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
	print(k)

print(list(a.keys()))
print()
"""
	Value리스트 만들기 (values)
	
	>>> a.values()
	dict_values(['pey', '0119993323', '1118'])
	마찬가지 방법으로 value만을 얻고 싶다면 a.values()처럼 values 함수를 사용하면 된다.
	values 함수 호출 시 dict_values 객체가 리턴된다.
	dict_values 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용하면 된다.
"""
#dict_values
print(a.values())

for v in a.values():
	print(v)

print(list(a.values()))
print()
"""
	Key, Value 쌍 얻기(items)
	
	>>> a.items()
	dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
	items 함수는 key와 value의 쌍을 터플로 묶은 값을 dict_items객체로 돌려준다.
"""
#dict_items
print(a.items())

for [k,v] in a.items():	#(k,v)도 가능
	print(k + ':' + v)

print(list(a.items()))
print()
"""
	Key: Value 쌍 모두 지우기(clear)
	
	>>> a.clear()
	>>> a
	{}
	clear() 함수는 딕셔너리 안의 모든 요소를 삭제한다.
	위에서 보듯이 빈 리스트가 [] 빈 터플이 ()인 것과 마찬가지로 빈 딕셔너리도 {}과 같이 표현된다.
"""
a.clear()
print(a)
print()
"""
	Key로 Value얻기 (get)
	
	>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
	>>> a.get('name')
	'pey'
	>>> a.get('phone')
	'0119993323' 
	get(x) 함수는 x 라는 key에 대응되는 value를 돌려준다.
	앞서 살펴 보았듯이 a.get('name')은 a['name']처럼 사용하는 것과 완전히 동일한 결과값을 돌려 받는다.
	어떤 것을 사용하는가는 독자의 선택이다.
""""""
	딕셔너리 내에 찾으려는 키값이 없을 경우 디폴트 값으로 가져오도록 하고 싶을 때에는 get(x, '디폴트값')을 사용하면 편리하다.
	
	>>> a.get('foo', 'bar')
	'bar'
	a 딕셔너리에는 'foo'에 해당하는 값이 없다. 따라서 디폴트 값인 'bar'를 리턴한다.
"""
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('foo', 'bar'))
print()
"""
해당 Key가 있는지 조사 (in)

>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> 'name' in a
True
>>> 'email' in a
False
'name' 이라는 문자열은 a 딕셔너리의 key 이다. 따라서 'name' in a 호출 시 True를 리턴한다.
반대로 'email' 은 a 딕셔너리에 존재하지 않는 키이므로 False 를 리턴하게 된다.
"""
print('name' in a)
print('email' in a)