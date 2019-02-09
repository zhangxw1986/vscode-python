#定义函数

import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx,ny

r = move(1,1,30,math.pi/6)
print("你现在的位置是：",r )