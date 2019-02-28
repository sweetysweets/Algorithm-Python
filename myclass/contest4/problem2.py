"""
Description

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only first such pair.

NOTE: A solution will always exist, read Goldbach’s conjecture.Also, solve the problem in linear time complexity, i.e., O(n).


Input

The first line contains T, the number of test cases. The following T lines consist of a number each, for which we'll find two prime numbers.Note: The number would always be an even number.


Output

For every test case print two prime numbers space separated, such that the smaller number appears first. Answer for each test case must be in a new line.


Sample Input 1

5
74
1024
66
8
9990
Sample Output 1

3 71
3 1021
5 61
3 5
17 9973
"""

class Solution:
    def __init__(self,n):
        self.n = n
        self.is_prime = self.SieveOfEratosthenes(n)

    def SieveOfEratosthenes(self,n):
        is_prime = [0] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            is_prime[i] = True
        p = 2
        while p * p <= n:
            if is_prime[p]:
                i = p * 2
                while i <= n:
                    is_prime[i] = False
                    i += p
            p += 1
        return is_prime


    def find_prime_pair(self):
        for i in range(0, self.n):
            if self.is_prime[i] and self.is_prime[self.n - i]:
                print(i, (self.n - i))
                return


if __name__ == '__main__':

    t = input()
    for _ in range(int(t)):
        n = input()
        S = Solution(int(n))
        S.find_prime_pair()




