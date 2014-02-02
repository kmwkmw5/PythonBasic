# -*- coding:utf-8 -*-
"""
	14.1 연산자의 중복
	14.1.1 수치 연산자 중복
"""
# 이항 연산자, 역 이항 연산자, 확장 산술 연산자
class MyStr:
	def __init__(self, s):
		self.s = s
	#python3 : __truediv__
	def __truediv__(self, other):
		return self.s.split(other)
	# 역 이항 연산자
	def __add__(self, other):
		return self.s + other.s
	# 확장 산술 연산자
	def __iadd__(self, other):
		return self.s + other.s

s1 = MyStr('a:b:c')
s2 = MyStr('z:')
s3 = MyStr(':z')
print(s1 / ':')
print(s2 + s1)
s1 += s3
print(s1)
'''
__add__		+
__sub__		-
__mul__		*
__div__		/
__truediv__	/				from __future__ import division이 실행되었을 경우
__floordiv__	//
__mod__		%
__divmod__		divmod()
__pow__		pow(), **		(self, other[, modulo])
__lshift__		<<
__rshift__		>>
__and__		&
__xor__		^
__or__			|
역 이항 연산자는 앞에 r을 붙임
'''

# 확장 산술 연산자



















