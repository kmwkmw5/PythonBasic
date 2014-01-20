# -*- coding:utf-8 -*-
"""
5) 외장함수

"""""""""""""""""""""
####################
import sys
####################
"""""""""""""""""""""

	명령행에서 인수를 전달(sys.argv)

"""
print(sys.argv)
print('')
"""

	강제 스크립트 종료법(sys.exit)

"""
#sys.exit()
"""

	자신이 만든 모듈 불러서 쓰기(sys.path)

"""
sys.path.append('/var/www')
print(sys.path)
"""

"""""""""""""""""""""
####################
import pickle
####################
"""""""""""""""""""""

	객체를 그 상태 그대로 파일에 저장하고 싶을 때(pickle)

"""
f = open("test", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("test", 'rb')
data = pickle.load(f)
print(data)
f.close()
print('')
# 딕셔너리 객체를 이용하였지만 어떤 자료형이든지 상관없다.
"""

"""""""""""""""""""""
####################
#import io			# ver3
import StringIO	# ver2
####################
"""""""""""""""""""""

	파일 흉내내기(StringIO) : StringIO는 파일처럼 취급되는 객체를 만들어낸다.
							  단 실제 파일객체는 아니고 흉내를 낼 뿐이다.
	
"""
#f = io.StringIO()	# ver3
f = StringIO.StringIO()
f.write("life is too short")
value = f.getvalue()
print(value)
f.close()
print('')
"""

"""""""""""""""""""""
####################
import os
####################
"""""""""""""""""""""

	현재 내 시스템 환경변수값을 알고싶을 때는? (os.environ)

"""
print(os.environ)
print(os.environ['PATH'])
print('')
"""

	디렉토리에 대한 것들(os.chdir, os.getcwd)

"""
# 현재 디렉토리의 위치 변경
#os.chdir('/var/www')

# 현재 디렉토리의 위치 출력
print(os.getcwd())
print('')
"""

	시스템 명령(os.system, os.popen)

"""
# 시스템 명령어 사용
print(os.system('ls -al'))

# 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일객체로 반환
files = os.popen('dir')
print(files.read())
files.close()
"""
기타 유용한 os 관련 함수
		함수					설명
os.mkdir(디렉토리)		디렉토리를 생성한다.
os.rmdir(디렉토리)		디렉토리를 삭제한다.단, 디렉토리가 비어있어야 삭제가 가능하다.
os.unlink(파일)		파일을 지운다.
os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.


"""""""""""""""""""""
####################
import shutil
####################
"""""""""""""""""""""

	파일 복사(shutil)
	shutil.copy(src, dst)

"""
shutil.copy('test', 'copy')
"""

"""""""""""""""""""""
####################
import glob
####################
"""""""""""""""""""""

	디렉토리에 있는 파일들을 리스트로 만들려면 (glob)
	glob(pathname) *, ?등의 메타문자를 써서 원하는 파일만을 읽어들일 수도 있다.
	
"""
print(glob.glob("/var/www/*"))
print('')
"""

"""""""""""""""""""""
####################
import tempfile
####################
"""""""""""""""""""""

	임시파일 (tempfile)
	tempfile.mktemp()는 중복되지 않는 임시파일의 이름을 만들어서 돌려준다.
	
	tempfile.TemporaryFile()은 임시적인 저장공간으로 사용될 파일 객체를 돌려준다.
	기본적으로 w+b 의 모드를 갖는다. 이 파일객체는 f.close()가 호출될 때 자동으로 사라지게 된다.

"""
# mktemp()
filename = tempfile.mktemp()
print(filename)

# TemporaryFile()
f = tempfile.TemporaryFile()
f.close()
print('')
"""

"""""""""""""""""""""
####################
import time
####################
"""""""""""""""""""""

	time.time : UTC(Universal Time Coordinated 협정 세계 표준시)를 이용하여
				  현재의 시간을 실수형태로 반환하여 주는 함수이다.
				  1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려준다.

"""
print(time.time())
"""

	time.localtime : time.time()에 의해서 반환된 실수값을 이용해서
						년도, 달, 월, 시, 분, 초,.. 의 형태로 바꾸어 주는 함수이다.

"""
print(time.localtime(time.time()))
"""

	time.asctime : 위의 time.localtime에 의해서 반환된 터플 형태의 값을 인수로 받아서
					 알아보기 쉬운 날짜와 시간 형태의 값을 반환하여 주는 함수이다.
					 가장 자주 사용되는 시간관련 함수이다.

"""
print(time.asctime(time.localtime(time.time())))
"""

	time.ctime : time.asctime을 쉽게 쓰기 위함

"""
print(time.ctime())
"""

	time.strftime('출력할 형식포맷코드', time.localtime(time.time())) 
		strftime 함수는 시간에 관계된 것을 세밀하게 표현할 수 있는 여러 가지 포맷코드를 제공해 준다.

포맷코드			설명								예(조금 이상한듯)
%a		요일 줄임말							Mon
%A		요일									Monday
%b		달 줄임말							Jan
%B		달									January
%c		날짜와 시간을 출력함					Mon Jan 20 21:05:23 2014
%d		날(day)								[00,31]
%H		시간(hour)-24시간 출력 형태			[00,23]
%I		시간(hour)-12시간 출력 형태			[01,12]
%j		1년 중 누적 날짜						[001,366]
%m		달									[01,12]
%M		분									[01,59]
%p		AM or PM							AM
%S		초									[00,61]
%U		1년 중 누적 주-일요일을 시작으로		[00,53]
%w		숫자로 된 요일						[0(일요일),6]
%W		1년 중 누적 주-월요일을 시작으로		[00,53]
%x		현재 설정된 로케일에 기반한 날짜 출력	06/01/01
%X		현재 설정된 로케일에 기반한 시간 출력	17:22:21
%Y		년도 출력							2001
%Z		시간대 출력							대한민국 표준시
%%		문자									%
%y		세기부분을 제외한 년도 출력			01
"""
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print('')
"""

	time.sleep : 보통 루프 안에서 많이 쓰이는데 일정한 시간 간격을 주기 위해서 주로 쓰이게 된다.

"""
for i in range(3):
	print(i)
	time.sleep(0.1)
"""

"""""""""""""""""""""
####################
import calendar
####################
"""""""""""""""""""""

	파이썬에서 달력쓰기(calendar)
	
"""
# 한 해의 달력 모두 출력
print(calendar.calendar(2014))
#print(calendar.prcal(2014))	# 개행문자 등이 조금씩 다른듯

# 한 월의 달력만 출력
print(calendar.prmonth(2014, 1))

# 무슨 요일인지 출력(0:월요일 ~ 6:일요일
print(calendar.weekday(2014, 1, 19))

# (1일이 무슨 요일인지, 몇 일까지 있는지)
print(calendar.monthrange(2014,1))
print('')
"""

"""""""""""""""""""""
####################
import random
####################
"""""""""""""""""""""

	난수 발생시키기 (random)

"""
# 0 ~ 1.0 사이의 수
print(random.random())

# 1 ~ 10 사이의 수
print(random.randint(1,10))
"""

"""""""""""""""""""""
####################
#import _thread	# ver3
import thread		# ver2
####################
"""""""""""""""""""""

	파이썬에서의 쓰레드 (_thread)
	thread.start_new_thread(함수, (인자))
"""
'''
def say(msg):
	while 1:
		print(msg)
		time.sleep(1)

thread.start_new_thread(say, ('you',))
thread.start_new_thread(say, ('need',))
thread.start_new_thread(say, ('python',))
for i in range(100):
	print(i)
	time.sleep(0.1)
'''
"""

"""""""""""""""""""""
####################
import webbrowser
####################
"""""""""""""""""""""

	웹브라우저 실행시키기 (webbrowser)

"""
# 실행중인 웹브라우저에서 이동
webbrowser.open("http://www.google.com")
# 새로운 창에서 이동???
webbrowser.open_new("http://www.google.com")