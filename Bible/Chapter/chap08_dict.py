#===============================================================================
# 제 8 장 사전
#===============================================================================

#===============================================================================
# 8.1 사전의 연산
#===============================================================================

#------------------------------------------------------------------------------ 
# 사전의 생성
print({'one':1, 'two':2})
print(dict(one=1, two=2))
print(dict({'one':1, 'two':2}))
print(dict([('one',1), ('two',2)]))
#{'two': 2, 'one': 1}

keys = ['one', 'two', 'three']
values = (1,2,3)
print(zip(keys, values))
#<zip object at 0x7f41ae970fc8>
#[('one', 1), ('two', 2), ('three', 3)]
print(dict(zip(keys, values)))
#{'one': 1, 'three': 3, 'two': 2}
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# for 문에서의 반복 : 키, 순서는 무시
D = {'a':3, 'b':2, 'c':1}
for key in D:	# D.keys()와 동일한 결과
	print(key, D[key])
#b 2
#c 1
#a 3
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 리눅스의 passwd 파일을 사전으로 읽는 예제
#pwd_dict.py
#------------------------------------------------------------------------------ 

#===============================================================================
# 8.2 사전의 뷰
# .keys(), .values(), .items()
#===============================================================================

#===============================================================================
# 8.3 사전의 메소드
# http://docs.python.org/3.3/library/stdtypes.html#mapping-types-dict
#===============================================================================

#===============================================================================
# 8.4 사전 내장(Dictionary Comprehension)
#===============================================================================

print({w:1 for w in 'abc'})
#{'a': 1, 'c': 1, 'b': 1}

a1 = 'abcd'
a2 = (1, 2, 3, 4)
print({x:y for x,y in zip(a1, a2)})
#{'d': 4, 'a': 1, 'c': 3, 'b': 2}

print({w:k for k,w in [(1, 'one'), (2, 'two'), (3, 'three')]})
#{'two': 2, 'three': 3, 'one': 1}

# enumerate(시퀀스) 함수 : 시퀀스형 데이터를 (인덱스, 값)의 터플 형태로 반환, for문과 연계
print({w:k+1 for k,w in enumerate(['one', 'two', 'three'])})
#{'two': 2, 'three': 3, 'one': 1}

#===============================================================================
# 8.5 심볼 테이블
# 변수들이 사전의 형태로 저장되는 공간
#===============================================================================

#------------------------------------------------------------------------------
# 전역/지역 심볼 테이블
#------------------------------------------------------------------------------

# globals()
a = 1
print(globals())
#{'a': 1,
#'__package__': None, '__doc__': None, '__name__': '__main__',
#'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
#'__builtins__': <module 'builtins' (built-in)>}

# locals()
def f(a, b):
	c = 10
	print(locals())
f(2, 3)
#{'b': 3, 'c': 10, 'a': 2} 

#------------------------------------------------------------------------------ 
# 객체(이름 공간)의 심볼 테이블
#------------------------------------------------------------------------------ 

# 모듈의 심볼 테이블
import re
print(re.__dict__) # 모듈의 심볼 테이블(엄청 길다)

# 클래스의 심볼 테이블
class C:
	x = 10
	y = 20
print(C.__dict__)
#{'__dict__': <attribute '__dict__' of 'C' objects>,
#'__weakref__': <attribute '__weakref__' of 'C' objects>,
#'x': 10, 'y': 20,
#'__module__': '__main__', '__doc__': None}

# 인스턴스의 심볼 테이블(x,y가 없음)
c = C()
c.a = 100
c.b = 200
print(c.__dict__)
#{'a': 100, 'b': 200}

# 함수의 심볼 테이블(locals()의 f함수 이용)(c가 없음)
f.x = 20
print(f.__dict__)
#{'x': 20}

#------------------------------------------------------------------------------ 
# 아래의 문장들은 모두 같은 값을 얻어냄
import math
print(math.sin)
print(math.__dict__['sin'])
print(getattr(math, 'sin')) # getattr(이름공간, 이름)
#<built-in function sin>

# 아래의 문장들은 모두 같은 값을 설정함
math.mypi = 3.14
math.__dict__['mypi'] = 3.14
setattr(math, 'mypi', 3.14)

# 자신의 모듈을 참조하기
import sys
current_module = sys.modules[__name__]
print(current_module)
#<module '__main__' from '/home/miki29/workspace/PythonBasic/Bible/Chapter/chap08_dict.py'>
print(current_module.__dict__)
#{'__file__': '/home/miki29/workspace/PythonBasic/Bible/Chapter/chap08_dict.py',
#'f': <function f at 0x7f8dfd758050>, 'D': {'c': 1, 'b': 2, 'a': 3}, 'key': 'a',
#'__package__': None, 'a': 1, '__doc__': None, 'values': (1, 2, 3),
#'current_module': <module '__main__' from '/home/miki29/workspace/PythonBasic/Bible/Chapter/chap08_dict.py'>,
#'c': <__main__.C object at 0x7f8dfd756bd0>,
#'math': <module 'math' from '/usr/local/lib/python3.3/lib-dynload/math.cpython-33m.so'>,
#'re': <module 're' from '/usr/local/lib/python3.3/re.py'>,
#'__loader__': <_frozen_importlib.SourceFileLoader object at 0x7f8dfeb5dfd0>,
#'__cached__': None, 'a1': 'abcd', 'C': <class '__main__.C'>, 'keys': ['one', 'two', 'three'],
#'sys': <module 'sys' (built-in)>, 'a2': (1, 2, 3, 4), '__builtins__': <module 'builtins' (built-in)>,
#'__name__': '__main__'}
#------------------------------------------------------------------------------ 

#===============================================================================
# 8.6 이름 공간 구현하기
#===============================================================================

ns_list = []

ns_list.append({})
ns_list[-1]['x'] = 1
ns_list[-1]['a'] = 1

ns_list.append({})
ns_list[-1]['x'] = 2
ns_list[-1]['b'] = 2

ns_list.append({})
ns_list[-1]['x'] = 3
ns_list[-1]['c'] = 3

print(ns_list)
#[{'x': 1, 'a': 1}, {'x': 2, 'b': 2}, {'x': 3, 'c': 3}]

def getValue(name):
	for ns in reversed(ns_list):
		if name in ns:
			return ns[name]

print(getValue('x'))
#3

#===============================================================================
# 8.7 순서를 유지하는 사전 : OrderedDict 사전
#===============================================================================

from collections import OrderedDict
d = OrderedDict()
d['one'] = 1
d['ten'] = 10
d['two'] = 2
print(d)
#OrderedDict([('one', 1), ('ten', 10), ('two', 2)])
print(d.popitem())
#('two', 2)
d['two'] = 2
d.move_to_end('ten')
print(d)
#OrderedDict([('one', 1), ('two', 2), ('ten', 10)])