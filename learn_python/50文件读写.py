# -*- coding: utf-8 -*-
#第一行是保证文件直接在unix、linux、mac上直接执行；第二行注释表示使用UTF-8编码

'the first string'
#任何文件的第一个字符串，表示模块的文档注释
__author__ = 'zhangxw1986'
#表示作者

#以上就是python模块的标准文件模板；接下来才是真正的文件

#（1）最原始的方法：
# f = open('/Volumes/public/vscode-python/test.py','r')
# print(f.read())
# f.close()
# print(f.read())

#（2）with语句可以自动调用close()方法：

with open('/Volumes/public/vscode-python/test.py','r') as f1:
  print(f1.read())


with open('/Volumes/public/vscode-python/file_test1.py','w') as f2:
  f2.write('Hello,world!')

