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
    def __init__(self,str1,str2):
        self.matrix = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        self.str1 = str1
        self.str2 = str2
        self.size1 = len(str1)
        self.size2 = len(str2)

    def get_matrix(self):
        for i in range(self.size1):
            for j in range(self.size2):
                if str1[i] == str2[j]:
                    self.matrix[i+1][j+1] = self.matrix[i][j] + 1
                else:
                    self.matrix[i+1][j+1] = max(self.matrix[i+1][j],self.matrix[i][j+1])

    def show_matrix(self):
        print("----matrix----")
        print(" "," ",end=" ")
        for i in self.str1:
            print(" ".join(i),end=" ")
        print()
        for j in range(self.size2+1):
            if j!= 0:
                print(self.str2[j-1],end=" ")
            else:
                print(" ",end=" ")
            for tmp in range(self.size1+1):
                print(self.matrix[tmp][j],end=" ")
            print()
        print("-------------")

    def get_all_seq(self):
        self.track_back(self.size1,self.size2,[])

    def track_back(self,i,j,seq):
        if i == 0 or j == 0:
            print(''.join(seq[::-1]))
            return   #### 程序返回
        if self.str1[i-1] == self.str2[j-1]:
            seq.append(self.str1[i-1])
            self.track_back(i-1,j-1,seq)
        elif self.matrix[i-1][j] < self.matrix[i][j-1]:
            self.track_back(i,j-1,seq)
        elif self.matrix[i-1][j] > self.matrix[i][j-1]:
            self.track_back(i-1,j,seq)
        else:
            self.track_back(i, j - 1, seq)
            self.track_back(i - 1, j, seq[:])

            # 所以L1 = L是把L所指的对象绑定到名字L1上，
            # 而L2 = L[:]则是把L通过切片运算取得的新列表对象绑定到L2上。
            # 前者两个名字指向同一个对象，后者两个名字指向不同对象。
            # 换句话说，L1和L是指的同一个东西，那么修改L1也就修改了L；
            # L2则是不同的东西，修改L2不会改变L。
            # 注意这个引用的概念对于所有的东西都成立，例如容器内部存储的都是引用……








if __name__ == '__main__':
    str1 = sys.stdin.readline().strip('\n')
    str2 = sys.stdin.readline().strip('\n')
    # str3 = [i for i in str1 if i in str2]
    # str4 = [i for i in str2 if i in str1]


    S = Solution(str1,str2)

    S.get_matrix()
    S.show_matrix()
    S.get_all_seq()
    # result = ""
    # result_set = []
    # S.track_back_v2(len(str1),len(str2),result,result_set)
    # for x in result_set:
    #     print(x)
