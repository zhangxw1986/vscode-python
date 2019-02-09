import os

li = [d for d in os.listdir('.')]
print(li)

li1 = [d*d for d in range(1,11) if d%2 == 0]
print(li1)

li2 = [m+n for m in 'ABC' for n in 'XYZ']
print(li2)

L = ["IBM",'ORACLE','LENOVO','APPLE']
li3 = [s.lower() for s in L]
print(li3)