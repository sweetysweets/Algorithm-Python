from collections import defaultdict
from heapq import heapify, heappush, heappop


def Prim(nodes, edges):
    '''  基于最小堆实现的Prim算法  '''
    element = defaultdict(list)
    for start, stop, weight in edges:
        element[start].append((weight, start, stop))
        element[stop].append((weight, stop, start))
    all_nodes = set(nodes)
    used_nodes = set(nodes[0])
    usable_edges = element[nodes[0]][:]
    heapify(usable_edges)
    # 建立最小堆
    MST = []
    while usable_edges and (all_nodes - used_nodes):
        weight, start, stop = heappop(usable_edges)
        if stop not in used_nodes:
            used_nodes.add(stop)
            MST.append((start, stop, weight))
            for member in element[stop]:
                if member[2] not in used_nodes:
                    heappush(usable_edges, member)

    return MST


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
    main()