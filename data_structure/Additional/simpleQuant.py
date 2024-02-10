# 颜色量化算法
import sys
import os
from PIL import Image

def simpleQuant():
    im = Image.open('bubbles.jpg')
    width, height = im.size
    for row in range(height):
        for col in range(width):
            r, g, b = im.getpixel((col, row))
            r = (r // 36) * 36
            g = (g // 42) * 42
            b = (b // 42) * 42
            im.putpixel((col, row), (r, g, b))
    im.show()

# 调用函数进行简单的量化操作
simpleQuant()
