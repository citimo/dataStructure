# 宽度优先搜索
from Graph import Graph, Vertex
from Queue.Queue1 import Queue
# 定义BFS函数，参数为图g和起点start
def bfs(g,start):
    # 初始化起点距离为0，前驱节点为None
    start.setDistance(0)
    start.setPred(None)
    # 创建一个队列
    vertQuene = Queue()
    # 将起点加入队列
    vertQuene.enqueue(start)
    # 当队列不为空时，循环
    while(vertQuene.size() > 0):
        # 从队列中取出一个节点
        currentVert = vertQuene.dequeue()
        # 遍历该节点的所有连接节点
        for nbr in currentVert.getConnections():
            # 如果连接节点颜色为white，则将其颜色改为gray，距离改为当前节点距离+1，前驱节点改为当前节点
            if (nbr.getColor() == 'while'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                # 将连接节点加入队列
                vertQuene.enqueue(nbr)
        # 当前节点颜色改为black
        currentVert.setColor('black')

# 定义遍历函数，参数为y
def traverse(y):
    # 将y赋值给x
    x = y
    # 当x的前驱节点不为空时，循环
    while (x.getPred()):
        # 打印x的id
        print(x.getId())
        # 将x赋值为前驱节点
        x = x.getPred()
    # 打印x的id
    print(x.getId())

# 调用BFS函数，遍历图g中起点为g.getVertex('sage')的节点
g = Graph()
traverse(g.getVertex('sage'))