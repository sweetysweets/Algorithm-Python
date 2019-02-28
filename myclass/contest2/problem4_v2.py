import sys
import math


class Solution:
    def __init__(self):
        self.prime_nums = []

        # 找出质数
        prime = [True] * 100001
        prime[0] = prime[1] = False
        p = 2
        while p * p <= 100000:
            if prime[p] == True:
                i = p * 2
                while i <= 100000:
                    prime[i] = False
                    i += p
            p += 1
        for i in range(len(prime)):
            if prime[i] == True:
                self.prime_nums.append(i)


    def numbersWith9Divisors(self, n):

        # print(prime_nums)
        count = 0
        for x in self.prime_nums:
            if x**8<n:
                count += 1
        for i in range(0,len(self.prime_nums)):
            for j in range(i+1,len(self.prime_nums)):
                if math.pow(self.prime_nums[i],2) * math.pow(self.prime_nums[j],2)< n:
                    count +=1
        print(count)


    def numbersWith9Divisors_v2(self, n):

        count = 0
        i = 0
        while i < len(self.prime_nums):
            j = i + 1
            if pow(self.prime_nums[i] * self.prime_nums[j], 2) > n:
                break
            while j < len(self.prime_nums):
                if pow(self.prime_nums[i] * self.prime_nums[j], 2) > n:
                    break
                j += 1
                count += 1
            i += 1
        i = 0
        # while self.prime_nums[i] < 28:
        for i in range(len(self.prime_nums)):
            if pow(self.prime_nums[i], 8) > n:
                break
            count += 1
            i += 1
        print(count)





if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        n = int(sys.stdin.readline())
        S.numbersWith9Divisors_v2(n)
