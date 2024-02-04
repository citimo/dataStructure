# 为整数构建简单的散列函数
def hash(alist, sizeoftable):
    hash_value = []
    for pos in range(alist):
        newhashvalue = pos % sizeoftable
        hash_value.append(newhashvalue)
    return hash_value
