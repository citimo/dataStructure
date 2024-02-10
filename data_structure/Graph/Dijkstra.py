# Dijkstra算法,使用贪心策略求解单源最短路径问题
import sys

# 定义Dijkstra算法函数
def dijkstra(graph, start):
    # 初始化节点距离数组
    dist = {node: sys.maxsize for node in graph}
    dist[start] = 0

    # 初始化节点访问状态
    visited = set()

    # 当访问过的节点数量小于图节点数量时，循环
    while len(visited) < len(graph):
        # 选择当前距离最短的节点
        current_node = min((node for node in graph if node not in visited), key=lambda x: dist[x])
        visited.add(current_node)

        # 更新邻居节点的最短距离
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_dist = dist[current_node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    return dist
