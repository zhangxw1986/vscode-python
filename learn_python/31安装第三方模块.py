from PIL import Image
import sys
import os



im = Image.open(r'D:\vscode-python\learn_python\images\qe3.JPG')
print(im.format,im.size)
im.thumbnail((200,100))
im.save(r'D:\vscode-python\learn_python\images\qe3.JPG','JPEG')


print(sys.path)