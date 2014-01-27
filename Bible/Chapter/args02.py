# chap05_list 5.10
# args02.py
import argparse

parser = argparse.ArgumentParser(description='fixed size argument list example')
parser.add_argument('size', nargs='*', type=int)

#args = parser.parse_args(['1024', '768'])
args = parser.parse_args();
print(args.size)
#python3 args02.py 222 333
#[222, 333]