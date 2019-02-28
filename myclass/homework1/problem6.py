
"""
固定和的元素对
Description

输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。

Input

输入第一行是数组，每一个数用空格隔开；第二行是数字和。

Output

输出这样两个数有几对。

Sample Input 1

1 2 4 7 11 0 9 15
11

Sample Output 1
3

"""


import sys


class Solution:

    def two_sum(self, nums, sum):
        result = 0
        nums.sort()
        begin = 0
        end = len(nums) - 1

        # 俩头夹逼，或称两个指针两端扫描法，很经典的方法，O(N)
        while begin < end:
            current_sum = nums[begin] + nums[end]
            if current_sum == sum:
                result += 1
                begin += 1
                end -= 1
            else:
                if current_sum < sum:
                    begin += 1
                else:
                    end -= 1
        return result


if __name__ == '__main__':
    S = Solution()
    str_arr = sys.stdin.readline().split()
    arr = [int(i) for i in str_arr]
    k = int(sys.stdin.readline())
    print(S.two_sum(arr, k))


"""

https://www.kancloud.cn/kancloud/the-art-of-programming/41581

1.定义两个指针，第一个指向第一个元素，第二个指向最后一个元素；

2.先拿第一个元素和最后一个元素相加，与要求的数字进行比较；

    1）如果等于，恭喜找到了；

    2）如果大于，则将第二个指针向后移一位（索引值－1），再求和进行比较；

    3）如果小于，则将第一个指针向前移一位（索引值＋1），在进行求和比较；

直至找到结果。

"""