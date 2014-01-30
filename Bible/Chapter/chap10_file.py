#===============================================================================
# 제 10 장 파일
#===============================================================================

#===============================================================================
# 10.1 텍스트 파일 쓰기/읽기
#===============================================================================

with open('t1.txt', 'w', encoding = 'utf-8') as f:
	print(f)
	#<_io.TextIOWrapper name='t1.txt' mode='w' encoding='utf-8'>
	f.write('chap10')

#===============================================================================
# 10.2 줄 단위로 파일 쓰기/읽기
#===============================================================================

lines = ['first line\n', 'second line\n', 'third line\n']
f = open('t2.txt', 'w')
f.writelines(lines)
f.write(''.join(lines))
f.close()

with open('t2.txt') as f:
	print(len(f.read()))
	#68

import os
print(os.path.getsize('t2.txt'))
#68 윈도우에서는 더 크게 나올 것임.
print(repr(os.linesep))
#'\n' 윈도우에서는 '\r\n'
#파이썬은 '\r\n'을 '\n'으로 인식 후 파일 처리를 함.

#===============================================================================
# 10.3 파일에서 원하는 만큼의 문자 읽기
#===============================================================================

with open('t2.txt') as f:
	print(repr(f.read(10)))
	#'first line'
	print(repr(f.read(10)))
	#'\nsecond li'

#===============================================================================
# 10.4 이진 파일 쓰기/읽기
#===============================================================================

with open('t1.bin', 'wb') as f:
	#f.write('abcd')
	#TypeError: 'str' does not support the buffer interface
	f.write('abcd'.encode())
	f.write(b'efgh')

with open('t1.bin', 'rb') as f:
	b = f.read(5)
	print(b)
	#b'abcde'
	print(b.decode())
	#abcde
	print(f.readline())
	#b'fgh'

#===============================================================================
# 10.5 파일 처리 모드 311p
#===============================================================================

#===============================================================================
# 10.6 임의 접근 파일
#===============================================================================

with open('t.txt', 'wb+') as f:
	s = b'0123456789abcdef'
	print(f.write(s))
	#16
	print(f.seek(5))
	#5
	print(f.tell())
	#5
	print(f.read(1))
	#b'5'
	print(f.seek(2, os.SEEK_CUR))
	#8
	print(f.seek(-3, os.SEEK_END))
	#13
	print(f.read(1))
	#b'd'

#===============================================================================
# 10.7 파일 객체의 메소드와 속성
#===============================================================================

# http://docs.python.org/3.3/library/io.html#i-o-base-classes

#===============================================================================
# 10.8 파일 입출력 예제
#===============================================================================

#===============================================================================
# 10.9 표준 입출력 방향의 전환
#===============================================================================

#print('abcde', file=파일변수)

#------------------------------------------------------------------------------ 
# 표준 출력을 문자열로 하기
import io
# f = io.StringIO()
with io.StringIO() as f:
	print('hello', end=' ', file=f)
	print('world', file=f)
	print(f.getvalue())
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 문자열을 파일 객체처럼 읽기
s = '''
Python’s standard library is very extensive,
offering a wide range of facilities as indicated by the long table of contents listed below.
The library contains built-in modules (written in C) that provide access to system functionality
such as file I/O that would otherwise be inaccessible to Python programmers,
as well as modules written in Python that provide standardized solutions
for many problems that occur in everyday programming.
Some of these modules are explicitly designed to encourage and enhance the portability of Python programs
by abstracting away platform-specifics into platform-neutral APIs.
'''
with io.StringIO(s) as f:
	print(f.read(6))
	f.seek(10)
	print(f.read(20))
	print(f.readline(), end='')
	print(f.readlines())
#------------------------------------------------------------------------------ 

#===============================================================================
# 10.10 지속 모듈 : 파이썬 객체를 파일에 저장하는 기법 318p
#===============================================================================

# dbm : http://docs.python.org/3.3/library/dbm.html#module-dbm
# pickle : http://docs.python.org/3.3/library/pickle.html?#pickle-python-object-serialization
# marshal : http://docs.python.org/3.3/library/marshal.html#module-marshal
# shelve : http://docs.python.org/3.3/library/shelve.html#module-shelve