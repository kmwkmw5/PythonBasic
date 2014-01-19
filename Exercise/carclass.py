class Car:
	name = ''
	color = ''
	
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	def __del__(self):
		pass
		
	def __add__(self, other):
		return 'add ok'
	
	def __sub__(self, other):
		return 'sub ok'
	
	def getName(self):
		return self.name
	
	def getColor(self):
		return self.color
	
	def setName(self, name):
		self.name = name
		
	def setColor(self, color):
		self.color = color

myCar = Car('Tico', 'red')
print(myCar.getName())
print(myCar.getColor())

yourCar = Car('Audi', 'blue')
print(yourCar.getName())
print(yourCar.getColor())

print(myCar + yourCar)
print(myCar - yourCar)

myCar.setName('superTico')
print(myCar.name)