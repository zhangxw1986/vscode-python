#导入包下的模块module，包下需要有__init__.py，才会将此目录识别为包
import myinit.module as mm

import os,sys

print('test path ',sys.argv[0])
dirname,filename = os.path.split(os.path.abspath(sys.argv[0]))

print('running from ',dirname)
print('file is ' ,filename)

print(__file__)


