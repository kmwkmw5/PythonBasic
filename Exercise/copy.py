# -*- coding:utf-8 -*-
import sys;

try:
	originFileName = sys.argv[1];
	copyFileName = sys.argv[2];
except:
	print('Usage: python copy.py originFileName copyFileName')
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