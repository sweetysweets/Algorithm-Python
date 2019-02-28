"""
最长公共子序列
Description

给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input

输入为两行，一行一个字符串


Output

输出如果有多个则分为多行，先后顺序不影响判断。


Sample Input 1

1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1

23G456K
23G45JK
"""


import sys


class Solution(object):

    def __init__(self,arr1,arr2,m,n):
        self.arr1 = arr1
        self.arr2 = arr2
        self.n = len(arr1)
        self.m = len(arr2)
        self.num = [0]*n
        for i in range(n):
            self.num[i] = [0]*m
        self.flag = self.num

    def LCS(self):
        for i in range(1,self.n):
            for j in range(1,self.m):
                if self.arr1[i-1] == self.arr2[j-1]:
                    self.num[i][j]=self.num[i-1][j-1]+1
                    self.flag[i][j]=1
                elif self.num[i][j-1]>self.num[i-1][j]:
                    self.num[i][j] = self.num[i][j - 1]
                    self.flag[i][j] = 2
                else:
                    self.num[i][j] = self.num[i-1][j]
                    self.flag[i][j] = 3

    def getLCS(self):
        res = [""]*1000
        k = 0
        i =self.n-1
        j = self.m-1
        while i>0 and j>0:
            if self.flag[i][j]==1:
                res[k]=self.arr1[i-1]
                k +=1
                i -=1
                j -= 1
            elif self.flag[i][j]==2:

                j -= 1
            elif self.flag[i][j] == 3:
                i -= 1

        for i in range(k-1,-1,-1):
            print(res[i])



    

if __name__ == '__main__':
    str1 = sys.stdin.readline().strip('\n')
    str2 = sys.stdin.readline().strip('\n')
    str3 = [i for i in str1 if i in str2]
    str4 = [i for i in str2 if i in str1]

    S = Solution(str3,str4,len(str4),len(str3))
    S.LCS()
    S.getLCS()
