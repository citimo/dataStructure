# Prim算法，求解最小生成树（Minimum Spanning Tree）的贪心算法，最小生成树是指在给定的带权无向图中选择一棵包含所有节点且边的权重之和最小的树。
import sys

def prim(graph):
    # 选择一个起始节点
    start_node = list(graph.keys())[0]
    
    # 初始化顶点集合和边集合
    vertex_set = set(graph.keys())
    edge_set = set()
    
    # 初始化距离数组
    dist = {node: sys.maxsize for node in graph}
    dist[start_node] = 0
    
    while vertex_set:
        # 选择当前距离最小的节点
        current_node = min(vertex_set, key=lambda x: dist[x])
        vertex_set.remove(current_node)
        
        # 遍历当前节点的邻居节点
        for neighbor, weight in graph[current_node].items():
            if neighbor in vertex_set and weight < dist[neighbor]:
                # 更新距离数组和边集合
                dist[neighbor] = weight
                edge_set.add((current_node, neighbor, weight))
    
    return edge_set
