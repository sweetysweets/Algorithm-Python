
def partition(points,begin,end):
    privot = points[begin]
    i = begin
    j = end
    while i<j:
        while i<j and points[j][0]>privot[0]:
            j-=1
        points[i] = points[j]
        while i<j and points[i][0]<privot[0]:
            i+=1
        points[j] = points[i]
    points[i] = privot
    return i


def qsort(points,start,end):
    if start<end:
        s = partition(points,start,end)
        qsort(points,start,s-1)
        qsort(points,s+1,end)



def convex(points):
    result = []


def convex(points,n):
    result = []
    result.append(points[0])
    result.append(points[n-1])
    up, down, up_max_point, down_max_point = getTwoSubConvex(points,points[0],points[n-1])
    convex(up,up_max_point,)

    return result

def getDistence(point1,point2,point3):
    return (point3[0]-point1[0])*(point2[1]-point1[1]) - (point2[0]-point1[0])*(point3[1]-point1[1])


def getTwoSubConvex(points,point1,point2):
    up = []
    down = []
    up_max_dis = 0
    down_max_dis = 0
    up_max_point = None
    down_max_point = None
    for i in range(len(points)):
        dis = getDistence(point1, point2, points[i])
        if dis>0:
            up.append(points[i])
            if up_max_dis<abs(dis):
                up_max_point = points[i]
        elif dis<0:
            down.append(points[i])
            if down_max_dis < abs(dis):
                down_max_point = points[i]
    return up,down,up_max_point,down_max_point


if __name__ == '__main__':
    points= [(9.0, -16.0),(9.5, 13.0),(-36.0, -10.0),(-8.5, -5.5),(27.0, 7.0),(20.5, 19.0),(-22.5, 19.0),(-14.0, 8.0)]
    points1 = sorted(points,key=lambda x:x[0])
    print(points1)
    qsort(points,0,7)
    print(points)



    # result = convex(points,8)
    # print(result)

    # (9, -16)(-36, -10)
    #
    # (9, -16)(27, 7)
    # (-36, -10)(-22.5, 19)
    # (27, 7)(20.5, 19)
    # (20.5, 19)(-22.5, 19)
