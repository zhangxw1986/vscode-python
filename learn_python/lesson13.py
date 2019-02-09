#调用函数

a = abs(-11)
print(a)

print(max(1,2,3,4))

def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if(x>0):
        return x
    else:
        return -x

