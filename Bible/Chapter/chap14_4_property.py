#===============================================================================
# 14.4 property 속성 만들기
#===============================================================================

#------------------------------------------------------------------------------ 
# property(fget=None, fset=None, fdel=None, doc=None)

class PropertyClass:
	def get_deg(self):
		print('get_deg call')
		return self.__deg
	def set_deg(self, d):
		print('set_deg call', d)
		self.__deg = d % 360
# 	def del_deg(self):
# 		print('del_deg call')
	deg = property(get_deg, set_deg)

p = PropertyClass()

p.deg = 390
#set_deg call 390

print(p.deg)
#get_deg call
#30

p.deg = -370
#set_deg call -370

print(p.deg)
#get_deg call
#350
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 장식자 이용

class PropertyClass2:
	@property
	def deg(self):
		print('getter')
		return self.__deg
	@deg.setter
	def deg(self, d):
		print('setter', d)
		self.__deg = d % 360

p = PropertyClass2()

p.deg = 390
#setter 390

print(p.deg)
#getter
#30

p.deg = -370
#setter -370

print(p.deg)
#getter
#350
#------------------------------------------------------------------------------ 