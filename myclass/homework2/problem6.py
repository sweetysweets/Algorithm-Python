"""
计数排序
Description

实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。


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

    # 时间复杂度n^2 空间复杂度1
    def count_sort(self,nums):
        n = len(nums)
        b = [None] * n
        for i in range(n):
            p = 0
            q = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    p += 1
                elif nums[j] == nums[i]:
                    q += 1
            for k in range(p, p + q):  ##说明这几个位置的值都相同，也可以只判断小的
                b[k] = nums[i]
        return b


    def count_sort_v2(self,nums):
        n = len(nums)
        b = [None] * n
        for i in range(n):
            p = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    p += 1 ##说明这几个位置的值都相同，也可以只判断小的 ,不可以，会有none
            b[p] = nums[i]
        return b

    def print_arr(self, arr):
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
        # arr = [13,24,3,56,34,3,78,12,29,49,84,51,9,100]
        b = S.count_sort(arr)
        print(b)
        S.print_arr(b)
        print()



"""
计数排序是一个非基于比较的排序算法，该算法于1954年由 Harold H. Seward 提出。
它的优势在于在对一定范围内的整数排序时，它的复杂度为Ο(n+k)（其中k是整数的范围），快于任何比较排序算法。
当然这是一种牺牲空间换取时间的做法，而且当O(k)>O(n*log(n))的时候其效率反而不如基于比较的排序（基于比较的排序的时间复杂度在理论上的下限是O(n*log(n)), 如归并排序，堆排序）

主要思想：根据array数组元素的值进行排序，然后统计大于某元素的元素个数，最后就可以得到某元素的合适位置；
比如：array[4] = 9；统计下小于array[4]的元素个数为：8；所以array[4] = 9 应该放在元素的第8个位置；         
主要步骤：        
1、根据array数组，把相应的元素值对应到tmpArray的位置上；      
2、然后根据tmpArray数组元素进行统计大于array数组各个元素的个数；      
3、最后根据上一步统计到的元素，为array元素找到合适的位置，暂时存放到tmp数组中； 
总结
计数排序的时间复杂度和空间复杂度都是非常有效的，
但是该算法对输入的元素有限制要求，所以并不是所有的排序都使用该算法；
最好的是0～9之间的数值差不会很大的数据元素间比较；
有人会说这个没多大用，但是在后面的基数排序中会看到，这可以算是基数排序中的一个基础； 
"""