from heapq import heappop, heappush
G = {
    0:{},
    1: {1: 1, 2: 2},
    2: {1: 1, 3: 6, 4: 11},
    3: {1: 2, 2: 6, 4: 9, 5: 13},
    4: {2: 11, 3: 9, 5: 7, 6: 3},
    5: {3: 13, 4: 7, 6: 4},
    6: {4: 3, 5: 4},
}

def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        w, p, u = heappop(Q)
        if u in P: continue # 如果目标点在生成树中，跳过
        P[u] = p # 记录目标点不在生成树中
        for v, w in G[u].items():
            heappush(Q, (w, u, v)) # 将u点的出边入堆
    return P


if __name__ == '__main__':

    T = prim(G, 1)
    sum_count = 0
    for k, v in T.items():
        if v !=None:
            sum_count += G[k][v]

    print(sum_count)
    print(T)
    # 结果为19
    # {1: None, 2: 1, 3: 1, 4: 3, 5: 6, 6: 4}
