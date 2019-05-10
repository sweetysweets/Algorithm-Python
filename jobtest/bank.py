def getMax(n):
    n = n - 5
    return getMaxForN(n)



tmp = []
def getMaxForN(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = 1
    for i in range(n-1,0,-1):
        result += getMaxForN(i)
    return result


tmp = []
def getMaxTmp(n):
    global tmp
    tmp = [0 for i in range(n+1)]
    tmp[1] = 1
    result = 1
    for i in range(2,n+1):
        result += tmp[i-1]
        tmp[i] = result%666666666


if __name__ == '__main__':
    n = int(input())

    if n< 6 :
        print(0)
    else:
        getMaxTmp(n-5)
        print(tmp[n-5])
        # print(getMax(n))

