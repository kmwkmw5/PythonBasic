class MyClass:
	__age = 23
	hobby = 'coding'
	def __privateMethod(self):
		self.__name = 'abc'
		print('private method' + str(self.__age))
	def publicMethod(self):
		print('publid method' + str(self.hobby))
		
m = MyClass()
m.publicMethod()
#m.__privateMethod() # error
m._MyClass__privateMethod()

#print(m.__name) # error
#print(m.__age) # error