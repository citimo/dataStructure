from random import random
# x**n(modp)的递归定义
def modexp(x, n, p):
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n//2, p)
    if n % 2 != 0:
        tmp = (tmp * x) % p
    return tmp

# 欧几里得算法,求两个数的最大公因数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 扩展欧几里得算法,当且仅当m和x互素时x关于模m才有逆元,互素是指gcd(m,x)=1
def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)

# 求模m下的逆元
def mod_inverse(x, m):
    g, a, b = ext_gcd(x, m)

# RSA公钥加密算法
def RSAgenKeys(p, q):
    n = p * q
    pqminus = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(pqminus, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pqminus, e)
    if b < 0:
        d = pqminus + b
    else:
        d = b
    return (e, d, n)

def RSAencrypt(m, e, n):
    chunks = toChunks(m, n.bit_length() // 8 * 2)
    encList = []
    for messChunk in chunks:
        c = modexp(messChunk, e, n)
        encList.append(c)
    return encList

def RSAdecrypt(chunkList, d, n):
    rList = []
    for c in chunkList:
        m = modexp(c, d, n)
        rList.append(m)
    return chunksToPlain(rList, n.bit_length() // 8 * 2)

# 将字符串转换为数字块列表
def toChunks(m, chunkSize):
    byteMess = bytes(m, 'utf-8')
    hexString = ''
    for b in byteMess:
        hexString = hexString + ("%02x" % b)
    
    numChunks = len(hexString) // chunkSize
    chunkList = []
    for i in range(0, numChunks*chunkSize+1, chunkSize):
        chunkList.append(hexString[i:i+chunkSize])
    chunkList = [eval('0x'+x) for x in chunkList if x]
    return chunkList

def chunksToPlain(clist, chunkSize):
    hexList = []
    for c in clist:
        hexString = hex(c)[2:]
        clen = len(hexString)
        hexList.append('0' * ((chunkSize - clen) % 2) + hexString)

    hstring = "".join(hexList)
    messArray = bytearray.fromhex(hstring)
    return messArray.decode('utf-8')
