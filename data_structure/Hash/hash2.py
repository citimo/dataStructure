# 为字符串构建简单的散列函数
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    
    return sum % tablesize

# 在考虑权重的同时，利用序数值计算字符串的散列值
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * (pos + 1)
    
    return sum % tablesize

if __name__ == '__main__':
    print(hash('cat', 11))
    