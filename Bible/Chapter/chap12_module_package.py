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
























