# 深度优先搜索
from Graph import Graph
# 定义DFSGraph类，继承自Graph类
class DFSGraph(Graph):
    # 初始化函数，调用父类的初始化函数
    def __init__(self):
        super().__init__()
        # 定义时间变量
        self.time = 0
    
    # 定义DFS函数，遍历图中的每一个顶点
    def dfs(self):
        # 遍历图中的每一个顶点，将其颜色设为白色，pred设为-1
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        # 遍历图中的每一个顶点，如果颜色为白色，则调用dfsVisit函数
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsVisit(aVertex)
    
    # 定义dfsVisit函数，传入一个顶点，将其颜色设为灰色，时间变量加1，发现时间设为当前时间变量，遍历该顶点的所有连接点，如果颜色为白色，则将其pred设为当前顶点，并调用dfsVisit函数，最后将颜色设为黑色，完成时间设为当前时间变量
    # 定义深度优先搜索函数
    def dfsvisit(self, startVertex):
        # 设置起点颜色为灰色
        startVertex.setColor('gray')
        # 搜索次数加1
        self.time += 1
        # 记录搜索起始时间
        startVertex.setDiscovery(self.time)
        # 遍历起点连接的点
        for nextVertex in startVertex.getConnections():
            # 如果连接点颜色为白色
            if nextVertex.getColor() == 'white':
                # 记录搜索路径
                nextVertex.setPred(startVertex)
                # 递归调用深度优先搜索函数
                self.dfsvisit(nextVertex)
        # 设置连接点颜色为黑色
        startVertex.setColor('black')
        # 搜索次数加1
        self.time += 1
        # 记录搜索结束时间
        startVertex.setFinish(self.time)
