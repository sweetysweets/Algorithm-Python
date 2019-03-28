"""
硬币最小数量
Description

Given the list of coins of distinct denominations and total amount of money.
 Output the minimum number of coins required to make up that amount.
 Output -1 if that money cannot be made up using given coins.
 You may assume that there are infinite numbers of coins of each type.


Input

The first line contains 'T' denoting the number of test cases.
Then follows description of test cases.
 Each cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct coins and total amount of money respectively.
  The second line contains N space-separated integers A1, A2, ..., AN denoting the values of coins.

Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000


Output

Print the minimum number of coins required to make up that amount or return -1 if it is impossible to make that amount using given coins.


Sample Input 1

2
3 11
1 2 5
2 7
2 6
Sample Output 1

3
-1
https://blog.csdn.net/M771310443/article/details/50188345
https://blog.csdn.net/qq_26410101/article/details/80777600

dp[i] = min(dp[i], dp[i - coins[j]] + 1);
意思是当零钱为i元需要的最少硬币数等于第i元减去硬币中所有出现的可能的小于i元的硬币的出现次数加1。这里的j从0循环到coins.size()-1，这里dp需要初始化为一个很大的数，但是不能是INT_MAX，否则+1操作会发生数值溢出。


"""


class Solution(object):

    def coin_change(self, coins, amount):
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]

if __name__ == '__main__':
    S = Solution()
    t = input()
    for _ in range(int(t)):
        str_n_amouts = input().split()
        str_coins = input().split()

        n = int(str_n_amouts[0])
        amount = int(str_n_amouts[1])
        coins = [ int(str_coins[i]) for i in range(n)]

        print(S.coin_change(coins,amount))



