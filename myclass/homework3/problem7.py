
"""


广度优先遍历图
Description

按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。


Input

输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。


Output

输出遍历顺序，用空格隔开


Sample Input 1

1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1

a b c d
"""
from collections import deque
from sys import stdin

from queue import Queue

class Solution:
    def __init__(self,n,graph):
        self.n = n
        self.Visited = [False] * (n + 1)  # 记录该节点是否被访问过


def bfs(G, v):
    q = deque([v])
    # 同样需要申明一个集合来存放已经访问过的顶点，也可以用列表
    visited = {v}
    while q:
        u = q.popleft()
        print(u,end=" ")
        for w in G[u]:
            if w not in visited:
                q.append(w)
                visited.add(w)
        sorted(q)
        # print(q)



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
        bfs(graph,start)



