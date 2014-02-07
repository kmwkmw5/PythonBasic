#===============================================================================
# 14.2 장식자(Decorator)
#===============================================================================

#===============================================================================
# 14.2.1 장식자의 이해
#===============================================================================

#------------------------------------------------------------------------------ 
# 장식자 : 함수를 인수로 받는 함수 클로저
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# wrapper 함수
def wrapper(func):
	def wrapped_func():
		print('before...')
		func()
		print('after...')
	return wrapped_func
#----------------------------------
# 장식자를 사용하지 않은 적용
def myfunc():
	print('I am here')
myfunc = wrapper(myfunc)
#----------------------------------
myfunc()
#before...
#I am here
#after...
#----------------------------------
# 장식자 형태의 적용
@wrapper
def myfunc2():
	print('I am here')
#----------------------------------
myfunc2()
#before...
#I am here
#after...
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 장식자를 사용하는 대표적인 예 : 정적 메소드, 클래스 메소드
# 아래 D, D2는 동일한 결과
class D:
	@staticmethod
	def add(x, y):
		return x+y

class D2:
	def add(x, y):
		return x+y
	add = staticmethod(add)

print(D.add(2, 4))
#6
print(D2.add(2, 4))
#6
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.2 연결된 장식자
#===============================================================================

#------------------------------------------------------------------------------ 
def makebold(fn):
	def wrapper():
		return "<b>" + fn() + "</b>"
	return wrapper

def makeitalic(fn):
	def wrapper():
		return "<i>" + fn() + "</i>"
	return wrapper

@makebold
@makeitalic
def say():
	return "Hello"

print(say())
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.3 장식된 함수에 인수를 전달하기
#===============================================================================

#------------------------------------------------------------------------------
# 일반 예제
 
def debug(fn):
	def wrapper(a, b):
		print('dubug', a, b)
		return fn(a, b)
	return wrapper
@debug
def add(a, b):
	return a+b
print(add(1, 2))
#dubug 1 2
#3

# 일반화된 예제
def debug2(fn):
	def wrapper(*args, **kw):
		print('calling', fn.__name__, 'args =', args, 'kw =', kw)
		result = fn(*args, **kw)
		print('\tresult =', result)
		return result
	return wrapper
@debug2
def add2(a, b):
	return a+b
print(add2(1, 2))
#calling add2 args = (1, 2) kw = {}
#	result = 3
#3
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.4 인수를 갖는 장식자
#===============================================================================

#------------------------------------------------------------------------------ 
# 장식자 내부에 또 다른 장식자가 정의(함수 세 개 중첩)
def accepts(*types):
	def check_accepts(f):
		def new_f(*args, **kw):
			for(a, t) in zip(args, types):
				assert isinstance(a, t), "arg {} does not match {}".format(a, t)
			return f(*args, **kw)
		return new_f
	return check_accepts

@accepts(int, int)
def add3(a, b):
	return a+b
print(add3(1, 2))
#3
#print(add3(3.4, 6))
#AssertionError: arg 3.4 does not match <class 'int'>
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.5 메소드 장식하기
#===============================================================================

#------------------------------------------------------------------------------ 
def accepts2(*types):
	def check_accepts(f):
		def new_f(self, *args, **kw):
			for(a, t) in zip(args, types):
				assert isinstance(a, t), "arg {} does not match {}".format(a, t)
			return f(self, *args, **kw)
		return new_f
	return check_accepts
class Sori:
	@accepts2(int, int)
	def add(self, a, b):
		return a+b
s = Sori()
print(s.add(2, 3))
#5
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# @functools.wraps
def debug3(fn):
	def wrapper(*args, **kw):
		result = fn(*args, **kw)
	return wrapper
class Sori3:
	@debug3
	def add(self, a, b):
		return a+b
s = Sori3()
print(s.add.__name__)
#wrapper -> add가 나와야 되는데 장식자로 인해 발생한 문제 -> @functools.wraps 해결

import functools
def debug4(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		return fn(*args, **kw)
	return wrapper
class Sori4:
	@debug4
	def add(self, a, b):
		'''doc string'''
		return a+b
s = Sori4()
print(s.add.__name__)
print(s.add.__doc__)
#add
#doc string
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.7 클래스 장식자
#===============================================================================

#------------------------------------------------------------------------------ 
import functools
class class_decorator:
	def __init__(self, view_func):
		self.view_func = view_func
		functools.wraps(view_func)(self)
	def __call__(self, request, *args, **kw):
		print('호출 전에 수행할 코드들...')
		response = self.view_func(request, *args, **kw)
		print('호출 이후에 수행할 코드들...')
		return response
@class_decorator
def add4(a, b):
	return a+b
print(add4(1, 2))
#호출 전에 수행할 코드들...
#호출 이후에 수행할 코드들...
#3
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.2.8 유용한 장식자들
#===============================================================================

import functools

def counter(func):
	"""
	함수 호출 횟수를 센다.
	"""
	@functools.wraps(func)
	def wrapper(*args, **kw):
		wrapper.count = wrapper.count + 1
		res = func(*args, **kw)
		print("{0} : {1} 호출".format(func.__name__, wrapper.count))
		return res
	wrapper.count = 0
	return wrapper

def logging(func):
	"""
	함수 호출 내용을 로깅(프린트)하는 장식자이다.
	"""
	@functools.wraps(func)
	def wrapper(*args, **kw):
		res = func(*args, **kw)
		print('{}({}, {}) => {}'.format(func.__name__, args, kw, res))
		return res
	return wrapper

def benchmark(func):
	"""
	실행 시간을 출력하는 장식자이다.
	"""
	import time
	@functools.wraps(func)
	def wrapper(*args, **kw):
		t = time.clock()
		res = func(*args, **kw)
		print(func.__name__, time.clock() - t)
		return res
	return wrapper

@counter
@benchmark
@logging
def add5(a, b):
	return a+b
print(add5(1, 2))
#add5((1, 2), {}) => 3
#add5 0.0
#add5 : 1 호출
#3
print(add5(2, 3))
#add5((2, 3), {}) => 5
#add5 0.0
#add5 : 2 호출
#5