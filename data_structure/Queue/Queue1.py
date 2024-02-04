# 实现队列
class Queue():
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue('dog')
    q.enqueue(4)
    print(q.isEmpty())
    q.enqueue(True)
    print(q.size())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
