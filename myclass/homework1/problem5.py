"""
区间第k最小
Description

找到给定数组的给定区间内的倒数第K小的数值。


Input

输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。


Output

结果。


Sample Input 1

1 2 3 4 5 6 7
3 5
2
Sample Output 1

4

"""

import sys


class Solution:

    # def quicksort(self, num, low, high):  # 快速排序
    #     if low < high:
    #         location = self.partition(num, low, high)
    #         self.quicksort(num, low, location - 1)
    #         self.quicksort(num, location + 1, high)

    def partition(self, num, low, high):
        pivot = num[low]
        while low < high:
            while low < high and num[high] > pivot:
                high -= 1
            while low < high and num[low] < pivot:
                low += 1
            temp = num[low]
            num[low] = num[high]
            num[high] = temp
        num[low] = pivot
        return low

    def findkth(self, num, low, high, k):  # 找到数组里第k个数
        index = self.partition(num, low, high)
        if index == k:
            return num[index]
        if index < k:
            return self.findkth(num, index + 1, high, k)
        else:
            return self.findkth(num, low, index - 1, k)


if __name__ == '__main__':
    S = Solution()

    # linelist = map(int, linestrlist)  # 方法一
    # linelist = [int(i) for i in linestrlist] # 方法二

    str_arr = sys.stdin.readline().split()
    arr = [int(i) for i in str_arr]
    low_and_high = sys.stdin.readline().split()
    k = int(sys.stdin.readline())
    high = int(low_and_high[1]) - 1
    low = int(low_and_high[0]) - 1
    reverse_k = k - 1
    print(S.findkth(arr[low:high+1], 0, high - low, reverse_k))

"""
 
　　
def quicksort(num ,low ,high):  #快速排序
    if low< high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)
 
def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] > pivot):
            high -= 1
        while (low < high and num[low] < pivot):
            low += 1
        temp = num[low]
        num[low] = num[high]
        num[high] = temp
    num[low] = pivot
    return low
 
def findkth(num,low,high,k):   #找到数组里第k个数
        index=partition(num,low,high)
        if index==k:return num[index]
        if index<k:
            return findkth(num,index+1,high,k)
        else:
            return findkth(num,low,index-1,k)
 
 
pai = [2,3,1,5,4,6]
# quicksort(pai, 0, len(pai) - 1)
 
print(findkth(pai,0,len(pai)-1,0))
"""

