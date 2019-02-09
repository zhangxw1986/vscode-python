#高级特性--切片

li = []
n = 1
while n <100:
    li.append(n)
    n = n + 2
# print(li)

first3 = li[0:3]
print(first3)
print(li[-3:-1])
print(li[-3:])

ra = list(range(100))
print(ra)
print(ra[:10])
print(ra[-10:])
print(ra[:10:2])
print(ra[::5])