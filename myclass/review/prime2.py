from collections import defaultdict
from heapq import heapify, heappush, heappop


def Prim(matrix,begin):
    visited = [False for i in range(len(matrix))]
    current = begin
    while not visited[current]:
        visited[current] = True
        print(current)
        mincost = float("inf")
        tmp = -1
        for i in range(len(matrix[current])):
            if matrix[current][i] < mincost and matrix[current][i]!=0:
                mincost =  matrix[current][i]
                tmp = i
        current = tmp





def main():
    nodes = list('ABCDEFGHI')
    edges = [("A", "B", 4), ("A", "H", 8),
             ("B", "C", 8), ("B", "H", 11),
             ("C", "D", 7), ("C", "F", 4),
             ("C", "I", 2), ("D", "E", 9),
             ("D", "F", 14), ("E", "F", 10),
             ("F", "G", 2), ("G", "H", 1),
             ("G", "I", 6), ("H", "I", 7)]
    print("\n\nThe undirected graph is :", edges)
    print("\n\nThe minimum spanning tree by Prim is : ")
    print(Prim(nodes, edges))


if __name__ == '__main__':
    # main()
    vexs = [
        [0,4,0,0,0,0,0,8,0],
        [0, 0, 8, 0, 0, 0, 0, 11, 0],

        [0, 0, 0, 7, 0, 4, 0, 0, 2],

        [0, 0, 0, 0, 9, 14, 0, 11, 0],

        [0, 0, 0, 0, 0, 10,0 , 0, 0],

        [0, 0, 0, 0, 0, 0, 2, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 1, 6],

        [0, 0, 0, 0, 0, 0, 0, 0, 7],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],

    ]
    Prim(vexs,0)
