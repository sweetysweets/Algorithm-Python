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
"""


# https://www.cnblogs.com/bambipai/p/8443182.html



class decisionnode:
    def __init__(self, value=None, col=None, rb=None, lb=None):
        self.value = value
        self.col = col
        self.rb = rb
        self.lb = lb


# 读取数据并将数据转换为矩阵形式
def readdata(filename):
    data = open(filename).readlines()
    x = []
    for line in data:
        line = line.strip().split('\t')
        x_i = []
        for num in line:
            num = float(num)
            x_i.append(num)
        x.append(x_i)
    x = array(x)
    return x


# 求序列的中值
def median(x):
    n = len(x)
    x = list(x)
    x_order = sorted(x)
    return x_order[n // 2], x.index(x_order[n // 2])


# 以j列的中值划分数据，左小右大，j=节点深度%列数
def buildtree(x, j=0):
    rb = []
    lb = []
    m, n = x.shape
    if m == 0: return None
    edge, row = median(x[:, j].copy())
    for i in range(m):
        if x[i][j] > edge:
            rb.append(i)
        if x[i][j] < edge:
            lb.append(i)
    rb_x = x[rb, :]
    lb_x = x[lb, :]
    rightBranch = buildtree(rb_x, (j + 1) % n)
    leftBranch = buildtree(lb_x, (j + 1) % n)
    return decisionnode(x[row, :], j, rightBranch, leftBranch)


# 搜索树：输出目标点的近邻点
def traveltree(node, aim):
    global pointlist  # 存储排序后的k近邻点和对应距离
    if node == None: return
    col = node.col
    if aim[col] > node.value[col]:
        traveltree(node.rb, aim)
    if aim[col] < node.value[col]:
        traveltree(node.lb, aim)
    dis = dist(node.value, aim)
    if len(knears) < k:
        knears.setdefault(tuple(node.value.tolist()), dis)  # 列表不能作为字典的键
        pointlist = sorted(knears.items(), key=lambda item: item[1], reverse=True)
    elif dis <= pointlist[0][1]:
        knears.setdefault(tuple(node.value.tolist()), dis)
        pointlist = sorted(knears.items(), key=lambda item: item[1], reverse=True)
    if node.rb != None or node.lb != None:
        if abs(aim[node.col] - node.value[node.col]) < pointlist[0][1]:
            if aim[node.col] < node.value[node.col]:
                traveltree(node.rb, aim)
            if aim[node.col] > node.value[node.col]:
                traveltree(node.lb, aim)
    return pointlist


def dist(x1, x2):  # 欧式距离的计算
    return ((np.array(x1) - np.array(x2)) ** 2).sum() ** 0.5


knears = {}
k = int(input('请输入k的值'))
if k < 2: print('k不能是1')
global pointlist
pointlist = []
file = input('请输入数据文件地址')
data = readdata(file)
tree = buildtree(data)
tmp = input('请输入目标点')
tmp = tmp.split(',')
aim = []
for num in tmp:
    num = float(num)
    aim.append(num)
aim = tuple(aim)
pointlist = traveltree(tree, aim)
for point in pointlist[-k:]:
    print(point)
