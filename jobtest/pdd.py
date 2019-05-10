
# parent(i) = floor((i - 1)/2)
# left(i)   = 2i + 1
# right(i)  = 2i + 2


def shift_down(list, index):
    if index * 2 + 1 <= len(list) - 1:
        child = index * 2 + 1
        if child + 1 <= len(list)- 1:
            if list[child] > list[child + 1]:
                child += 1  ##找更小的值
        if list[child] < list[index]:
            list[child], list[index] = list[index], list[child]
            shift_down(list,child)


def shift_up(list,index):
    ## parent 存在
    if (index-1)//2>=0 and list[(index-1)//2] > list[index]:
        list[(index - 1) // 2] , list[index] = list[index], list[(index - 1) // 2]  ##交换
        shift_up(list,(index - 1) // 2)


def delete(list,n,val):
    position = list.index(val)
    list[position] = list[n-1]  ##替换
    list.pop()   ##删除
    parent = (position-1)//2
    ## 没有父亲
    if parent < 0:
        shift_down(list, position)
        return
    else:
        if list[parent]<list[position]:
            shift_down(list,position)
        else:
            shift_up(list,position)



if __name__ == '__main__':
    list=[1,2,3,4,5,6,7,8]
    n = 8
    delete(list,n,7)
    print(list)