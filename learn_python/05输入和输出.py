import sys,io

#改变标准输出的默认编码,windows需要加这个
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


#input()和print()是命令行界面下最基本的输入和输出，

name = input("请输入你的姓名：")
print("hello,%s" % name)