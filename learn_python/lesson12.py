#使用dict和set

d = {'mike':93,'job':12,'jones':100}
print(d['mike'])
d.update({'kane':29})
print(d)
d.popitem()
print(d)



s = set()
s.add(1)
s.add(2)
print(s)
s2 = {2,3,4,56,7}
print(s | s2)
s.remove(1)
print(s)

