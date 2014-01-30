# -*- coding:utf-8 -*-
class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __del__(self):
		print('Bye ' + self.name)
	
	def __add__(self, other):
		return self.name + ' & ' + other.name + ' get married'
	def __sub__(self, other):
		return self.name + ' & ' + other.name + ' get divorced'
	
	def __repr__(self):
		return '저는 %d살 %s 입니다.' % (self.age, self.name)
	# python2
	def __cmp__(self, other):
		return self.age - other.age
	
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	def getAge(self):
		return self.age
	def setAge(self, age):
		self.age = age
	def getKind(self):
		return self.kind
	def setKind(self, kind):
		self.kind = kind
	def bark(self):
		raise NotImplementedError
		
class Dog(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, name, age)
		self.kind = 'dog'
	def bark(self):
		print('wal wal')
	
class Cat(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, name, age)
		self.kind = 'cat'
	def bark(self):
		print('meow meow')
		
if __name__ == '__main__' :
	doggy = Dog('doggy', 5)
	catty = Cat('catty', 7)
	
	print(doggy)
	print(catty)
	if doggy > catty:
		print('%s가 %s보다 나이가 많습니다.' % (doggy.getName(), catty.getName()))
	elif doggy == catty:
		print('%s와 %s는 나이가 서로 같습니다.' % (doggy.getName(), catty.getName()))
	else:
		print('%s가 %s보다 나이가 적습니다.' % (doggy.getName(), catty.getName()))
	
	doggy.bark()
	catty.bark()