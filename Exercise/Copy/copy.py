# -*- coding:utf-8 -*-
import sys;

def usage():
	print("""
Usage
======
python %s originFileName copyFileName
""" % (sys.argv[0]))


try:
	originFileName = sys.argv[1];
	copyFileName = sys.argv[2];
except:
	usage()
	exit()

try:
	originFile = open(originFileName, 'r')
except:
	print(originFileName + ' open error!')
	exit()
data = originFile.read();
originFile.close()

try:
	copyFile = open(copyFileName, 'w')
except:
	print(copyFileName + ' open error!')
	exit()
copyFile.write(data)
copyFile.close()