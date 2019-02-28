"""
插入排序
Description

实现插入排序。


Input

输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。


Output

输出排序的数组，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""

import sys


class Solution:

    # 时间复杂度n^2 空间复杂度1
    def insert_sort(self, arr):
        for i in range(1, len(arr)):
            wait_sort = arr[i]
            j = i - 1
            while j >= 0 and wait_sort < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = wait_sort

        return arr

    def print_arr(self, arr):
        # print(' '.join(arr))
        for i in range(len(arr) - 1):
            print(arr[i], end=' ')
        print(arr[len(arr) - 1], end='')


if __name__ == '__main__':
    S = Solution()
    for line in sys.stdin:
        if not line:
            break
        if line == '\n':
            break
        arr_str = line.split()
        arr_str.pop(0)
        arr = [int(x) for x in arr_str]
        S.insert_sort(arr)
        S.print_arr(arr)
        print()
