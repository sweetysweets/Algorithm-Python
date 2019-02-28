import sys

def first(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2
        if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        if (x > arr[mid]):
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid - 1), x, n)

    return -1


def sortAccording(A1, A2, m, n):
    temp = [0] * m
    visited = [0] * m
    for i in range(0, m):
        temp[i] = A1[i]
        visited[i] = 0

    temp.sort()

    ind = 0

    for i in range(0, n):
        f = first(temp, 0, m - 1, A2[i], m)
        if (f == -1):
            continue
        j = f
        while (j < m and temp[j] == A2[i]):
            A1[ind] = temp[j];
            ind = ind + 1
            visited[j] = 1
            j = j + 1

    for i in range(0, m):
        if (visited[i] == 0):
            A1[ind] = temp[i]
            ind = ind + 1


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print("")



if __name__ == '__main__':

    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        k = sys.stdin.readline().split()

        str_arr = sys.stdin.readline().split()

        arr_1 = [int(i) for i in str_arr]
        str_arr = sys.stdin.readline().split()
        arr_2 = [int(i) for i in str_arr]

        sortAccording(arr_1, arr_2, int(k[0]), int(k[1]))
        printArray(arr_1, int(k[0]))

