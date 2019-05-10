
def which_side(point1,point2,point3):

    return (point2[0]-point1[0])*(point3[1]-point1[1]) - (point3[0]-point1[0])*(point2[1]-point1[1]) >0

def is_convex(i,j,n):
    current = None
    for tmp in range(n):
        if tmp != i and tmp != j:
            point3 = points[tmp]
            newFlag = which_side(points[i], points[j], point3)
            print(newFlag)
            if current is None:
                current = newFlag
            else:
                if newFlag != current:
                    return False
    return True


def convex(points,n):
    result = []
    for i in range(n):
        for j in range(i+1,n):
            if is_convex(i,j,n):
                result.append((points[i],points[j]))
    return result






if __name__ == '__main__':
    points= [(9.0, -16.0),(9.5, 13.0),(-36.0, -10.0),(-8.5, -5.5),(27.0, 7.0),(20.5, 19.0),(-22.5, 19.0),(-14.0, 8.0)]
    result = convex(points,8)
    print(result)

    # (9, -16)(-36, -10)
    #
    # (9, -16)(27, 7)
    # (-36, -10)(-22.5, 19)
    # (27, 7)(20.5, 19)
    # (20.5, 19)(-22.5, 19)
