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

#------------------------------------------------------------------------------ 
# __init__.py : 패키지 내의 초기화 스크립트(필수)

#__all__ : 가져오기를 할 모듈이나 패키지 이름들을 지정(폴더 정보)
#__all__ = ['Recognition', 'SignalProcessing', 'Synthesis']
#__version__ = '1.2'
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 상대 가져오기
# .(현재 폴더), ..(상위 폴더), ...(두 단계 상위 폴더)
#from . import Recognition
#from . import SignalProcessing
#from . import Synthesis
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# __main__.py
# python의 인수로 폴더나 zip 등을 지정할 수 있다.
# 이 때, __main__.py의 파일이 실행된다.
#------------------------------------------------------------------------------ 

#===============================================================================
# 12.3 프로그램 배포하기
#===============================================================================

#------------------------------------------------------------------------------ 
# setup.py
# from distutils.core import setup
# 
# setup(name="spam",
#         version="1.0",
#         description="setup test",
#         author="Lee, Gang Seong",
#         author_email="gslee0115@gmail.com",
#         url="http://pythonworld.net/",
# 
#         py_modules = ['A', 'B', 'mymath02'],			# 개별적인 모듈 지정
#         packages = ['Speech', 						# 패키지 포함
#             'Speech/Recognition', 
#             'Speech/SignalProcessing', 
#             'Speech/Synthesis'],
#         #package_dir={'Speech': 'Speech2'},			# 패키지명:폴더명(서로 다를 때)
#         package_data={'Speech': ['images/*.jpg']},	# 추가 패키지 데이터는 따로 지정
#         data_files=[('data', ['Speech/images/a1.jpg'])], # 패키지에 포함되지 않는 데이터 파일
# )
# data_files에서('설치경로', [파일목록]) 설치경로가 상대 경로이면 아래의 경로의 위치 기준
print(sys.prefix)
#/usr/local
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 배포판 만들기와 설치하기 382p
#------------------------------------------------------------------------------ 