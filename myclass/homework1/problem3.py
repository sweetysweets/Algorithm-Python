"""
数组和窗口
Description

给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，每次向右滑动一个位置，求出每一次滑动时窗口内最大元素的和。


Input

输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。


Output

输出一个值。


Sample Input 1

4 3 5 4 3 3 6 7
3
Sample Output 1

27

"""
from sys import stdin


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 严谨判断输入的数字是否合法
        if not nums:
            return []
        window, res = [], []
        result = 0
        for i, x in enumerate(nums):
            # 如果队列头元素不在滑动窗口中了，就删除头元素
            if i >= k and window[0] <= i-k:
                window.pop(0)
            # 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空
            while window and nums[window[-1]] <= x:  # 把最大值左边的数小的就清除。
                window.pop()
            window.append(i)
            # 滑动窗口经过三个元素，获取当前的最大值，也就是队列的头元素
            if i + 1 >= k:
                res.append(nums[window[0]])
                result += int(nums[window[0]])
        return result


if __name__ == '__main__':

    S = Solution()
    arr = stdin.readline().split()
    k = int(stdin.readline())
    print(S.maxSlidingWindow(arr, k))


"""
借助一个辅助队列，从头遍历数组，根据如下规则进行入队列或出队列操作： 
0. 如果队列为空，则当前数字入队列 
1. 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空，然后当前数字入队列 
2. 如果当前数字小于队列尾，则当前数字入队列 
3. 如果队列头超出滑动窗口范围，则删除队列头 
这样能始终保证队列头为当前的最大值
"""