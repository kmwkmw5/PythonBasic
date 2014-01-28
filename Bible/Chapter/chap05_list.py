#===============================================================================
# 제 5 장 리스트
#===============================================================================

#===============================================================================
# 5.1 리스트의 연산
#===============================================================================

#===============================================================================
# 5.2 중첩 리스트(Nested Lists)
#===============================================================================

#===============================================================================
# 5.3 리스트 메소드
# 스택 .append(data), .pop()
# 큐   .append(data), .pop(0)
#===============================================================================

# http://docs.python.org/3.3/tutorial/datastructures.html#more-on-lists
# http://docs.python.org/3.3/library/stdtypes.html#mutable-sequence-types

#===============================================================================
# 5.4 리스트에 튜플이나 리스트(복합 자료형)가 있을 때 반복 참조하기
#===============================================================================

lt = [('one', 1), ('two', 2), ('three', 3)]
for name, num in lt:
	print('name={:7} num={}'.format(name, num))
#name=one     num=1
#name=two     num=2
#name=three   num=3

#===============================================================================
# 5.5 리스트 정렬하기
# 메소드 .sort(), .reverse()
# 함수   sorted(), reversed()
#===============================================================================

# .sort() 메소드의 옵션(reverse, key)
L = 'Python is a Programming Language'.split()
L.sort()
print(L) # 대문자가 소문자보다 앞선다.
#['Language', 'Programming', 'Python', 'a', 'is']
L.sort(key = str.lower, reverse = True)
print(L)
#['Python', 'Programming', 'Language', 'is', 'a']

# key의 예제
L = [1,5,3,9,8,4,2]
L.sort(key = lambda a: (a%3, a))
print(L)
#[3, 9, 1, 4, 2, 5, 8]

#===============================================================================
# 5.6 리스트 내장(List Comprehension)
#===============================================================================

L = [k*k for k in range(10)]
print(L)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 중첩 리스트 내장
L = [[row + (i*3) for row in [10, 11, 12]] for i in [0, 1, 2]]
print(L)
#[[10, 11, 12], [13, 14, 15], [16, 17, 18]]

L = [[1 if col_idx == row_idx else 0 for col_idx in range(0,3)] for row_idx in range(0,3)]
print(L)
#[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# 발생자 내장
# []를 ()으로 바꿈.
# 발생자 객체가 생성되고 이는 반복자의 일종임

#===============================================================================
# 5.7 순환 참조 리스트
# Garbage Collection을 방해하므로 약한 참조(18장)을 권장
#===============================================================================

GNU = ['is Not Unix']
GNU.insert(0, GNU)
print(GNU)
#[[...], 'is Not Unix']

#===============================================================================
# 5.8 순차적인 정수 리스트 만들기(range)
#===============================================================================

#===============================================================================
# 5.9 지역적으로 사용 가능한 이름 리스트 얻기
#===============================================================================

print(dir())
#['__builtins__', '__doc__', '__name__', '__package__']
print(__name__)
#__main__
print(__builtins__)
#<module 'builtins' (built-in)>

import sys
print(dir(sys))
#['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
#'__package__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache',
#'_current_frames', '_debugmallocstats', '_getframe', '_home', '_mercurial',
#'_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix',
#'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright',
#'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval',
#'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile',
#'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace',
#'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'maxsize',
#'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache',
#'platform', 'prefix', 'setcheckinterval', 'setdlopenflags', 'setprofile',
#'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
#'thread_info', 'version', 'version_info', 'warnoptions']

#===============================================================================
# 5.10 명령줄 인수 처리
#===============================================================================

#------------------------------------------------------------------------------ 
# 고정 인수
#------------------------------------------------------------------------------ 


#------------------------------------------------------------------------------ 
# argparse
# args01.py
import argparse

parser = argparse.ArgumentParser(description = 'arguments example')

parser.add_argument('count', type = int)
parser.add_argument('units', type = float)
parser.add_argument('msg') # 기본 str

args = parser.parse_args()
print('count={} units={} msg={}'.format(args.count, args.units, args.msg))
print(type(args.count), type(args.units), type(args.msg))
#python3 args01.py 3 2.54 "my message"
#count=3 units=2.54 msg=my message
#<class 'int'> <class 'float'> <class 'str'>

#python3 args01.py 3 2.54
#usage: args01.py [-h] count units msg
#args01.py: error: the following arguments are required: msg

#python3 args01.py -h
#usage: args01.py [-h] count units msg
#
#arguments example
#
#positional arguments:
#  count
#  units
#  msg
#
#optional arguments:
#  -h, --help  show this help message and exit
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# nargs : 하나의 변수에 여러 인자 값을 리스트로 받음('*', '+', '?'를 사용할 수 있음)
# args02.py
import argparse

parser = argparse.ArgumentParser(description='fixed size argument list example')
parser.add_argument('size', nargs=2, type=int)

#args = parser.parse_args(['1024', '768'])
args = parser.parse_args();
print(args.size)
#python3 args02.py 222 333
#[222, 333]
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 옵션 처리 208p
#------------------------------------------------------------------------------ 

#===============================================================================
# 5.11 디렉터리의 파일 목록 얻기 212p
#===============================================================================