# -*- coding: utf-8 -*-

import sys

from io import BytesIO

f = BytesIO()
f.write('中文')
print(f.getvalue())