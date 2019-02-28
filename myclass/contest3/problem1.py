"""
Description

Babul’s favourite number is 17. He likes the numbers which are divisible by 17.
This time what he does is that he takes a number N and tries to find the largest number which is divisible by 17, by rearranging the digits.
As the number increases he gets puzzled with his own task.
So you as a programmer have to help him to accomplish his task.
Note: If the number is not divisible by rearranging the digits, then print “Not Possible”.
N may have leading zeros.


Input

The first line of input contains an integer T denoting the no of test cases. Each of the next T lines contains the number N.


Output

For each test case in a new line print the desired output.


Sample Input 1

4
17
43
15
16
Sample Output 1

17
34
51
Not Possible
"""

import itertools


class Solution:

    # def largest_div(self,number):
    #     divisibles = list(''.join(x) for x in itertools.permutations(list(number)) if int(''.join(x)) % 17 == 0)
    #     return None if len(divisibles) == 0 else max(divisibles)
    def largest_div(self, number):
        divisibles = list(''.join(x) for x in itertools.permutations(list(number)) if int(''.join(x)) % 17 == 0)
        return None if len(divisibles) == 0 else max(divisibles)




if __name__ == '__main__':
    S = Solution()
    t = input()
    for _ in range(int(t)):
        n = input().strip()
        result = S.largest_div(n)
        print(result if result is not None else 'Not Possible')

