from math import sqrt

class Node():
    def __init__(self , x , y ):
        self.x = x
        self.y = y
    def getDistance(self , a):
        return pow((a.x - self.x),2)+pow((a.y - self.y),2)


def getLevelOfList(a):
    level = 0
    while  type(a) == type([1]):
        level+=1
        a = a[0]
    return level

def nearest_dot(s):
    lenth = len(s)
    left = s[0:lenth//2]
    right = s[lenth//2:]
    mid_x = (left[-1][0]+right[0][0])/2.0   #求中点

    if len(left) > 2:   lmin = nearest_dot(left)    #左侧部分最近点对
    else:   lmin = left
    if len(right) > 2:   rmin = nearest_dot(right)   #右侧部分最近点对
    else:   rmin = right

    # print('此时lmin是：',lmin)
    # print('此时rmin是：',rmin)

    if getLevelOfList(lmin) == 2 and len(lmin) >1:
        # print("len>1 ", lmin)
        dis_l = get_distance(lmin)
    elif getLevelOfList(lmin)==3 and len(lmin) >= 1:
        temp_left_min = float("inf")
        # print(lmin)
        for i in range(len(lmin)):
            tmp = get_distance(lmin[i])
            if tmp < temp_left_min:
                temp_left_min = tmp
        dis_l = temp_left_min
    else:
            # print(lmin)
            dis_l = float("inf")
    if getLevelOfList(rmin)==2 and len(rmin) >1:
        # print("len>1 ", rmin)
        dis_2 = get_distance(rmin)
    elif getLevelOfList(rmin) == 3 and len(rmin) >= 1:
        temp_right_min = float("inf")
        for i in range(len(rmin)):
            # print("rmin[",i,"]是 ", rmin[i])
            tmp = get_distance(rmin[i])
            if tmp < temp_right_min:
                temp_right_min = tmp
        dis_2 = temp_right_min
    else:
        # print(rmin)
        dis_2 = float("inf")

    d = min(dis_l, dis_2)   #最近点对距离


    # print("$$$$$$$$$$$$$$$ ")
    # print("dist_1是：",dis_l)
    # print("dist_2是：",dis_2)
    # print('此时的d= ', d )
    mid_min=[]
    for i in left:
        if mid_x-i[0]<=d :   #如果左侧部分与中间线的距离<=d
            for j in right:
                if abs(i[0]-j[0])<=d and abs(i[1]-j[1])<=d:     #如果右侧部分点在i点的(d,2d)之间
                    if get_distance((i,j))<=d:
                        mid_min.append([i,j])   #ij两点的间距若小于d则加入队列
                        # print('.........' , mid_min)
    if  getLevelOfList(lmin) == 3 and len(lmin) >= 1 and dis_l <= d :
        for i in range(len(lmin)):
            # print('aaaaaaaaaa' , lmin[i])
            mid_min.append(lmin[i])
    elif getLevelOfList(lmin) == 2 and len(lmin) >1 and dis_l <=d :
        mid_min.append(lmin)
    if getLevelOfList(rmin) == 3 and len(rmin) >= 1 and dis_2 <= d:
        for i in range(len(rmin)):
            # print('mmmmmmmm' , rmin[i])
            mid_min.append(rmin[i])
    elif getLevelOfList(rmin) == 2 and len(rmin) > 1 and dis_2 <= d:
        mid_min.append(rmin)

    # for i in range(len(right)):
    #     for j in range( i+1 , len(right)):
    #         if get_distance( (right[i] , right[j])) <= d :
    #             mid_min.append([right[i] , right[j]])
    # for i in range(len(rmin)):
    #     mid_min.append([rmin[i]])
    # print('mid_min是: ', mid_min)
    if mid_min:
        dic=[]
        for i in mid_min:
            dic.append({get_distance(i):i})
        dic.sort(key=lambda x: x.keys())

        result = []
        for i in range(len(dic)):
            if list(dic[i].keys())[0] == list(dic[0].keys())[0]:
                result.append(list(dic[i].values())[0])
            # print('~~~~' , list(dic[i].values())[0] , end=' ')
        # print()
        return result
    elif dis_l>dis_2:
        return rmin
    else:
        return lmin

# 求点对的距离
def get_distance(min):
    return sqrt((min[0][0]-min[1][0])**2 + (min[0][1]-min[1][1])**2)

def divide_conquer(s):
    s.sort( key = lambda x : (x[0],x[1]))
    print('排序好后的s为：', s)
    nearest_dots = nearest_dot(s)
    nearest_dots.sort(key = lambda x: (x[0][0],x[0][1]) )
    print (nearest_dots)
    for i in range(len(nearest_dots)):
        temp_pair = nearest_dots[i]
        for j in [0,1]:
            if i == len(nearest_dots)-1 and j == 1:
                print(temp_pair[j][0], temp_pair[j][1])
            else:
                print(temp_pair[j][0],temp_pair[j][1],end=',')

def transform( c ):
    if '.' not in c:
        return int(c)
    else:
        return float(c)

if __name__=='__main__':
    # a = Node( 1 , 1)
    # b = Node( 1.5 , 1.5 )
    # print( a.getDistance(b))
    # s =[(1,1),(2 ,2),(3,3),(4, 4),(5,5),(1.5,1.5)]
    # print(type(s))
    # # s = [(0, 1), (3, 2), (4, 3), (5, 1), (1, 2), (2, 1), (6, 2), (7, 2), (8, 3), (4, 5), (9, 0), (6, 4)]
    # divide_conquer(s)

    # print(getLevelOfList([[1.5, 1.5], [2, 2]]))         #output : 2
    # print(getLevelOfList([[[1, 1], [1.5, 1.5]], [[1.5, 1.5], [2, 2]]])) #output :3
    #input : 1 1,2 2,3 3,4 4,5 5,1.5 1.5
    #1 1,2 2,2 3,1.5 1.5,2.5 3.5,3 4,9 10,7 8
    #1 1,1 1.5,2 2,3 4.5,2 1.5,3 4,7 8
    #1 1,2 2,3 3,4 4,5 5,1.5 1.5,2.2 2.2
    numOfExamples = int( input())
    for a in range(numOfExamples):
        strInputArray = input().split(',')
        s =[]
        for i in range( len(strInputArray)):
            temp = []
            # print(strInputArray[i])
            temp_str = strInputArray[i].split(' ')
            for j in [0,1]:
                # print(transform(strInputArray[i][j]) , end =' ')
                temp.append(transform(temp_str[j]))
            s.append(temp)
        print(s)
        divide_conquer(s)
