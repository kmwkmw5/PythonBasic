# chap05_list 5.10
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