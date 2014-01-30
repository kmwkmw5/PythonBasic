#===============================================================================
# 제 11 장 함수
#===============================================================================

#===============================================================================
# 11.1 함수의 정의
#===============================================================================

#===============================================================================
# 11.2 함수의 호출
#===============================================================================

#===============================================================================
# 11.3 유효 범위
#===============================================================================

#------------------------------------------------------------------------------ 
# 유효 범위 규칙(Scope Rule) : LEGB 규칙
# L : Local
# E : Enclosing Function Local
# G : Global
# B : Built-in
x = 10					# G
y = 11
def foo():
	x = 20				# L:foo, E:bar
	def bar():
		a = 30			# L
		print(a, x, y)	# L, E, G
	bar()
	x = 40
	bar()
foo()
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# global 문
def f(a):
	global h
	h = a + 10
f(1)
print(h)
#11

# nonlocal 문 : 가장 가까운 이름 공간에서부터 변수를 찾는다.
def outer():
	x = 1
	def inner():
		nonlocal x
		x = 2
		print("inner:", x)
	inner()
	print("outer:", x)
outer()
#inner: 2
#outer: 2
#------------------------------------------------------------------------------

#==============================================================================
# 11.4 함수의 인수
#==============================================================================

# 인수의 기본값, 키워드 인수, 가변 인수(튜플)

#------------------------------------------------------------------------------ 
# 정의되지 않은 키워드 인수 처리하기
def f2(width, height, **kw):
	print(width, height)
	print(kw)
f2(width=10, height=5, depth=10, dimension=3)
#10 5
#{'depth': 10, 'dimension': 3}

def g(a, b, *args, **kw):
	print(a, b, args, kw)
g(1,2,3,4,c=5,d=6)
#1 2 (3, 4) {'d': 6, 'c': 5}
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 튜플 인수와 사전 인수로 함수 호출하기
def h(a, b, c):
	print(a, b, c)

# 튜플 넘기기
args = (1, 2, 3)
h(*args)
#1 2 3

# 사전 넘기기
dargs = {'a':1, 'b':2, 'c':3}
h(**dargs)
#1 2 3

# 튜플, 사전 같이 넘기기
args = (1, 2)
dargs = {'c': 3}
h(*args, **dargs)
#1 2 3
#------------------------------------------------------------------------------ 

#===============================================================================
# 11.5 함수 안의 함수
#===============================================================================

#------------------------------------------------------------------------------ 
# 일급 함수

# 함수를 변수에 저장
def add(a, b):
	return a + b
addition = add
print(addition(3, 4))
#7

# 함수를 인수로 전달
def f3(g, a, b):
	return g(a, b)
print(f3(add, 2, 3))
#5

# 함수를 반환
def decorate(type = 'italic'):
	def italic(s):
		return '<i>' + s + '</i>'
	def bold(s):
		return '<b>' + s + '</b>'
	if type == 'italic':
		return italic
	else:
		return bold
	
# 변수에 넣어 사용시
bold_dec = decorate('bold')
ital_dec = decorate('italic')
print(bold_dec('hello'))
#<b>hello</b>
print(ital_dec('hello'))
#<i>hello</i>

# 단독 사용시
print(decorate()('hello'))
#<i>hello</i>
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 함수 클로저
def quadratic(a, b, c):
	cache = {}
	def f(x):
		if x in cache:
			return cache[x]
		y = a*x*x + b*x + c
		cache[x] = y
		return y
	return f
f1 = quadratic(3, -4, 5)
print(f1(0.1))
#4.63
f2 = quadratic(-2, 7, 10)
print(f2(0.4))
#12.48

def makeCounter():
	count = 0
	def counter():
		nonlocal count
		count += 1
		return count
	return counter
c1 = makeCounter()
c2 = makeCounter()
print(c1()) #1
print(c1()) #2
print(c2()) #1

print(c1.__closure__)
#(<cell at 0x7fb755bbfe50: int object at 0x856e20>,)
print(c1.__closure__[0])
#<cell at 0x7fe6f532fe50: int object at 0x856e20>
print(c1.__closure__[0].cell_contents)
#2
c1()
print(c1.__closure__[0].cell_contents)
#3
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# partial(클로저가 될 함수, 함수에 전달할 인자) 함수 : 함수 클로저를 반환하는 함수
from functools import partial
def quadratic2(x, a, b, c):
	return a*x*x + b*x + c
f1 = partial(quadratic2, a=3, b=-4, c=5)
print(f1(0.1))
#4.63
bin2int = partial(int, base=2)
print(bin2int('10010')) # int('10010', base=2)
#18
#------------------------------------------------------------------------------ 

#===============================================================================
# 11.6 한 줄짜리 함수 : 람다 함수
#===============================================================================

#------------------------------------------------------------------------------ 
# lambda 인수들 : 반환식

f = lambda:1
print(f())
#1

g = lambda x, y=1 : x+y
print(g(1))
#2
print(g(1,2))
#3

h1 = lambda x, *args : args
print(h1(1,2,3,4,5))
#(2, 3, 4, 5)

h2 = lambda x, *args, **kw : kw
print(h2(1,2,3,a=4,b=5))
#{'a': 4, 'b': 5}
#------------------------------------------------------------------------------ 

#===============================================================================
# 11.7 함수적 프로그래밍
#===============================================================================

#------------------------------------------------------------------------------ 
# map(반복할 함수, 반복할 인자)

# 정의된 함수
def ff(x):
	return x*x
X = [1,2,3,4,5]
print(map(ff, X))
#<map object at 0x7f4f62cd49d0>
print(list(map(ff, X)))
#[1, 4, 9, 16, 25]

# lambda
X = range(1,6)
Y = map(lambda a : a*a, X)
print(list(Y))
#[1, 4, 9, 16, 25]

# lambda 인자 2개
X = range(1,6)
Y = range(6,11)
Z = map(lambda x,y : x+y, X, Y)
print(list(Z))
#[7, 9, 11, 13, 15]
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# filter(bool을 리턴하는 함수, 시퀀스)

f = filter(lambda x : x>2, [1, 2, 3, 34])
print(list(f))
#[3, 34]

print(''.join(filter(lambda x : x<'a', 'abcABCdefDEF')))
#ABCDEF

# None : 진리값 그대로 이용
L = ['high', 'level', '', 'built-in', '', [], (), 'a']
print(list(filter(None, L)))
#['high', 'level', 'built-in', 'a']
#------------------------------------------------------------------------------ 

#===============================================================================
# 11.8 함수 객체의 속성
#===============================================================================

#------------------------------------------------------------------------------
# http://docs.python.org/3.3/reference/datamodel.html?highlight=__defaults__ 
# __doc__ : 문서 문자열
# __name__ : 함수의 이름
# __defaults__ : 기본 인수 값들
# __code__ : 코드 객체
# __globals__ : 함수의 전역 영역을 나타내는 사전
#------------------------------------------------------------------------------ 

def fff(a, b, c=1):
	'func attribute testing'
	localx = 1
	localy = 2
	return 1
print(fff.__doc__)
#func attribute testing
print(fff.__name__)
#fff
print(fff.__defaults__)
#(1,)
print(fff.__code__)
#<code object fff at 0x7f64e6c7d420, file "/home/miki29/workspace/PythonBasic/Bible/Chapter/chap11_function.py", line 286>
print(fff.__globals__)
#{'__doc__': None, 'addition': <function add at 0x7f64e6c7d8c0>, '__file__': '/home/miki29/workspace/PythonBasic/Bible/Chapter/chap11_function.py', 'outer': <function outer at 0x7f64e6c7d680>, '__loader__': <_frozen_importlib.SourceFileLoader object at 0x7f64e80e0f10>, 'y': 11, 'x': 10, 'foo': <function foo at 0x7f64e6c7d560>, 'ital_dec': <function decorate.<locals>.italic at 0x7f64e6c7da70>, 'add': <function add at 0x7f64e6c7d8c0>, 'h2': <function <lambda> at 0x7f64e6c7def0>, 'g': <function <lambda> at 0x7f64e6c7d5f0>, 'f': <filter object at 0x7f64e6c7ac10>, 'decorate': <function decorate at 0x7f64e6c7d9e0>, '__name__': '__main__', 'bin2int': functools.partial(<class 'int'>, base=2), 'h': <function h at 0x7f64e6c7d830>, 'Z': <map object at 0x7f64e6c7ab50>, '__package__': None, 'makeCounter': <function makeCounter at 0x7f64e6c7d710>, 'L': ['high', 'level', '', 'built-in', '', [], (), 'a'], 'quadratic2': <function quadratic2 at 0x7f64e6c7de60>, '__cached__': None, 'partial': <class 'functools.partial'>, 'args': (1, 2), 'Y': range(6, 11), 'c2': <function makeCounter.<locals>.counter at 0x7f64e6c7ddd0>, 'c1': <function makeCounter.<locals>.counter at 0x7f64e6c7dd40>, 'X': range(1, 6), 'ff': <function ff at 0x7f64e6c7df80>, 'fff': <function fff at 0x7f64e6c7dc20>, 'f1': functools.partial(<function quadratic2 at 0x7f64e6c7de60>, c=5, b=-4, a=3), 'f2': <function quadratic.<locals>.f at 0x7f64e6c7dcb0>, 'f3': <function f3 at 0x7f64e6c7d950>, 'dargs': {'c': 3}, '__builtins__': <module 'builtins' (built-in)>, 'h1': <function <lambda> at 0x7f64e6c7d7a0>, 'bold_dec': <function decorate.<locals>.bold at 0x7f64e6c7db00>, 'quadratic': <function quadratic at 0x7f64e6c7db90>}

#===============================================================================
# 11.9 재귀적 프로그래밍
#===============================================================================