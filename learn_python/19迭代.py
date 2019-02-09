#迭代
from collections import Iterable
d = {"bc":"999","retdesc":"交易成功","apdex":100.0,"rcvnds":[],"bussc":True,"lastMenuCode":"","syssc":True,"appname":"P2-员工渠道整合平台","sndnd":"102001","@version":"1","oriex1":"undefined","glb":"1020017121542671932751725","apgrp":"YGQGL_AP_YQ","sndndc":False,"seq":"0000000000","app":6,"ret":"000000000000","st":1542591032699,"proc":4,"svct":"000000","cost":4,"chn":"UNDEFINED","initc":"6","initnd":"102001","stall":False,"lastMenu":"","ap":"by12ygqglap2004","sndc":"6","tc":"a0332r100","@timestamp":"2018-11-19T10:59:00.000Z","nd":"102001","initndc":False}

for key in d:
    print(key)
for value in d.values():
    print(value)

for key,value in d.items():
    print(key,':',value)
print('============')
print('是否可迭代：',isinstance('abc',Iterable))
print('是否可迭代：',isinstance('(1,2,3)',Iterable))
