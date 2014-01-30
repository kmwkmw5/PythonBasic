import math
class Rectangle(object):
     
    def __init__(self,r):
        self.r = r
     
    @property
    def area(self):
        return self.r*self.r
     
    @property
    def sqrt(self):
        return self.r*math.sqrt(2)
   
a = Rectangle(4)
     
print a.area  # 16 
print a.sqrt  # 5.65685424949
     
a.area = 1  # AttributeError: can't set attribute