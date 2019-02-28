"""

拓扑排序解的个数
Description

给定有向无环图中所有边，计算图的拓扑排序解的个数。


Input

输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。


Output

输出拓扑排序解的个数。


Sample Input 1

1
a c,b c,c d,d e,d f,e g,f g
Sample Output 1

4

"""

from sys import stdin

class Solution:
    def __init__(self,n,dict,in_degree):
        self.graph = dict
        self.n = n
        self.in_degree = in_degree
        self.ans = [0 for i in range(self.n)]
        self.visit = [0 for i in range(self.n)]
        self.count = 0

    def dfs(self,cnt):
        if cnt == self.n:
            self.count += 1
            # for i in range(self.n):
            #     print(self.ans[i],end=" ")
            # print()
        else:
            for i in range(self.n):
                if self.in_degree[i] == 0 and self.visit[i]== 0:
                    for j in range(self.n):
                        if self.graph[i][j]!= 0:
                            self.in_degree[j] -= 1
                    self.visit[i] = 1
                    self.ans[cnt] = i
                    self.dfs(cnt+1)
                    for k in range(self.n): #回溯，恢复现场，将入度重新加一，并且将该顶点标记为未访问
                        if self.graph[i][k]:
                            self.in_degree[k] += 1
                    self.visit[i] = 0

if __name__ == '__main__':

    # test_case = int(stdin.readline())
    # for index in range(test_case):
    #     graph = dict()
    #
    #     str_arr = stdin.readline().split(",")
    #     for str_points in str_arr:
    #         str_edge = str_points.split()
    #         if graph.get(str_edge[0]):
    #             graph[str_edge[0]].append(str_edge[1])
    #         else:
    #             graph[str_edge[0]] = [str_edge[1]]
    #     print(graph)
    #     S = Solution(graph)
    #     S.dfs(0)

    test_case = int(stdin.readline())
    for index in range(test_case):
        str_arr = stdin.readline().split(",")
        actual = 0
        n = len(str_arr)+1
        graph = [[0 for i in range(n)]for j in range(n)]
        in_degree = [0 for i in range(n)]

        for str_points in str_arr:
            str_edge = str_points.split()
            i = ord(str_edge[0]) - 97
            j = ord(str_edge[1]) - 97
            if i<actual and j< actual:
                pass
            else:
                actual = i if i > j else j
            graph[i][j] = 1
            in_degree[j] += 1
        # for i in range(n):
        #     print(" ".join(str(test) for test in graph[i]))
        # print()
        # print(actual)
        # print(in_degree)
        S = Solution(actual+1,graph,in_degree)
        S.dfs(0)
        print(S.count)


