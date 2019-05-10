class Node(object):
    def __init__(self,i,flag):
        self.i = i
        self.flag = flag   #false left true right

    def __str__(self):
        return str(self.i)


def hasMove(nodes,n):
    k = -1
    ## 最大活动整数m
    for tmp in range(n):
        if not nodes[tmp].flag:
            if tmp>=1 and nodes[tmp].i > nodes[tmp-1].i:
                if k == -1 or nodes[k].i <nodes[tmp].i:
                    k = tmp
        else:
            if tmp<len(nodes)-1 and nodes[tmp].i > nodes[tmp+1].i:
                if k == -1 or nodes[k].i < nodes[tmp].i:
                    k = tmp

        # if nodes[tmp].flag and nodes[tmp].i > nodes[tmp + 1].i \
        #         and nodes[k].i < nodes[tmp].i and tmp < n:
        #     k = tmp
        # elif tmp > 1 and not nodes[tmp].flag \
        #         and nodes[tmp].i > nodes[tmp - 1].i \
        #         and nodes[k].i < nodes[tmp].i:
        #     k = tmp



    return k


def jt(n):
    tmp = [Node(i+1,False) for i in range(n)]
    k = n-1
    print([i.i for i in tmp])
    print([i.flag for i in tmp])
    while k != -1:
        print(k)

        m = tmp[k].i
        if not tmp[k].flag:
            tmp[k],tmp[k-1]=tmp[k-1],tmp[k]
        else:
            tmp[k], tmp[k+1] = tmp[k +1], tmp[k]
        ##交换方向
        for i in range(n):
            if tmp[i].i>m:
                tmp[i].flag = not tmp[i].flag

        k = hasMove(tmp,n)
        print([i.i for i in tmp])
        print([i.flag for i in tmp])


if __name__ == '__main__':
    jt(2)