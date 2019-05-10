if __name__ == '__main__':
    li = [1,2,3,3]
    co = li.copy()
    co[0] = 10000
    print(co)
    print(li)

    test = [[0]*5 for i in range(4)]
    print(test)