"""
订单问题
Description

Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders. The amount of tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped Ai rupees and if Ankit takes this order, the tip would be Bi rupees.In order to maximize the total tip value they decided to distribute the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal to N, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount of total tip money after processing all the orders.


Input

• The first line contains one integer, number of test cases.

• The second line contains three integers N, X, Y.

• The third line contains N integers. The ith integer represents Ai.

• The fourth line contains N integers. The ith integer represents Bi.


Output

Print a single integer representing the maximum tip money they would receive.


Sample Input 1

2
5 3 3
1 2 3 4 5
5 4 3 2 1
8 4 4
1 4 3 2 7 5 9 6
1 2 3 6 5 4 9 8
Sample Output 1

21
43
"""

import itertools


class Solution:

    def __init__(self,n,x,y,ai,bi):
        self.n = n
        self.x = x
        self.y = y
        self.ai = ai
        self.bi = bi
        self.ans = 0


    def max_tips(self,x,p,q,sum):
        if x == self.n:
            self.ans=self.ans if self.ans > sum else sum
            return
        if p >= 1:
            self.max_tips(x+1, p-1, q, sum+self.ai[x])
        if q >= 1:
            self.max_tips(x + 1, p , q-1, sum + self.bi[x])
        # print(p,q,self.ans)




if __name__ == '__main__':
    t = input()
    for _ in range(int(t)):
        str_nums = input().split()
        n = int(str_nums[0])
        x = int(str_nums[1])
        y = int(str_nums[2])
        str_nums = input().split()
        ai = []
        for i in range(n):
            ai.append(int(str_nums[i]))
        str_nums = input().split()
        bi = []
        for i in range(n):
            bi.append(int(str_nums[i]))

        S = Solution(n,x,y,ai,bi)
        S.max_tips(0,x,y,0)
        print(S.ans)
