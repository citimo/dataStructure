# 将整数转换成以 2~16 为进制基数的字符串
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


# 栈帧：实现递归
from Stack.Stack1 import Stack
rStack = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr(n // base, base)
