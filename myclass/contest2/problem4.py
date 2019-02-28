import sys
import math


class Solution:

    def __init__(self):
        prime_nums = []
        tmp_n = int(math.sqrt(1000000000000))
        # 找出小于平方根的所有质数
        prime = [True] * (tmp_n + 1)
        prime[0] = prime[1] = False
        p = 2
        while p * p <= tmp_n:
            if prime[p] == True:
                i = p * 2
                while i <= tmp_n:
                    prime[i] = False
                    i += p
            p += 1
        for i in range(len(prime)):
            if prime[i] == True:
                prime_nums.append(i)
        self.prime_nums = prime_nums

    def numbersWith9Divisors(self, n):

        tmp_n = int(math.sqrt(n))
        result = []
        # 现在要找出两两乘积小于tmp_n的
        for i in range(len(self.prime_nums)):
            if self.prime_nums[i] * self.prime_nums[0] > tmp_n:
                break
            for j in range(i+1,len(self.prime_nums)):
                if self.prime_nums[i] * self.prime_nums[j] > tmp_n:
                    break
                result.append(self.prime_nums[i] * self.prime_nums[j])
        # for i in result:
        #     print(i*i)

        print(len(result))



if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        n = int(sys.stdin.readline())
        S.numbersWith9Divisors(n)
    # S.numbersWith9Divisors(100)

"""
我认为是找到两个不同质数乘积的数

"""


"""
求质数的简便方法  厄氏大法
for i in range(2,int(n**0.5)+1):
    if prime[i]==True:
        prime[i*i:n:i]= [False]*len(prime[i*i:n:i])
    

"""
