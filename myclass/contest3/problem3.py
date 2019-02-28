"""
Description

Archana is very fond of strings. She likes to solve many questions related to strings. She comes across a problem which she is unable to solve. Help her to solve.
The problem is as follows:-Given is a string of length L.
Her task is to find the longest string from the given string with characters arranged in descending order of their ASCII code and in arithmetic progression.
She wants the common difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value.


Input

The first line of input contains an integer T denoting the number of test cases. Each test contains a string s of lengthL.

1<= T <= 100

3<= L <=1000

A<=s[i]<=Z

The string contains minimum three different characters.


Output

For each test case print the longest string.
Case 1:Two strings of maximum length are possible- “CBA” and “RPQ”.
But he wants the string to be of higher ASCII value therefore, the output is “RPQ”.
Case 2:The String of maximum length is “JGDA”.


Sample Input 1

2
ABCPQR
ADGJPRT
Sample Output 1

RQP
JGDA
"""




class Solution:
    def __init__(self):
        self.arr = [0] * 26

    def getdp(self,string):
        res = ""
        for i in range(len(string)):
            self.arr[ord(string[i]) - ord('A')] = 1
        for i in range(1, 26):
            for j in range(25, -1, -1):
                if self.arr[j] != 0:
                    ss = chr(ord('A') + j)
                    for k in range(j - i, -1, -i):
                        if self.arr[k] != 0:
                            ss += chr(ord('A') + k)
                        else:
                            break
                    if len(ss) > len(res):
                        res = ss
        self.arr = [0] * 26  ##重置
        return res


if __name__ == '__main__':
    S = Solution()
    t = int(input())
    for _ in range(t):
        string = input()
        print(S.getdp(string))



