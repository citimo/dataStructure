# 创建 HashTable 类，以此实现映射抽象数据类型，采用线性探测处理冲突
class HashTable:
    def __init__(self) -> None:
        self.size = 11  # 初始大小可以任意指定，但选用一个素数很重要
        self.slots = [None] * self.size # 存储键
        self.data = [None] * self.size  # 存储值
    
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data    # 替换
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # 替换
    
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]  # 更新 data 为相应的值
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20], H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(H[99])
    