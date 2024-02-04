# 创建 HashTable 类，以此实现映射抽象数据类型，采用链接法处理冲突
class HashTable:
    def __init__(self, size=11):
        self.size = size    # 初始化哈希表，指定大小，默认为11
        self.table = [None] * self.size # 表格初始化为指定大小的空列表

    def hash_function(self, key):
        return key % self.size  # 简单的哈希函数，通过对键取余得到槽位的索引

    def put(self, key, data):
        index = self.hash_function(key) # 插入键值对到哈希表
        if self.table[index] is None:
            # 如果槽位为空，创建一个包含键值对的元组列表
            self.table[index] = [(key, data)]   
        else:
            # 如果槽位不为空，遍历链表
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # 如果键已存在，更新对应的数据
                    self.table[index][i] = (key, data)
                    return
            # 如果键不存在，将新的键值对添加到链表中
            self.table[index].append((key, data))

    def get(self, key):
        # 通过键查找对应的值
        index = self.hash_function(key)
        if self.table[index] is not None:
            # 遍历链表查找键
            for existing_key, data in self.table[index]:
                if existing_key == key:
                    return data
        return None

    def __getitem__(self, key):
        # 使用方括号操作符进行读取操作
        return self.get(key)

    def __setitem__(self, key, data):
        # 使用方括号操作符进行写入操作
        self.put(key, data)

# Example Usage
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
    print(H.table)
    print(H[20])  # 输出: chicken
    H[20] = 'duck'
    print(H[20])  # 输出: duck
    print(H[99])  # 输出: None
