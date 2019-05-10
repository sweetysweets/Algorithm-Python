def optimal_bst(p,q,n):
    # e = [[0 for i in range(n+2)] for j in range(n+1)]
    # w = [[0 for i in range(n+2)] for j in range(n+1)]

    e = [[0 for j in range(n + 1)] for i in range(n + 2)]
    w = [[0 for j in range(n + 1)] for i in range(n + 2)]  ##里面的才是列 后面的是行
    root = [[0 for i in range(n+1)] for j in range(n + 2)]

    # e[i,i-1] w[i,i-1]
    for i in range(1,n+2):  #1..n+1
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j = i+l-1
            e[i][j] = float("inf")  ##别忘了初始化
            w[i][j] = w[i][j-1]+p[j]+q[j]

            for r in range(i,j+1):
                t = e[i][r-1]+e[r+1][j]+w[i][j]
                if t<e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e,root

def print_bst(root,i,j,r):
    print(i,j)
    current = root[i][j]
    if current == r:
        print("root is k",current)
        # print_bst(root,i,current-1,current)
        # print_bst(root,current+1,j,current)
        # return

    elif j<r-1:
        return
    elif j == i-1: #di
        if j<r:
            print("d",j,"is left child of",r)
        else:
            print("d", j, "is right child of", r)
        return  ###wangle
    else: #ki
        if current < r:
            print("k", current, "is left child of", r)
        else:
            print("k", current, "is right child of", r)
    print_bst(root, i, current - 1, current)
    print_bst(root, current + 1, j, current)
    return

if __name__ == "__main__":
    p = [0, 0.15, 0.1, 0.05, 0.1, 0.2]
    q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    e, root = optimal_bst(p, q, 5)
    # for i in range(5 + 2):
    #     for j in range(5 + 1):
    #         print(e[i][j], " ", end='')
    #     print()
    # for i in range(5 + 1):
    #     for j in range(5 + 1):
    #         print(root[i][j], " ", end='')
    #     print()
    print_bst(root,1,5,root[1][5])