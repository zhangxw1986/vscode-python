from __future__ import print_function
import sys
import json
from datetime import datetime
filename = sys.argv[1]
day = int(sys.argv[2])
start_h = int(sys.argv[3])
start_m = int(sys.argv[4])
end_h = int(sys.argv[5])
end_m = int(sys.argv[6])

print('input filename: {}'.format(filename))
print('input day: {}'.format(day))
print('{}:{}-{}:{}'.format(start_h,start_m,end_h,end_m))
ret_lines = []
# print('hello vscode')
with open(filename,'r') as f:
    for line in f:
        obj = json.loads(line)
        # print(obj)
        assert isinstance(obj['st'],int)
        if obj['tc'].lower() == 'a0332r100' \
            and datetime.fromtimestamp(obj['st'] // 1000) >= datetime(2018,11,day,start_h,start_m) \
            and datetime.fromtimestamp(obj['st'] // 1000) < datetime(2018,11,day,end_h,end_m):
                ret_lines.append(line)
                print(line)
print("length:{}".format(len(ret_lines)))
with open('201811{}_a0332r100_{}{}_{}{}.txt'.format(day,start_h,start_m,end_h,end_m),'w') as f:
    for line in ret_lines:
        print(line,file=f)


