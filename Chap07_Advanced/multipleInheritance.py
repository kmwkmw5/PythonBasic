# -*- coding:utf-8 -*-
# 일반적인 다중상속
class ParentOne:
	def func(self):
		print("ParentOne의 함수 호출!")
	
class ParentTwo:
	def func(self):
		print("ParentTwo의 함수 호출!")
	
class Child(ParentOne, ParentTwo):
	def childFunc(self):
		ParentOne.func(self)
		ParentTwo.func(self)
		
objectChild = Child()
objectChild.childFunc()
objectChild.func()	# ParentOne의 메소드가 호출됨(먼저 쓴 인수)
print('')

# 다이아몬드 구조
class A:
	def __init__(self):
		print("A 클래스의 생성자 호출!")
		
class B(A):
	def __init__(self):
		A.__init__(self)
		print("B 클래스의 생성자 호출!")
	
class C(A):
	def __init__(self):
		A.__init__(self)
		print("C 클래스의 생성자 호출!")
	
class D(B, C):
	def __init__(self):
		B.__init__(self)
		C.__init__(self)
		print("D 클래스의 생성자 호출!")
	
objectD = D()		# A의 생성자(일반적으로는 메소드)가 두 번 호출됨.
print('')
"""
# super를 통한 해결(python3)
class AA:
	def __init__(self):
		print("A 클래스의 생성자 호출!")

class BB(AA):
	def __init__(self):
		super().__init__()
		print("B 클래스의 생성자 호출!")

class CC(AA):
	def __init__(self):
		super().__init__()
		print("C 클래스의 생성자 호출!")

class DD(BB, CC):
	def __init__(self):
		super().__init__()
		print("D 클래스의 생성자 호출!")
	
objectDD = DD()
"""