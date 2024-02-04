# 十进制数转换为二进制数
from Stack1 import Stack
def divideBy2(decNumber):
    remstack = Stack()
    while remstack > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    
    return binString
