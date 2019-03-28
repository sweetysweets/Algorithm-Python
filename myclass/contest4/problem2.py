"""
数组查询
Description

Given an array, the task is to complete the function which finds the maximum sum subarray, where you may remove atmost one element to get the maximum sum.


Input

第一行为测试用例个数T；后面每两行表示一个用例，第一行为用例中数组长度N，第二行为数组具体内容。


Output

每一行表示对应用例的结果。


Sample Input 1

1
5
1 2 3 -4 5
Sample Output 1

11
Hint

例如，对一个数组A[] = {1, 2, 3, -4, 5}，要移除-4得到最大和的子数组，和为11.
https://www.geeksforgeeks.org/maximum-sum-subarray-removing-one-element/
"""


"""
运行时出现以下错误：TypeError: 'int' object is not callable
变量名和预留的函数名冲突

"""
class Solution:
    def __init__(self,n,nums):
        self.n = n
        self.nums = nums

    def max_sum_of_array(self,arr):
        mini = arr[0]
        sum = 0
        for tmp in arr:
            sum += tmp
            mini = min(tmp,mini)
        if mini < 0:
            sum = sum - mini
        return sum

    def max_sum_of_sub_sequence(self):
        max_sum = self.nums[0]
        start = 0
        sum = 0
        for i in range(self.n):
            if sum < 0:
                sum = self.nums[i]
                start = i
            else:
                sum += i
                sum = self.max_sum_of_array(self.nums[start:i + 1])
            if sum > max_sum:
                max_sum = sum
        return max_sum


if __name__ == '__main__':

    t = input()
    for _ in range(int(t)):
        n = int(input())
        str_nums = input().split()
        nums = []
        for i in range(n):
            nums.append(int(str_nums[i]))
        S = Solution(n,nums)
        result = S.max_sum_of_sub_sequence()
        print(result)




