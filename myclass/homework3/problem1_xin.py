
def print1():
    for i in range(len(result)):
        for j in range(len(result[0])):
            if i == len(result)-1 and j == len(result[0])-1:
                print(result[i][j])
            elif i != len(result)-1 and j == len(result[0])-1:
                print(result[i][j],end=',')
            else:
                print(result[i][j] , end=' ')

def mysort(sortindex):
    keyset=""
    for i in range(sortindex):
        keyset+= "x["+str(i)+"],"
    keyset = keyset.rstrip(",")
    '''
        按照这里把我在网上找的博客https://blog.csdn.net/lianshaohua/article/details/80483357
        里的'+',改为','就可以了
    '''
    result.sort(key=lambda x:eval(keyset),reverse=True)

def work( i , count , res_temp):
    global cost
    res_temp_copy = res_temp.copy()
    # print('result是：', result, 'cost是：', cost)
    if i > n :
        # global result
        if count == cost:
            # print('此时的res_temp是：', res_temp_copy, 'count是：', count)
            if res_temp_copy not in result:
                result.append(res_temp_copy)
            # print('count==cost的 result',  res)
        if count < cost:
            # print('此时的res_temp是：aaaa   ', res_temp_copy, 'count是：', count)
            result.clear()
            result.append(res_temp_copy)
            # print('count<cost的result ', res)
            cost = count
    if count <= cost:
        for j in range(1,n+1):
            if x[j] == 0 :
                res_temp.append(j)
                x[j] = 1
                work(  i + 1 , count+costMatrix[i][j] , res_temp)
                res_temp.pop()
                x[j] = 0



if __name__=='__main__':
    numOfExamples = int(input())
    x = [ 0 for i in range(1000)]
    for c in range(numOfExamples):
        n = int(input())
        costMatrix = [[0 for j in range(n + 1)] for i in range(n + 1)]
        strarray = input().split(',')
        for j in range(0, len(strarray)):
            temp_array = []
            tempArray = strarray[j].split(' ')
            costMatrix[int(tempArray[0])][int(tempArray[1])] = int(tempArray[2])
        print(costMatrix)
        cost = 0
        res_temp = []
        result = []
        for i in range( 1 , len(costMatrix)):
            cost += costMatrix[i][i]
            res_temp.append(i)
        result.append(res_temp)
        print('开始前的result是：',result)
        work(1,0, [])
        # print1()
        # a = []
        print('结束后的result是：',result)
        mysort(len(result[0]))
        # result.sort(key=lambda x:(x[0],x[1],x[2],x[3]),reverse=True)
        print1()

#自测用例
#2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
#2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 6,3 1 5,3 2 8,3 3 1,3 4 8,4 1 4,4 2 6,4 3 9,4 4 4
#1 1 1,2 1 1,3 1 1,1 2 1,1 3 1,2 2 1,2 3 1,3 3 1,3 2 1
#1 1 1,2 1 1,3 1 1,4 1 1,1 2 1,1 3 1,1 4 1,2 2 1,2 3 1,2 4 1,3 2 1,4 2 1,3 3 1,3 4 1,4 4 1,4 3 1
#1 1 1,2 1 1,3 1 1,4 1 1,1 2 1,1 3 1,1 4 1,2 2 3,2 3 1,2 4 1,3 2 1,4 2 1,3 3 1,3 4 1,4 4 1,4 3 1
'''
    1 1 1 1
    1 2 1 1
    1 1 1 1
    1 1 1 1
'''
#1 1 1,2 1 1,3 1 1,4 1 1,1 2 1,1 3 1,1 4 1,2 2 3,2 3 1,2 4 1,3 2 2,4 2 1,3 3 1,3 4 1,4 4 1,4 3 1
'''
    1 1 1 1
    1 2 1 1
    1 2 1 1
    1 1 1 1
'''
