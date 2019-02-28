"""
实现Shell排序
Description

实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），打印排序结果，注意不一定是最终排序结果！


Input

输入第一行表示测试用例个数，后面为测试用例，每一个用例有两行，第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。


Output

输出的每一行为一个用例对应的指定排序结果。


Sample Input 1

1
49 38 65 97 76 13 27 49 55 4
5 3
Sample Output 1

13 4 49 38 27 49 55 65 97 76

"""
from sys import stdin

class Solution:
    def shell_sort(self,arr,gaps):
        for gap in gaps:
            for j in range(gap, len(arr)):
                i = j
                while (i - gap) >= 0:
                    if arr[i] < arr[i - gap]:
                        arr[i], arr[i - gap] = arr[i - gap], arr[i]
                        i -= gap
                    else:
                        break
        return arr



if __name__ == '__main__':
    S = Solution()
    # arr = [49,38,65,97,76,13,27,49,55,4]
    # gaps = [5,3]
    # print(S.shell_sort(arr,gaps))

    test_case = int(stdin.readline())
    for index in range(test_case):
        str_arr = stdin.readline().split()
        arr = [int(i) for i in str_arr]
        str_gap = stdin.readline().split()
        gaps = [int(i) for i in str_gap]
        result = S.shell_sort(arr, gaps)
        print(" ".join(str(num) for num in result))

