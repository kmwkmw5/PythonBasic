#===============================================================================
# 제 14 장 연산자의 중복과 장식자
#===============================================================================

#===============================================================================
# 14.1 연산자의 중복
#===============================================================================

#===============================================================================
# 14.1.1 수치 연산자 중복
# 이항 연산자, 역 이항 연산자, 확장 산술 연산자, 단항 연산자, 기타 형변환
#===============================================================================

#------------------------------------------------------------------------------ 
'''
이항 연산자
역 이항 연산자는 앞에 r, 확장 산술 연산자는 앞에 i를 붙임
__add__			+
__sub__			-
__mul__			*
__truediv__		/
__floordiv__	//
__mod__			%
__divmod__		divmod()
__pow__			pow(), **		(self, other[, modulo])
__lshift__		<<
__rshift__		>>
__and__			&
__xor__			^
__or__			|

단항 연산자
__neg__			-
__pos__			+
__abs__			abs()
__invert__		~				비트 반전
'''

class MyStr:
	def __init__(self, s):
		self.s = s
	# 이항 연산자
	def __truediv__(self, other):
		return self.s.split(other)
	def __add__(self, other):
		return self.s + other
	# 역이항 연산자
	def __radd__(self, other):
		return other + self.s
	# 확장 산술 연산자
	def __iadd__(self, other):
		self.s = self.s + other
		return self

s1 = MyStr('a:b:c')
print(s1 / ':')
#['a', 'b', 'c']
print(s1 + ':d')
#a:b:c:d
print('z:' + s1)
#z:a:b:c
s1 += ':d'
print(s1.s)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
'''
기타 형변환 416p
__complex__		complex()
__int__			int()
__float__		float()
__round__		round()
__index__		operator.index()	인덱스 값으로 사용될 때 호출
'''
class Index:
	def __index__(self):
		print('__index__ called')
		return 3
L = [1,2,3,4,5]
i = Index()
print(L[i])
#__index__ called
#4
print(bin(i))
#0b11
print(oct(i))
#0o3
print(hex(i))
#0x3
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.2 컨테이너 자료형의 연산자 중복
#===============================================================================

#------------------------------------------------------------------------------ 
# 기본적으로 구현해야 하는 것들
#		__len__, __contains__, __getitem__, __setitem__, __delitem__
# 시퀀스형이면서 변경 가능한 자료형
#		append, count, index, extend, insert, pop, remove, reverse, sort
# 사전과 같은 매핑 자료형
#		keys, values, items, get, clear, copy, setdefault, pop, popitem, update
# 산술 연산
#		__add__, __radd__, __iadd__, __mul__, __rmul__, __imul__
# 반복자 지원
#		__iter__
#------------------------------------------------------------------------------ 

#===============================================================================
# 1 인덱싱
#===============================================================================

# __getitem__()의 구현과 예외처리(TypeError, IndexError)
class Square:
	def __init__(self, end):
		self.end = end
	def __len__(self):
		return self.end
	def __getitem__(self, k):
		if type(k) != int:
			raise TypeError('...')
		if k<0 or k>=self.end:
			raise IndexError('index {} out of range'.format(k))
		return k*k

s1 = Square(10)
print(len(s1))
#10
print(s1[4])
#16
#print(s1[20])
#IndexError: index 20 out of range
#print(s1['a'])
#TypeError: ...

# for문은 __getitem__() 메소드를 0부터 호출하기 시작한다.
for x in s1:
	print(x, end=' ')
print('')
#0 1 4 9 16 25 36 49 64 81 

# 다른 시퀀스 자료형으로 변환
print(list(s1))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(tuple(s1))
#(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)































