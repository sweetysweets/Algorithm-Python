"""
KD树构造和查找
Description

对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，将数据集在分割维度上排序后的中位数作为分割点。程序要检索给定点对应的最近的K个点的坐标。


Input

输入第一行为测试用例个数，后面为测试用例，每一个用例包含三行，第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。


Output

输出每一个用例的最近K个点，按照距离从小到大的顺序打印。


Sample Input 1

1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
2
Sample Output 1

8 6,9 3



1
1 1,2 2,3 3,4 4,5 5,6 6,7 7,8 8,9 9
5 5
3


"""


# https://www.cnblogs.com/bambipai/p/8443182.html
from  sys import stdin
from time import time
from random import randint

from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node:
    def __init__(self,_sa,_loc,_lc,_rc,_p):
        self.splitAttribute = _sa
        self.location = _loc
        self.left_child = _lc
        self.right_child = _rc
        self.parent = _p
        return
    def isLeft(self):
        if self.parent.left_child == self:
            return  True
        else:
            return  False
    def isRight(self):
        if self.parent.right_child == self:
            return True
        else:
            return False
    def isRoot(self):
        if self.parent == None:
            return True
        else:
            return False
    def neghbor(self):
        if self.isRight() == True:
            return  self.parent.left_child
        elif self.isLeft() == True:
            return  self.parent.right_child
        else:
            return None

    # def __str__(self):
        # return "splitAttribute "+str(self.splitAttribute)+"location "+str(self.location) + "left "+ self.left_child.__str__()+" right "+self.right_child.__str__()+"parent "+self.parent.__str__()

def KDTree(point_list,depth=0):
    try:
        k = len(point_list[0])
    except IndexError as e:
        return  None
    axis = depth%k

    point_list.sort(key = itemgetter(axis))
    median = len(point_list) //2
    _left_child = KDTree(point_list[:median], depth + 1)
    _right_child = KDTree(point_list[median + 1:], depth + 1)
    node = Node(axis, point_list[median], _left_child, _right_child,None)
    if node.left_child != None:
        node.left_child.parent = node;
    if node.right_child != None:
        node.right_child.parent = node
    return node


def distancePoint(pointA,pointB):
    if len(pointA) != len(pointB):
        return  -1
    d = len(pointA)
    count = 0
    for i in range(d):
        count += (pointA[i]-pointB[i])**2
    return  count**0.5

"""
k_close(p,o,k,)//查询点p,树当前节点o,近邻数目k 
1. 从根节点开始递归的查找，根据p在节点的左边还是右边，决定递归方向 
2. 若到达叶节点,则将其作为当前最优节点 
3. 回溯: 
(1) 若当前节点比当前最优点更优，则将其作为当前最优节点 
(2) 判断左子树是否存在最优点，若有则递归下去 
4. 当根节点搜索完毕，则查找结束


具体实现的时候需要说明的是，
可以用一个优先队列存储最优的k个节点，
这样每次比对回溯节点是否比当前最优点更优的时候，
就只需用当前最优点中里p最远的节点来比对，而这个工作对于优先队列来说是O(1)的


"""

def searchKDTree(node,point):
    result = []
    if len(node.location) != len(point):
        return None
    axis = node.splitAttribute
    value = point[axis]
    nodeT = node
    while nodeT != None:
        if value <= node.location[axis]:
            node = nodeT
            nodeT = node.left_child
        else:
            node = nodeT
            nodeT = node.right_child

    #back
    curPoint = node
    curDis = distancePoint(curPoint.location,point)
    nodeT = node
    while node.isRoot() != True:
        if node.neghbor() != None:
            dis = distancePoint(point,node.neghbor().location)
            if dis<curDis:

                curPoint = node.neghbor()
                curDis = dis
        if node.isRoot() != True:
            dis = distancePoint(point,node.parent.location)
            if dis<curDis:
                curPoint = node.parent
                curDis = dis
        node = node.parent
    return curPoint
# 　接下来就是搜索树得到k近邻的过程，与搜索最近邻的过程大致相同，需要创建一个字典knears，用于存储k近邻的点以及与目标点的距离（欧氏距离）
#
# 　　搜索的过程为：
#
# 　　(1)第一步还是遍历树，找到目标点所属区域对应的叶节点
#
# 　　(2)从叶结点依次向上回退，按照寻找最近邻点的方法回退到父节点，并判断其另一个子节点对区域内是否可能存在k近邻点，具体的，在每个结点上进行以下操作：
#
# 　　　　(a)如果字典中的成员个数不足k个，将该结点加入字典
#
# 　　　　(b)如果字典中的成员不少于k个，判断该结点与目标结点之间的距离是否不大于字典中各结点所对应距离的的最大值，如果不大于，便将其加入到字典中
#
# 　　　　(c)对于父节点来说，如果目标点与其切分轴之间的距离不大于字典中各结点所对应距离的的最大值，便需要访问该父节点的另一个子节点
#
# 　　(3)每当字典中增加新成员，就按距离值对字典进行降序排序，将得到的列表赋值给poinelist，pointlist[0][1]便是字典中各结点所对应距离的最大值
#
# 　　(4)当回退到根节点并完成对其操作时，pointlist中后k个结点就是目标点的k近邻



class Solution:
    def __init__(self,k):
        self.k = k
        self.knears ={}
        self.pointlist = []

    def search_k_nearest(self,node,aim):
        # 搜索树：输出目标点的近邻点
        # global pointlist  # 存储排序后的k近邻点和对应距离
        if node is None: return
        col = node.splitAttribute
        if aim[col] > node.location[col]:
            self.search_k_nearest(node.right_child, aim)
        if aim[col] < node.location[col]:
            self.search_k_nearest(node.left_child, aim)
        dis = distancePoint(node.location, aim)
        # print(self.knears,self.k)
        if len(self.knears) < self.k:
            self.knears.setdefault(node.location, dis)  # 列表不能作为字典的键
            self.pointlist = sorted(self.knears.items(), key=lambda item: item[1], reverse=True)

        elif dis <= self.pointlist[0][1]:
            self.knears.setdefault(node.location, dis)
            self.pointlist = sorted(self.knears.items(), key=lambda item: item[1], reverse=True)
        # print(self.pointlist)
        if node.right_child is not None or node.left_child is not None:

            # if abs(aim[node.splitAttribute] - node.location[node.splitAttribute]) < self.pointlist[0][1]:
                # if aim[node.splitAttribute] < node.location[node.splitAttribute]:
                #     self.search_k_nearest(node .right_child, aim)
                # if aim[node.splitAttribute] > node.location[node.splitAttribute]:
                #     self.search_k_nearest(node.left_child, aim)
            self.search_k_nearest(node.right_child, aim)
            self.search_k_nearest(node.left_child, aim)
        # print(self.pointlist)
        return self.pointlist


# def main():
#     global pointlist
#     pointlist = []
#     """Example usage"""
#     point_list = [(2.2,3.3), (5.3,4.3), (9.3,6.3), (4.3,7.3), (8.3,1.3), (7.3,2.3)]
#     tree = KDTree(point_list)
#     test_point =(4,9)
#     pointlist = search_k_nearest(tree, test_point)
#     tmpList = []
#     # for point in pointlist[-k:]:
#         # print(point)
#         # tmpList.append(point[0])
#     for i in range(k):
#         tmpList.append(pointlist[len(pointlist)-i-1][0])
#     print(",".join(str(test[0]) + " " + str(test[1]) for test in tmpList))

def transform( c ):
    if '.' not in c:
        return int(c)
    else:
        return float(c)

def main():
    test_case = int(stdin.readline())
    for index in range(test_case):
        point_list = []
        str_arr = stdin.readline().split(",")
        str_aim = stdin.readline().split()
        k = int(stdin.readline())
        for str_points in str_arr:
            str_point = str_points.split()
            x = transform(str_point[0])
            y = transform(str_point[1])
            point_list.append((x,y))
        # print(point_list)
        tree = KDTree(point_list)
        test_point =(transform(str_aim[0]),transform(str_aim[1]))
        S = Solution(k)
        pointlist = S.search_k_nearest(tree, test_point)
        # print(pointlist)
        tmpList = []
        for i in range(k):
            tmpList.append(pointlist[len(pointlist)-i-1][0])
        print(",".join(str(test[0]) + " " + str(test[1]) for test in tmpList))


if __name__ == '__main__':
    main()