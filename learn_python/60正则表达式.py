import re


#(1)re模块，match()判断正则表达式是否匹配字符串
test = '010-31211'

if re.match(r'^\d{3}\-\d{3,8}$',test):
    print('ok')
else:
    print('failed')


#(2)re模块，split()方法根据正则表达式切分字符串
s = 'a b  c         dd, ee'
s1 = s.split(' ')
print('split result is : ', s1)

s2 = re.split(r'[\s\,]+',s)
print('re  result is :', s2)

#(3)re模块，()用来对字符串进行分组
g = re.match(r'^(\d{3})-(\d{3,8})$',test)
print(g,g[0],g[1],g[2])

#(4)re模块，正则表达式默认采用贪婪匹配，如下：
f = re.match(r'(\d+)(0*)$','131200')
print(f,f.groups())

f1 = re.match(r'(\d+?)(0*)$','131200')
print(f1,f1.groups())

