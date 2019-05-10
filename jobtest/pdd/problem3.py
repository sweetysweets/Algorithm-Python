"""
避嫌抢劫

题目描述
小镇沿街分布(可以理解为都在数轴上)，有n家银行（位置以数轴的坐标表示，金额表示可以被抢走的金额），两个绑匪试图分别抢劫一个银行，为了让警方多奔波他们商定选择的两个银行距离不小于d，请问符合约定的情况下他们能抢到的总金额最大是多少？
输入描述:
输入包括 n+1 行。
第一行包含两个数字n和d (1 ≤ n ≤ 200000, 1 ≤ d ≤ 100000000)，n表示银行的数量，d表示约定的距离。
下面n行，每一行包括两个数字a，b（1 <= a,b <= 100000000），分别表示坐标和金额，空格分隔。
输出描述:
输出一个数字，表示可以获得的最大金额。
示例1输入输出示例仅供调试，后台判题数据一般不包含示例
输入
复制
6 3
1 1
3 5
4 8
6 4
10 3
11 2
输出
复制
11


"""




import sys





def get_max_money(n, d, v, p):
    max_money = 0
    for i in range(n):
        for j in range(i,n):
            if d+p[i] <= p[j]:
                max_money = max_money if max_money > v[i] + v[j] else v[i]+v[j]
    return max_money

def get_max_money_v2(n, d, tmp):
    max_money = 0
    tmp = sorted(tmp,key=lambda x:x[1],reverse=True)

    j = 1
    while j < n and tmp[0][0] - d < tmp[j][0] < tmp[0][0] + d:
        j += 1

    # print(j)
    if j==n:
        j = n -1
    for i in range(j+1):
        for m in range(i+1,j+1):
            if tmp[i][0]+d <= tmp[m][0] or tmp[i][0]-d>=tmp[m][0]:
                max_money = max_money if max_money > tmp[m][1] + tmp[i][1] else tmp[m][1] + tmp[i][1]

    return max_money


def get_max_money_v3(n, d, tmp):
    max_money = 0
    tmp1 = sorted(tmp,key=lambda x:x[1],reverse=True)
    tmp2 = sorted(tmp, key=lambda x: x[0], reverse=True)

    j = 1
    while j < n and tmp[0][0] - d < tmp[j][0] < tmp[0][0] + d:
        j += 1

    # print(j)
    if j==n:
        j = n-1
    for i in range(j+1):
        for m in range(i+1,j+1):
            if tmp[i][0]+d <= tmp[m][0] or tmp[i][0]-d>=tmp[m][0]:
                max_money = max_money if max_money > tmp[m][1] + tmp[i][1] else tmp[m][1] + tmp[i][1]
                break
    return max_money

if __name__ == '__main__':


    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    d = int(line[1])
    v = []
    p = []
    tmp = []
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        p.append(int(line[0]))
        v.append(int(line[1]))
        tmp.append((int(line[0]),int(line[1])))

    print(get_max_money_v2(n,d,tmp))







#
#
# import sys
#
# def get_max_money_v2(n, d, tmp):
#     max_money = 0
#     tmp = sorted(tmp,key=lambda x:x[1],reverse=True)
#
#     j = 1
#     while j < n and tmp[0][0] - d < tmp[j][0] < tmp[0][0] + d:
#         j += 1
#     if j==n:
#         j = n -1
#         for i in range(30):
#             for m in range(i+1,j+1):
#                 if tmp[i][0]+d <= tmp[m][0] or tmp[i][0]-d>=tmp[m][0]:
#                     max_money = max_money if max_money > tmp[m][1] + tmp[i][1] else tmp[m][1] + tmp[i][1]
#                     break
#     else:
#         for i in range(j+1):
#             for m in range(i+1,j+1):
#                 if tmp[i][0]+d <= tmp[m][0] or tmp[i][0]-d>=tmp[m][0]:
#                     max_money = max_money if max_money > tmp[m][1] + tmp[i][1] else tmp[m][1] + tmp[i][1]
#                     break
#     return max_money
#
# if __name__ == '__main__':
#
#
#     line = sys.stdin.readline().strip().split()
#     n = int(line[0])
#     d = int(line[1])
#     v = []
#     p = []
#     tmp = []
#     for i in range(n):
#         line = sys.stdin.readline().strip().split()
#         p.append(int(line[0]))
#         v.append(int(line[1]))
#         tmp.append((int(line[0]),int(line[1])))
#
#     print(get_max_money_v2(n,d,tmp))