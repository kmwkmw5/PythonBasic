#===============================================================================
# 제 12 장 모듈과 패키지
#===============================================================================

#===============================================================================
# 12.1 모듈
#===============================================================================

#------------------------------------------------------------------------------ 
# 파이썬(*.py, *.pyc, *.pyo), C, Fortran(*.pyd)
# 표준 모듈, 사용자 생성 모듈, 서드 파티 모듈
# 자격 변수, 무자격 변수
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 모듈 검색 경로
import sys
print(sys.path)
#['/home/miki29/workspace/PythonBasic/Bible/Chapter', '/home/miki29/workspace/PythonBasic',
#'/usr/local/lib/python33.zip', '/usr/local/lib/python3.3', '/usr/local/lib/python3.3/plat-linux',
#'/usr/local/lib/python3.3/lib-dynload', '/usr/local/lib/python3.3/site-packages']
sys.path.append('/var/www')
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 절대 가져오기
import math
from math import sin, cos, pi
from math import *
import math as mt
from re import sub as substitute
from re import sub as sub1, subn as sub2
from tkinter import (Tk, Frame, Button, Entry, Canvas, Text,
						LEFT, DISABLED, NORMAL, RIDGE, END)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# __name__ 변수

import math
print(math.__name__)
#math

# 최상위 모듈에서는 __main__을 출력(최상위인지 아닌지 확인할 수 있음)
print(__name__)
#__main__

if __name__ == '__main__':
	print('메인')
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 문자열로 표현된 모듈을 가져오기
modulename = 're'
re = __import__(modulename)
print(re)
#<module 're' from 'C:\\Python33\\lib\\re.py'>
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 모듈의 공유 373p
# 모듈의 재적재
import math
import imp
imp.reload(math)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 함수나 클래스가 속한 모듈 알아내기

# 한 번이라도 가져온 모든 모듈은 sys.modules 변수에 남아있다.(미리 로드되어 있는 모듈이 많다.)
import sys
print(type(sys.modules))
#<class 'dict'>
print('\n'.join(sys.modules.keys()))
#zipimport
#weakref
#_locale
#tkinter._fix
#... 생략

# sys.modules 변수에서 모듈을 사용하는 것도 가능
heapq = sys.modules['heapq']
print(heapq)
#<module 'heapq' from 'C:\\Python33\\lib\\heapq.py'>
print(heapq.tee([1,2,3]))
#(<itertools._tee object at 0x0000000002950808>, <itertools._tee object at 0x00000000028478C8>)

# sys.modules[__name__]
current_module = sys.modules[__name__]
print(current_module)
#<module '__main__' from 'C:\\App\\PythonBasic\\Bible\\Chapter\\chap12_module_package.py'>
a = 1
print(getattr(current_module, 'a'))
print(current_module.a)
#1

# __module__ 속성
from math import sin
print(sin.__module__)
#math
from cmd import Cmd
print(Cmd.__module__)
#cmd

def foo():
	pass
print(foo.__module__)
#__main__
#------------------------------------------------------------------------------ 

#===============================================================================
# 12.2 패키지
#===============================================================================




























