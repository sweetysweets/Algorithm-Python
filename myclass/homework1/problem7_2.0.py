"""
先升后降
Description

从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。


Input

输入时一个数组，数值通过空格隔开。


Output

输出筛选之后的数组，用空格隔开。如果有多种解雇哦，则一行一种结果。


Sample Input 1
1 2 4 7 11 10 9 15 3 5 8 6

Sample Output 1

1 2 4 7 11 10 9 8 6
"""

"""
2 1 5 3 6 4 8 9 7
"""

import sys


class Solution:

    def __init__(self):
        self.lis = []
        self.lds = []

    def lis_arr(self, nums):
        if not nums:
            return 0
        max_length = 0
        result = []
        for i in range(len(nums)):
            result.append(1)
            for j in range(i):
                if nums[j] < nums[i] and result[i] < result[j] + 1:
                    result[i] = result[j] + 1
            if max_length < result[i]:
                max_length = result[i]
        self.lis = result
        return max_length

    def lds_arr(self, nums):
        if not nums:
            return 0
        max_length = 0
        result = []
        for i in range(len(nums)):
            result.append(1)
            for j in range(i):
                if nums[j] > nums[i] and result[i] < result[j] + 1:
                    result[i] = result[j] + 1
            if max_length < result[i]:
                max_length = result[i]
        self.lds = result
        return max_length

    def double_lis_end_index(self, nums):
        if not nums:
            return None
        self.lds_arr(nums)
        self.lis_arr(nums)



    def double_lis_end(self, nums):
        index = self.double_lis_end_index(nums)
        all_lis_list = [[]]
        all_lds_list = [[]]
        for i in index:
            lis_list = []
            self.all_lis(nums[0:i],self.lis,i,lis_list, all_lis_list)
            self.all_lds(nums[i:len(nums)], self.lds, i, lis_list, all_lds_list)
            self.print_all_lis(all_lis_list,all_lds_list)



    def all_lis(self, nums, B, peak_index, lis_list, all_lis_list):
        if B[peak_index] == 1:
            lis_list.append(nums[peak_index])
            lis_list.reverse()
            all_lis_list.append(lis_list)
        else:
            curr_len = B[peak_index]
            lis_list.append(nums[peak_index])
            for i in range(peak_index):
                if B[i] == curr_len-1 and nums[i] < nums[peak_index]:
                    curr_lis = lis_list.copy()
                    self.all_lis(nums, B, i, curr_lis)

    def all_lds(self, nums, B, peak_index, lis_list, all_lds_list):
        if B[peak_index] == 1:
            lis_list.append(nums[peak_index])
            lis_list.reverse()
            all_lds_list.append(lis_list)
        else:
            curr_len = B[peak_index]
            lis_list.append(nums[peak_index])
            for i in range(peak_index):
                if B[i] == curr_len-1 and nums[i] > nums[peak_index]:
                    curr_lis = lis_list.copy()
                    self.all_lis(nums, B, i, curr_lis)

    def print_all_lis(self,all_lis_list,all_lds_list):
        for x in all_lis_list:
            for y in all_lds_list:
                print(x,end=' ')
                print(y)


    # def print_lis(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
    #     return str(self.print_lis(nums[0:len(nums) - 1]))


if __name__ == '__main__':
    S = Solution()
    # str_arr = sys.stdin.readline().split()
    # arr = [int(i) for i in str_arr]

    # final = S.double_end_lis_No_2(arr)
    # for i in range(len(final)-1):
    #     print(final[i], end=' ')
    # print(final[len(final)-1])

    # arr = [2, 1, 5, 3, 6, 4, 10, 9, 7]
    # arr.reverse()
    arr = [1, 2, 4, 7, 10, 9, 15, 3, 5, 8, 6]
    print(S.lds_arr(arr))

"""
 https://blog.csdn.net/sgbfblog/article/details/7799168

 双端LIS问题（从两端做LIS操作）。
 我们只要在数组的两端进行一次LIS操作，对应的字串长度分别保存在dp[]和dp2[]中，这样我们只要使得dp[i]+dp2[i]-1最大，这个长度就是满足条件的最长字串。
　

假设一个数组arr[n]，它的分段点是i（0-i递增，i到n-1递减），假设我们用方法LIS(i)（最长递增子序列）找到从0到i的递增子序列，LDS找到从i到n-1的最长递减子序列，那么它的总长度为LIS(i) + LDS(i) - 1，所以我们扫描整个数组，即让i从0到n-1，找出使LIS(i) + LDS(i) - 1最大的即可。

"""
