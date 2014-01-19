# -*- coding:utf-8 -*-
"""
3) 파일 읽고 쓰기

	파일 생성하기

다음을 에디터로 작성해서 실행해 보면 프로그램을 실행한 디렉토리에 새로운 파일이 하나 생성되는 것을 확인할 수 있다.
"""

	# open()

f = open("newfile", 'w') 
f.close()
"""

	파일열기모드		설명
		r		읽기모드 - 파일을 읽기만 할 때 사용
		w		쓰기모드 - 파일에 쓸 때 사용
		a		추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
""""""

	파일을 쓰기 모드로 열어서 출력값 적기
"""

	# f.write()

f = open("newfile", 'w')

for i in range(1, 11): 
	data = "%d 번째 줄입니다.\n" % i 
	f.write(data) 

f.close()
"""

	파일을 읽는 여러가지 방법

	첫 번째 방법 : f.readline()
"""

	# f.readline()
	
f = open("newfile", 'r') 
line = f.readline() # 첫 줄 read
print(line)
f.close()
"""
	만약 모든 라인을 읽어서 화면에 출력하고 싶다면 다음과 같은 프로그램을 작성해야 한다.
"""
f = open("newfile", 'r')

while 1: 
	line = f.readline()
	if not line: break 
	print(line, end='')

f.close()
print()
"""

	두 번째 방법 : f.readlines()
"""

	# f.readlines()

f = open("newfile", 'r') 
lines = f.readlines() # 리스트로 반환

for line in lines: 
	print(line, end='')

f.close()
print()
"""
	[“1 번째 줄입니다.”,“2 번째 줄입니다.”, , , “10 번째 줄입니다.”]
""""""

	세 번째 방법 : f.read()

"""

	# f.read()

f = open("newfile", 'r') 
data = f.read()

print(data, end='') 

f.close()
print()
"""
	f.read()는 파일을 전부 읽은 문자열을 돌려준다. 따라서 위의 예의 data는 파일의 전체내용이다.

""""""

	파일에 새로운 내용 추가하기
"""
f = open("newfile",'a')

for i in range(11, 20): 
	data = "%d번째 줄입니다.\n" % i 
	f.write(data) 

f.close()
"""

		[참고] tell과 seek
	
	파일객체 관련 함수로 ‘tell’과 ‘seek’도 빼놓을 수 없다. ‘tell’은 지금 현재 파일 포인터의 위치를 반환하고,
	seek은 지정하는 곳으로 포인터의 위치를 변화시킬 수 있는 파일객체 관련 함수이다.
	파일 포인터란 파일의 현재 위치를 가리키는 말이다.
	
	대화형 인터프리터를 실행시키고 다음을 따라해 보자.
	(아래 tell과 seek예제는 유닉스에서 실행해 보시기 바랍니다. 윈도우즈에서는 tell() 값이 조금 다르게 나올 수 있습니다.
	참고: File Objects)
"""
f = open("test", 'w') 
f.write("this is one line\n") 
f.write("two line\n") 
f.write("three line\n") 
f.close()
"""
우선 test.txt라는 파일을 쓰기 모드로 열어서 파일 객체를 생성한후 write함수를 이용하여
총 세 개의 줄을 test.txt파일에 입력하고 파일 객체를 닫는다.
"""

	# f.tell()

f = open("test", 'r') 
print(f.tell())
"""
0
처음에 파일을 읽기 모드로 열었고, 그 파일 포인터 값을 알기 위해서 tell을 호출하였다.
물론 파일의 맨 처음이기 때문에 0을 반환했다.
"""
print(f.readline(), end='')
print(f.tell()) 
"""
17
다음에 한 줄을 읽는다. 그 다음의 파일 포인터는 그 줄의 바이트 수만큼 포인터가 증가한다.
따라서 다시 tell을 호출했을 때 17이 된 것이다.
"""
print(f.readline(), end='')
print(f.tell()) 
print()
"""
26
마찬가지로 다시 한 줄을 읽었더니 파일 포인터의 위치는 26이 되었다.
""""""

"""

	# f.seek()

f.seek(0)
print(f.readline(), end='')
print()
"""
	파일 포인터의 값을 변화시키기 위해서 seek를 사용하였다.
	f.seek(0)는 파일 포인터의 위치를 0으로 하라는 것이다.
	따라서 다음에 다시 한 줄을 읽었을 때는 그 파일의 맨 처음 줄을 읽게 되는 것이다.

""""""

	sys모듈 입력
"""

	# import sys (sys1.py) 

import sys

args = sys.argv[1:] 
for i in args: 
	print(i)
print()
# argv[0] : 파일 이름, argv[1]부터 인수
"""
	C:/Python>python sys1.py aaa bbb ccc
	다음과 같은 결과 값을 볼 수 있을 것이다.
	
	결과값:
	aaa
	bbb
	ccc
	sys모듈의 argv는 명령창에서 입력한 인수들의 리스트를 나타낸다.
	즉, argv[0]는 파일 이름인 sys1.py가 되고
	argv[1]부터는 뒤에 따라오는 인수들이 차례로 argv의 요소가 된다.
	위의 예는 입력받은 인수들을 for문을 이용해 차례대로 하나씩 출력하는 예이다.

위의 예를 이용해서 간단한 스크립트를 하나 만들어 보자.
"""
#import sys
args = sys.argv[1:]
for i in args: 
	print(i.upper(), end=' ')
print()
"""
C:/Python> python sys2.py life is too short, you need python
결과값:

LIFE IS TOO SHORT, YOU NEED PYTHON
"""