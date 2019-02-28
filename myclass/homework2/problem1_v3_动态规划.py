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
    """
    最长公共子序列：
        通过动态规划，得到矩阵D，
        并从矩阵D中读出一个最长公共子序列
    """

    def __init__(self):
        self.matrix = [[]]

    def init(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.len1 = len(str1)
        self.len2 = len(str2)
        self.matrix = [[0 for i in range(self.len2 + 1)] for j in range(self.len1 + 1)]

    def _get_matrix(self):
        """通过动态规划，构建矩阵"""
        for i in range(self.len1):
            for j in range(self.len2):
                if self.str1[i] == self.str2[j]:
                    self.matrix[i + 1][j + 1] = self.matrix[i][j] + 1
                else:
                    self.matrix[i + 1][j + 1] = max(self.matrix[i][j + 1], self.matrix[i + 1][j])

    def _matrix_show(self, matrix):
        """展示通过动态规划所构建的矩阵"""
        print("----matrix-----")
        print(" ", " ", end=" ")
        for ch in self.str2:
            print(ch, end=" ")
        print()
        for i in range(len(matrix)):
            if i > 0:
                print(self.str1[i - 1], end=" ")
            else:
                print(" ", end=" ")
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()
        print("---------------")

    def _get_one_lcs_from_matrix(self):
        i = len(self.matrix) - 1
        if i == 0:
            print("matrix is too small")
            return
        j = len(self.matrix[0]) - 1
        res = []
        while not (i == 0 or j == 0):
            if self.str1[i - 1] == self.str2[j - 1]:
                res.append(self.str1[i - 1])
                i -= 1
                j -= 1
            else:
                if self.matrix[i - 1][j] > self.matrix[i][j - 1]:
                    i = i - 1
                else:
                    j = j - 1
        return "".join(res[::-1])

    def get_one_lcs(self):
        self._get_matrix()
        self._matrix_show(self.matrix)
        lcs = self._get_one_lcs_from_matrix()
        print(lcs)

    def _get_all_lcs_from_matrix(self):
        self._pre_travesal(self.len1, self.len2, [])

    def _pre_travesal(self, i, j, lcs_ted):
        if i == 0 or j == 0:
            print("".join(lcs_ted[::-1]))
            return
        if self.str1[i - 1] == self.str2[j - 1]:
            lcs_ted.append(self.str1[i - 1])
            self._pre_travesal(i - 1, j - 1, lcs_ted)
        else:
            if self.matrix[i - 1][j] > self.matrix[i][j - 1]:
                self._pre_travesal(i - 1, j, lcs_ted)
            elif self.matrix[i - 1][j] < self.matrix[i][j - 1]:
                self._pre_travesal(i, j - 1, lcs_ted)
            else:
                ###### 分支
                self._pre_travesal(i - 1, j, lcs_ted[:])
                self._pre_travesal(i, j - 1, lcs_ted)

    def get_all_lcs(self):
        self._get_matrix()
        self._matrix_show(self.matrix)
        self._get_all_lcs_from_matrix()

    def track_back_v2(self, i, j, lcs_str, my_set=None):
        while i > 0 and j > 0:
            if self.str1[i - 1] == self.str2[j - 1]:
                lcs_str += self.str1[i - 1]
                i -= 1
                j -= 1
            else:
                if self.matrix[i - 1][j] > self.matrix[i][j - 1]:
                    i -= 1
                elif self.matrix[i - 1][j] < self.matrix[i][j - 1]:
                    j -= 1
                else:
                    self.track_back_v2(i - 1, j, lcs_str, my_set)
                    self.track_back_v2(i, j - 1, lcs_str, my_set)
                    return
        my_set.append(lcs_str[::-1])

    # private
    # void
    # traceBack(int
    # i, int
    # j, String
    # lcs_str) {
    # while (i > 0 & & j > 0) {
    # if (X.charAt(i-1) == Y.charAt(j-1)) {
    # lcs_str += X.charAt(i-1);
    # --i;
    # --j;
    # }
    # else {
    # if (table[i-1][j] > table[i][j-1])
    # --i;
    # else if (table[i-1][j] < table[i][j-1])
    # --j;
    # else {// 相等的情况
    # traceBack(i-1, j, lcs_str);
    # traceBack(i, j-1, lcs_str);
    # return;
    # }
    # }
    # }
    # set.add(reverse(lcs_str));


if __name__ == '__main__':
    str1 = sys.stdin.readline().strip('\n')
    str2 = sys.stdin.readline().strip('\n')
    # str3 = [i for i in str1 if i in str2]
    # str4 = [i for i in str2 if i in str1]

    S = Solution()
    S.init(str1, str2)

    S.get_all_lcs()
    # result = ""
    # result_set = []
    # S.track_back_v2(len(str1),len(str2),result,result_set)
    # for x in result_set:
    #     print(x)
