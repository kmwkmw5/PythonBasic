# -*- coding:utf-8 -*-
class Animal:
	kind = 'undefined'
	def __init__(self, name):
		self.name = name
	def __del__(self):
		print('Bye ' + self.name)
	
	def __add__(self, other):
		return self.name + ' & ' + other.name + ' get married'
	def __sub__(self, other):
		return self.name + ' & ' + other.name + ' get divorced'
	
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	def getKind(self):
		return self.kind
	def setKind(self, kind):
		self.kind = kind
	def bark(self):
		raise NotImplementedError
		
class Dog(Animal):
	kind = 'Dog'
	def bark(self):
		print('wal wal')
	
class Cat(Animal):
	kind = 'Cat'
	def bark(self):
		print('meow meow')
		
if __name__ == '__main__' :
	doggy = Dog('doggy')
	catty = Cat('catty')
	
	doggy.bark()
	catty.bark()