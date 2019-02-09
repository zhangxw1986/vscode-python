#循环 for和while两种

li = ['bob','steve','clark']
for name in li:
    print(name)

list1 = list(range(10))
sum = 0
for i in list1:
    sum += i 
print('和是',sum)


sum1 = 0
n = 99 
while n>0:
    sum1 += n
    n= n - 2

print('和是',sum1)