# 骑士周游
# 来构建n*n棋盘对应的完整图
from Graph import Graph, Vertex
def knightGraph(bdSize):
    # 创建一个图
    ktGraph = Graph()
    # 遍历棋盘每一行
    for row in range(bdSize):
        # 遍历每一行每一列
        for col in range(bdSize):
            # 获取当前节点的ID
            nodeID = posToNodeId(row, col, bdSize)
            # 获取当前节点可以移动的位置
            newPositions = genLegalMoves(row, col, bdSize)
            # 遍历每一个可以移动的位置
            for e in newPositions:
                # 获取每一个可以移动位置的ID
                nid = posToNodeId(e[0], e[1])
                # 添加边
                ktGraph.addEdge(nodeID, nid)
    # 返回完整的图
    return ktGraph

# 生成合法的移动
def genLegalMoves(x, y, bdSize, depth=0, maxDepth=1000):
    # 检查递归深度
    if depth > maxDepth:
        return []

    # 初始化新的移动列表
    newMoves = []
    # 定义移动偏移量
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    # 遍历偏移量
    for i in moveOffsets:
        # 计算新的x坐标
        newX = x + i[0] 
        # 计算新的y坐标
        newY = y + i[1]
        # 判断新的坐标是否合法
        if genLegalMoves(newX, newY, bdSize, depth+1, maxDepth):
            # 合法则添加到新的移动列表中
            newMoves.append((newX, newY))
    # 返回新的移动列表
    return newMoves


# 判断坐标是否合法
def legalCoord(x, bdSize):
    # 判断x坐标是否大于等于0且小于bdSize
    if x >= 0 and x < bdSize:
        # 合法则返回True
        return True
    else:
        # 不合法则返回False
        return False

# 将坐标转换为节点id
def posToNodeId(x, y, bdSize):
    # 返回x*bdSize + y
    return x * bdSize + y

# 定义一个函数knightTour，用于实现骑士游走，参数n表示当前的步数，path表示当前的路径，u表示当前的节点，limit表示最大的步数
def knightTour(n, path, u, limit):
    # 设置当前节点的颜色为灰色
    u.setColor('gray')
    # 将当前节点添加到路径中
    path.append(u)
    # 如果当前步数小于最大步数，则进行下一步
    if n < limit:
        # 获取当前节点的连接节点列表
        nbrList = orderByAvail(u)   # nbrList = list(u.getConnections())
        # 初始化计数器i
        i = 0
        # 初始化done为False
        done = False
        # 遍历连接节点列表
        while i < len(nbrList) and not done:
            # 如果连接节点颜色为白色，则进行下一步递归
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            # 计数器i加1
            i = i + 1
        # 如果done为False，则表示无法完成骑士游走，将当前节点在路径中的颜色设置为白色，并返回done
        if not done:
            path.pop()
            u.setColor('white')
    # 如果done为True，则表示完成骑士游走，返回done
    else:
        done = True
    # 返回done
    return done

# 启发式技术，Warnsdorff 算法
# 定义一个函数orderByAvail，参数为n，用于按照可用节点数量排序
def orderByAvail(n):
    # 定义一个空列表resList，用于存放排序后的节点
    resList = []
    # 遍历n的连接节点
    for v in n.getConnections():
        # 如果当前节点的颜色为白色
        if v.getColor() == 'white':
            # 定义一个变量c，用于记录当前节点可用的连接节点数量
            c = 0
            # 遍历当前节点的连接节点
            for w in v.getConnections():
                # 如果当前连接节点的颜色为白色
                if w.getColor() == 'white':
                    # c加1
                    c = c + 1
            # 将当前节点可用连接节点数量和当前节点添加到resList中
            resList.append((c, v))
    # 对resList进行排序，按照可用节点数量排序
    resList.sort(key=lambda x: x[0])
    # 返回resList中按照可用节点数量排序后的节点
    return  [y[1] for y in resList]
