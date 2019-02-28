import sys


def sortAccording(A1, A2, m, n):
    A3=sorted(A1)
    for i in A2:
        index = A3.index(i)
        if index != -1:
            while A3[index] == i:
                print(i,end=' ')
                A3.pop(index)
    for i in A3:
        print(i,end=' ')
    print()


if __name__ == '__main__':

    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        k = sys.stdin.readline().split()

        str_arr = sys.stdin.readline().split()

        arr_1 = [int(i) for i in str_arr]
        str_arr = sys.stdin.readline().split()
        arr_2 = [int(i) for i in str_arr]

        sortAccording(arr_1, arr_2, int(k[0]), int(k[1]))


