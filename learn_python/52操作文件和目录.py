# -*- coding: utf-8 -*-
import os
import io
import sys
import shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
print('系统类型：',os.name)
# print('环境变量：',os.environ.get('PATH'))


#(1)操作文件和目录的函数一部分在os中，一部分放在os.path模块中。
#(1.1)查看目录
print(os.path.abspath('.'))
#(1.2)创建新目录/删除目录
print(os.path.join('d:\\vscode-python','testdir'))
# os.mkdir(os.path.join('d:\\vscode-python','testdir'))
# os.rmdir(os.path.join('d:\\vscode-python','testdir'))

print(os.path.splitext('d:\\vscode-python\\learn_python\\46调试.py'))

#(1.3)文件重命名，删掉文件
# print(os.rename('hello.py','hello.txt'))
# os.remove('hello.py')

#(1.4)复制文件利用shutil模块的copyfile()函数

#(1.5)利用python的特性来过滤文件，列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出当前目录下所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])