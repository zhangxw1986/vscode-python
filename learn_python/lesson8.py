#字符串和编码 
#ord()将字符转换为整数编码表示， chr()将编码转换为对应的字符
print(ord("A"))
print(ord("中"))
print(chr(121))

# \uxxxx是unicode的写法，其中xxxx是一个十六进制的数字
print("\u4e2d\u6587")

print('中文'.encode('utf-8'))
print('ABC'.encode('utf-8'))
print('ABC'.encode('ASCII'))

print(b'\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x88'.decode('utf-8'))
print(len('中文'.encode('utf-8')))

print(len('ABC中'))   #len在字符串中表示字符数
print(len('ABC中'.encode("utf-8")))    #len在bytes中是表示 计算的字节数

print('ac %s' % '米兰')