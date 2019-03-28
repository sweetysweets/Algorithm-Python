"""
生活日常之蔬菜购买
Description

Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato.
There are N different vegetable sellers in a line.
Each vegetable seller sells all three vegetable items, but at different prices.
Rahul, obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops.
Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop.
Rahul wishes to spend minimum money buying vegetables using this strategy.
Help Rahul determine the minimum money he will spend.


Input

First line indicates number of test cases T.
Each test case in its first line contains N denoting the number of vegetable sellers in Vegetable Market.
Then each of next N lines contains three space separated integers denoting cost of brinjal, carrot and tomato per kg with that particular vegetable seller.


Output

For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.

Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4


Sample Input 1

1
3
1 50 50
50 50 50
1 50 50
Sample Output 1

52
"""


class Solution:

    def __init__(self,n,costs):
        self.n = n
        self.arr = costs
        self.dp = [[-1 for i in range(3)] for j in range(n+1)]



    def min_cost(self):

        return min(self.arr[0][0] + self.dp_helper( 1, n - 1, 0),
            min(self.arr[0][1] + self.dp_helper( 1, n - 1, 1), self.arr[0][2] + self.dp_helper( 1, n - 1, 2)))

    def dp_helper(self,i,n,curr):
        if n<=0:
            return 0
        if self.dp[n][curr]!=-1:
            return self.dp[n][curr]
        if curr==0:
            self.dp[n][curr] = min(self.arr[i][1] + self.dp_helper(i + 1, n - 1, 1),
                                   self.arr[i][2] + self.dp_helper( i + 1, n - 1, 2))
            return  self.dp[n][curr]
        if curr ==1:
            self.dp[n][curr] = min(self.arr[i][0] + self.dp_helper(i + 1, n - 1, 0),
                                   self.arr[i][2] + self.dp_helper(i + 1, n - 1, 2))
            return self.dp[n][curr]

        self.dp[n][curr] = min(self.arr[i][0] + self.dp_helper(i + 1, n - 1, 0),
                               self.arr[i][1] + self.dp_helper(i + 1, n - 1, 1))
        return self.dp[n][curr]



if __name__ == '__main__':
    t = input()
    for _ in range(int(t)):
        n = int(input())
        costs = []
        for i in range(n):
            str_costs = input().split()
            one_seller_cost = [int(test) for test in str_costs]
            costs.append(one_seller_cost)
        S = Solution(n,costs)

        print(S.min_cost())



