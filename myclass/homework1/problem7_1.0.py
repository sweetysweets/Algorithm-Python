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
    def double_end_lis(self, nums):

        left = 0
        mid = 0
        right = 0
        max = 0
        k = 0
        size = len(nums)

        # LIS数组中存储的是递增子序列中最大值最小的子序列的最后一个元素（最大元素）对应array中的值
        LIS = [0 for i in range(10)]
        # 从左到右LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置, 也就是0~i的数字序列中最长递增子序列的长度 - 1
        B = [0 for i in range(10)]
        # 从右到左LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置, 也就是len - 1~i的数字序列中最长递增子序列的长度 - 1
        C = []
        # 从左到右
        # for i in nums[::-1]:
        # b = [0 for i in range(10)]  # 也可以b = [0]*10
        LIS[0] = nums[0]
        for i in range(0, size):
            left = 0
            right = B[k]
            while left <= right:
                mid = int((left + right) / 2)
                if nums[i] < LIS[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            LIS[left] = nums[i]  # 将array[i]入到LIS中
            if left > B[k]:
                B[k + 1] = B[k] + 1
                k += 1
            else:
                B[k + 1] = B[k]
                k += 1

            for i in range(0, k):
                B[i] += 1

        # 从右到左
        for i in range(0, size):
            C[i] = 0
            LIS[i] = 0

        k = 0
        LIS[0] = nums[size - 1]
        for i in range(size - 1, 0, -1):
            left = 0
            right = C[k]
            while left <= right:
                mid = int((left + right) / 2)
                if nums[i] < LIS[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                LIS[left] = nums[i]
                if left > C[k]:
                    C[k + 1] = C[k] + 1
                    k += 1
                else:
                    C[k + 1] = C[k]
                    k += 1
            for i in range(0, k):
                C[i] += 1
                # 求max
            for i in range(0, size):
                for i in range(0, size):
                    if B[i] + C[size - 1 - i] > max:
                        max = B[i] + C[size - 1 - i]
                        print(B[i] + "test" + C[size - 1 - i])
        return size - max + 1

    # def LIS(self, nums):
    #     if not nums:
    #         return None
    #     result = [[0 for col in range(len(nums))] for row in range(len(nums))]
    #     max_len = 0
    #     index = 0
    #
    #     for i in range(len(nums)):
    #
    #         if index == 0:
    #             result[max_len][index] = nums[i]
    #             index += 1
    #         else:
    #             if result[max_len][index-1] > nums[i]:
    #                 result[max_len][index] = nums[i]
    #                 index += 1
    #             else:
    #                 tmp = 0
    #                 while nums[i] < result[max_len][tmp]:
    #                     result[max_len][tmp] = 0
    #                     tmp += 1
    #                 max_len += 1
    #                 result[max_len][0] = nums[i]
    #                 index = 1
    #     return result

    def LIS_tmp(self, nums):
        if not nums:
            return None
        result = []
        max_len = 0
        index = 0

        for i in range(len(nums)):

            if index == 0:
                tmp_arr = []
                result.append(tmp_arr)
                result[max_len].append(nums[i])
                index += 1
            else:
                if result[max_len][index - 1] > nums[i]:
                    result[max_len].append(nums[i])
                    index += 1
                else:

                    while nums[i] < result[max_len][0]:
                        result[max_len].pop(0)

                    max_len += 1
                    tmp_arr = []
                    result.append(tmp_arr)
                    result[max_len].append(nums[i])
                    index = 1

        for i in range(len(result)):
            print(result[i][0])
        return result, max_len + 1




    def double_end_lis_No_2(self, nums):
        final = []
        max = 0

        for i in range(len(nums) - 1):
            num_left = nums[0:i + 1]
            num_right = nums[:i:-1]  # 其中[::-1]代表从后向前取值，每次步进值为1

            result_left = self.lis(num_left)
            result_right = self.lis(num_right)
            if max < len(result_left) + len(result_right):
                max = len(result_left) + len(result_right)
                final = result_left
                for i in range(len(result_right) - 1, -1, -1):
                    final.append(result_right[i])

        return final

    def lis(self, arr):
        n = len(arr)
        m = [0] * n
        result = []
        for x in range(n - 2, -1, -1):
            for y in range(n - 1, x, -1):
                if arr[x] < arr[y] and m[x] <= m[y]:
                    m[x] += 1
            max_value = max(m)
            result = []
            for i in range(n):
                if m[i] == max_value:
                    result.append(arr[i])
                    max_value -= 1
        return result


if __name__ == '__main__':
    S = Solution()
    str_arr = sys.stdin.readline().split()
    arr = [int(i) for i in str_arr]

    final = S.double_end_lis_No_2(arr)
    for i in range(len(final) - 1):
        print(final[i], end=' ')
    print(final[len(final) - 1])

"""
 https://blog.csdn.net/sgbfblog/article/details/7799168

 双端LIS问题（从两端做LIS操作）。
 我们只要在数组的两端进行一次LIS操作，对应的字串长度分别保存在dp[]和dp2[]中，这样我们只要使得dp[i]+dp2[i]-1最大，这个长度就是满足条件的最长字串。
　

假设一个数组arr[n]，它的分段点是i（0-i递增，i到n-1递减），假设我们用方法LIS(i)（最长递增子序列）找到从0到i的递增子序列，LDS找到从i到n-1的最长递减子序列，那么它的总长度为LIS(i) + LDS(i) - 1，所以我们扫描整个数组，即让i从0到n-1，找出使LIS(i) + LDS(i) - 1最大的即可。

"""
