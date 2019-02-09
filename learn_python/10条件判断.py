#条件判断

birth = input("请输出出生年份：")
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')