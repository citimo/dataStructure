# 传土豆模拟程序
from Queue1 import Queue
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        
        simqueue.dequeue()
        # print(simqueue.dequeue())
    
    return simqueue.dequeue()

if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))