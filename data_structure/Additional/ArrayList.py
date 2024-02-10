# 使用数组实现列表
class ArrayList:
    def __init__(self):
        self.sizeExponent = 0
        self.maxSize = 0
        self.lastIndex = 0
        self.myArray = []
    
    def append(self, val):
        if self.lastIndex >= self.maxSize - 1:
            self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1
    
    def __resize(self):
        newsize = 2 ** self.sizeExponent
        newarray = [0] * newsize
        for i in range(self.maxSize):
            newarray[i] = self.myArray[i]
        self.maxSize = newsize
        self.myArray = newarray
        self.sizeExponent += 1
    
    def __getitem__(self, idx):
        if idx < self.lastIndex:
            return self.myArray[idx]
        else:
            raise LookupError("Index out of bounds")
    
    def __setitem__(self, idx, val):
        if idx < self.lastIndex:
            self.myArray[idx] = val
        else:
            raise LookupError("Index out of bounds")
    
    def insert(self, idx, val):
        if self.lastIndex >= self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex, idx-1, -1):
            self.myArray[i+1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[idx] = val
    
    def pop(self, idx=None):
        if idx is None:
            idx = self.lastIndex - 1
        if idx < 0 or idx >= self.lastIndex:
            raise LookupError("Index out of bounds")
        val = self.myArray[idx]
        for i in range(idx, self.lastIndex - 1):
            self.myArray[i] = self.myArray[i+1]
        self.lastIndex -= 1
        return val
    
    def __delitem__(self, idx):
        self.pop(idx)
    
    def index(self, val):
        for i in range(self.lastIndex):
            if self.myArray[i] == val:
                return i
        raise ValueError("Value not found")
    
    def __iter__(self):
        self.__iter_index = 0
        return self
    
    def __next__(self):
        if self.__iter_index < self.lastIndex:
            val = self.myArray[self.__iter_index]
            self.__iter_index += 1
            return val
        else:
            raise StopIteration
    