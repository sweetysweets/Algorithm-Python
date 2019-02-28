"""

分治法解最近对问题
Description

最近对问题：使用分治算法解决最近对问题。


Input

第一行为测试用例个数。后面每一行表示一个用例，一个用例为一些平面上点的集合，点与点之间用逗号隔开，一个点的两个坐标用空格隔开。坐标值都是正数。


Output

对每一个用例输出两个距离最近的点（坐标使用空格隔开），用逗号隔开，先按照第一个坐标大小排列，再按照第二个坐标大小排列。如果有多个解，则按照每个解的第一个点的坐标排序，连续输出多个解，用逗号隔开。


Sample Input 1

1
1 1,2 2,3 3,4 4,5 5,1.5 1.5
Sample Output 1

1 1,1.5 1.5,1.5 1.5,2 2

"""
# 求出平面中距离最近的点对（若存在多对，仅需求出一对）
import random
import math
from sys import stdin


# 计算两点的距离
def calDis(seq):
    dis = math.sqrt((seq[0][0] - seq[1][0]) ** 2 + (seq[0][1] - seq[1][1]) ** 2)
    return dis


# 生成器：生成横跨跨两个点集的候选点
def candidateDot(u, right, dis, med_x):
    cnt = 0
    # 遍历right（已按横坐标升序排序）。若横坐标小于med_x-dis则进入下一次循环；若横坐标大于med_x+dis则跳出循环；若点的纵坐标好是否落在在[u[1]-dis,u[1]+dis]，则返回这个点
    for v in right:
        if v[0] < med_x - dis:
            continue
        if v[0] > med_x + dis:
            break
        if u[1] - dis <= v[1] <= u[1] + dis:
            yield v


# 求出横跨两个部分的点的最小距离
def combine(left, right, resMin, med_x):
    dis = resMin[1]
    minDis = resMin[1]
    pairs = resMin[0]
    for u in left:
        if u[0] < med_x - dis:
            continue
        for v in candidateDot(u, right, dis, med_x):
            dis = calDis([u, v])
            if dis < minDis:
                minDis = dis
                pairs = [[u, v]]
            if dis == minDis:
                pairs.append([u, v])

    return [pairs, minDis]


# 分治求解
def divide(seq):
    # 求序列元素数量
    n = len(seq)
    # 按点的纵坐标升序排序
    seq = sorted(seq)
    # 递归开始进行
    if n <= 1:
        return None, float('inf')
    elif n == 2:
        return [[seq], calDis(seq)]
    else:
        half = int(len(seq) / 2)
        med_x = (seq[half][0] + seq[-half - 1][0]) / 2
        left = seq[:half]
        resLeft = divide(left)
        right = seq[half:]
        resRight = divide(right)
        # 获取两集合中距离最短的点对
        if resLeft[1] < resRight[1]:
            resMin = combine(left, right, resLeft, med_x)
        elif resLeft[1] > resRight[1]:
            resMin = combine(left, right, resRight, med_x)
        else:
            resMin1 = combine(left, right, resLeft, med_x)
            resMin2 = combine(left, right, resRight, med_x)
            resMin =[]
            tmp=[]
            for id in resMin1[0]:
                if id not in tmp:
                    tmp.append(id)
            for id in resMin2[0]:
                if id not in tmp:
                    tmp.append(id)


            # tmp+=resMin1[0]
            # tmp+=resMin2[0]

            resMin.append(tmp)
            resMin.append(resMin1[1])
        pairs = resMin[0]
        minDis = resMin[1]

    return [pairs, minDis]

if __name__ == '__main__':
    test_case = int(stdin.readline())

    for index in range(test_case):
        seq = []
        str_arr = stdin.readline().split(",")
        for i in range(len(str_arr)):
            str_point=str_arr[i].split()
            seq.append((float(str_point[0]),float(str_point[1])))


        result = divide(seq)
        result_pairs=result[0]
        result_pairs.sort(key= lambda  x :(x[0][0],x[0][1]))
        ans = []
        for result_pair in result_pairs:
            ans.append( '{:g}'.format(result_pair[0][0]) + " " + '{:g}'.format(result_pair[0][1]) + "," + '{:g}'.format(
                result_pair[1][0]) + " " + '{:g}'.format(result_pair[1][1]))

        print(",".join(ans))
