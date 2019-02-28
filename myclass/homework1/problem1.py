"""
子数组的取值范围
Description

给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果大于num的个数。请实现一个时间复杂度为O(length(arr))的算法。


Input

输入的第一行为数组，每一个数用空格隔开，第二行为num。


Output

输出一个值。


Sample Input 1

3 6 4 3 2
2
Sample Output 1

6

"""

import sys


class DeQueue(object):
    # DeQueue() 创建一个空的新双端队列。 它不需要参数，并返回一个空队列。
    def __init__(self):
        self.items = []

    # enqueue_end(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
    def enqueue_end(self, item):
        self.items.insert(0, item)

    # dequeue_end() 从队尾移除项。它不需要参数并返回 item。 队列被修改。
    def dequeue_end(self):
        item = self.items.pop(0)
        return item

    # enqueue_head(item) 将新项添加到队首。 它需要 item 作为参数，并不返回任何内容。
    def enqueue_head(self, item):
        self.items.append(item)

    # dequeue_head() 从队首移除项。它不需要参数并返回 item。 队列被修改。
    def dequeue_head(self):
        item = self.items.pop()
        return item

    # isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
    def is_empty(self):
        return 0 == len(self.items)

    # size() 返回队列中的项数。它不需要参数，并返回一个整数。
    def size(self):
        length = len(self.items)
        return length

    def peek_end(self):
        return self.items[0]

    def peek_head(self):
        return self.items[-1]


class Solution(object):
    def get_num(self, nums, k):
        if not nums:
            return 0
        res = 0
        i = 0
        j = 0
        q_max = DeQueue()
        q_min = DeQueue()
        while i < len(nums):
            while j < len(nums):
                # 维护窗口最大值
                while not q_max.is_empty() and nums[q_max.peek_end()] <= nums[j]:
                    q_max.dequeue_end()
                q_max.enqueue_end(j)
                # 维护窗口最小值
                while not q_min.is_empty() and nums[q_min.peek_end()] >= nums[j]:
                    q_min.dequeue_end()
                q_min.enqueue_end(j)
                if nums[q_max.peek_head()] - nums[q_min.peek_head()] > k:
                    break
                j += 1
            res += len(nums) - j - i
            if q_max.peek_head() == i:
                q_max.dequeue_head()
            if q_min.peek_head() == i:
                q_min.dequeue_head()
            i += 1
        return res

    def get_num_2(self,nums,k):
        res = 0
        if not nums:
            return res
        size = len(nums)
        max = 0
        min = 0
        for i in range(0, size):
            max = nums[i]
            min = nums[i]
            for j in range(i+1, size):
                if nums[j] < min:
                    min = nums[j]
                if nums[j] > max:
                    max = nums[j]
                if max - min > k:
                    res += (size - j)
                    break
        return res


if __name__ == '__main__':
    S = Solution()
    str_list = sys.stdin.readline().split()
    arr = [int(i) for i in str_list]
    k = int(sys.stdin.readline())
    print(S.get_num_2(arr, k))

"""

使用双端队列，qmax维护着窗口子数组arr[i..j]的最大值更新的结构，
qmin维护着窗口子数组arr[i..j]的最小值更新的结构，
所有下标值最多进qmax和qmin 一次，出qmax和qmin 一次，
i 和j 的值也不断增加，从不减小，所以时间复杂度是O(N)。

　　通过题目可以分析得到以下两个结论：

　　1）如果子数组arr[i..j]满足条件，即max(arr[i..j])-min(arr[i..j])<=num，那么arr[k..l](i<=k<=l<=j)肯定都满足条件，即若一个数组满足条件，它的所有子数组肯定满足条件。

　　2）如果子数组arr[i..j]不满足条件，即max(arr[i..j])-min(arr[i..j])>num，那么arr[k..l](k<=i<=j<=l)肯定不满足条件，即若一个数组不满足条件，所有包含它的数组肯定都不满足条件。

"""

"""


1.生成qmax和qmin，同时生成两个整型变量i和j，表示子数组的范围，即arr[i..j]，生成整型变量res，表示所有满足天骄的子数组数量。

2.令j不断向右移动（j++），表示arr[i..j]一直向右扩大，不断更新qmax和qmin结构。一旦出现arr[i..j]不满足条件的情况，j向右扩的过程停止，此时arr[i..j-1]、arr[i..j-2]、arr[i..j-3]、
……、arr[i..i]都是满足条件的。也就是说满足条件的个数为j - i，即令res = j - i 。

3.完成步骤2，再令i向右移动一个位置，并对qmax和qmin进行更新，此时是arr[i+1..j]窗口的最大值和最小值的更新结构。然后反复重复步骤2。

4.根据步骤2和3，依次求出以arr[0]、arr[1]……、arr[N]作为第一个元素的子数组中满足条件的数量分别有多少个，累积起来的数量就是最终的结果。


"""
