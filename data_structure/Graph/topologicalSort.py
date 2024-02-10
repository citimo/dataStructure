# 拓朴排序
def topologicalSort(graph):
    # 创建一个空列表来存储排序结果
    result = []
    
    # 创建一个字典用于记录每个节点的入度
    inDegree = {}
    for vertex in graph:
        inDegree[vertex] = 0
    
    # 计算每个节点的入度
    for vertex in graph:
        for neighbor in vertex.getConnections():
            inDegree[neighbor] += 1
    
    # 创建一个队列用于存储入度为 0 的节点
    queue = []
    for vertex in graph:
        if inDegree[vertex] == 0:
            queue.append(vertex)
    
    # 执行拓扑排序
    while queue:
        # 从队列中取出一个节点
        vertex = queue.pop(0)
        
        # 将节点添加到排序结果中
        result.append(vertex)
        
        # 更新与该节点相邻节点的入度
        for neighbor in vertex.getConnections():
            inDegree[neighbor] -= 1
            # 如果相邻节点的入度变为 0，则将其加入队列
            if inDegree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果结果中的节点数量与图中的节点数量不一致，说明图中存在环路，无法进行拓扑排序
    if len(result) != len(graph):
        raise ValueError("图中存在环路，无法进行拓扑排序")
    
    return result
