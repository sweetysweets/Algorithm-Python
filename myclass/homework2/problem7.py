"""
非递归快排
Description

快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""

import sys


class Solution:

    def partition(self, arr, low, high):  #分区操作，返回基准线下标
        privot = arr[low]
        while low < high:
            while low < high and arr[high] >= privot:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= privot:
                low += 1
            arr[high] = arr[low]
        # 此时start = end
        arr[low] = privot
        return low

    def quick_sort(self,arr):
        '''''
        模拟栈操作实现非递归的快速排序
        '''
        if len(arr) < 2:
            return arr
        stack = []
        stack.append(len(arr) - 1)
        stack.append(0)
        while stack:
            l = stack.pop()
            r = stack.pop()
            index = self.partition(arr, l, r)
            if l < index - 1:
                stack.append(index - 1)
                stack.append(l)
            if r > index + 1:
                stack.append(r)
                stack.append(index + 1)

        return arr



    def print_arr(self, arr):
        for i in range(len(arr) - 1):
            print(arr[i], end=' ')
        print(arr[len(arr) - 1], end='')



    def qsort(self,arr):
        if not len(arr):
            return []
        else:
            # 在这里以第一个元素为基准线
            pivot = arr[0]
            left = self.qsort([x for x in arr[1:] if x < pivot])
            right = self.qsort([x for x in arr[1:] if x >= pivot])
        return left + [pivot] + right



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
    # arr = [13, 24, 3, 56, 34, 3, 78, 12, 29, 49, 84, 51, 9, 100]
        b = S.quick_sort(arr)
        S.print_arr(b)
        print()



"""
#quick sort
def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        # 由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < baseValue]
        # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
        equal = [w for w in array if w == baseValue]
        # 由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort(less) + equal + quickSort(greater)
# 示例：
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quickSort(array))
# 输出为[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]
"""
