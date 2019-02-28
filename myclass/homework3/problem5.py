"""
深度优先遍历
Description

按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。


Input

输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。


Output

输出深度优先遍历中遇到的最大深度。


Sample Input 1

1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1

4
"""
from sys import stdin



def dfs(G, v, dep, visited = set()):
    global depth
    visited.add(v)
    depth = max(depth,dep)
    for u in G[v]:
        if u not in visited:
            dfs(G, u, dep+1, visited.copy())



if __name__=='__main__':

    test_case = int(stdin.readline())

    for index in range(test_case):
        str_arr = stdin.readline().split()
        n = int(str_arr[0])
        start = str_arr[1]
        nodes = []
        graph = dict()
        for i in range(n + 1):
            if i == 0:
                nodes = stdin.readline().split()
                continue
            str_arr = stdin.readline().split()  # 边
            edge = []
            for tmp in range(n):
                if str_arr[tmp+1] == '1':
                    edge.append(nodes[tmp])
            graph[str_arr[0]] = edge
        # print(graph)
        depth = 1
        dfs(graph,start,1)
        print(depth)


