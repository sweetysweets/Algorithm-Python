"""
调整数组使差最小
Description

有两个序列 a,b，大小都为n,序列元素的值任意整数，无序；
要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。

Input

输入为两行，分别为两个数组，每个值用空格隔开。


Output

输出变化之后的两个数组内元素和的差绝对值。


Sample Input 1

100 99 98 1 2 3
1 2 3 4 5 40
Sample Output 1

96
"""

import sys


class Solution:
    def abs_test(self, a, b):
        # 假设刚开始就是差值最小的
        # 此时的差值绝对值为：
        min = abs(sum(a) - sum(b))
        # x,y分别为a,b列表的下标值
        x = y = 0
        # 当a的下标小于a的长度时，依次用b的每一个值和a的值交换
        # 比较他们的差值绝对值的大小
        while x < len(a):
            # 依次用b的每一个值和当前a的值交换
            while y < len(b):
                a[x], b[y] = b[y], a[x]
                # 交换后2个列表的差值绝对值
                tmp = abs(sum(a) - sum(b))
                # 如果此时的差值小，则赋值给min
                # 否则还将交换回去
                if min >= tmp:
                    min = tmp
                else:
                    a[x], b[y] = b[y], a[x]
                y += 1
            x += 1
            y = 0
        return min
        # return a, b


if __name__ == '__main__':
    S = Solution()
    str_list1 = sys.stdin.readline().split()
    str_list2 = sys.stdin.readline().split()
    a = [int(i) for i in str_list1]
    b = [int(i) for i in str_list2]
    print(S.abs_test(a, b))



"""
整体思想是利用两个列表和的差值绝对值大小判断是否交互两个列表的值

#!/usr/bin/env python

# coding=utf-8
def abs_test(a,b):
    # 假设刚开始就是差值最小的
    # 此时的差值绝对值为：
    min = abs(sum(a)-sum(b))
    # x,y分别为a,b列表的下标值
    x=y=0
    # 当a的下标小于a的长度时，依次用b的每一个值和a的值交换
    # 比较他们的差值绝对值的大小
    while x<len(a):
        #依次用b的每一个值和当前a的值交换
        while y<len(b):
            a[x],b[y] = b[y],a[x]
            # 交换后2个列表的差值绝对值
            tmp = abs(sum(a)-sum(b))
            # 如果此时的差值小，则赋值给min
            # 否则还将交换回去
            if min>tmp:
                min = tmp
            else:
                a[x],b[y] = b[y],a[x]
            y += 1
        x += 1
        y = 0
    return a,b


a = [1000, 999, 998, 997, 996, 995]
b = [994, 993, 992, 3, 2, 1]
val = abs_test(a,b)
print(val）
"""