"""
分配问题之匈牙利算法
Description

对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。使用匈牙利算法完成。


Input

输入：第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；用例的第二行为使用逗号隔开的人员完成任务的成本；每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。


Output

输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。


Sample Input 1

1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
Sample Output 1

2 1 3 4
"""
from sys import stdin


class Solution(object):

    def __init__(self,n):
        self.size = n
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        self.visit = [[0 for i in range(n)] for j in range(n)]

    def add_matrix(self,x,y,z):
        self.matrix[x-1][y-1]=z

    def show_matrix(self,matrix):
        for i in range(self.size):
            print(" ".join(str(test) for test in matrix[i]))
        print()
        pass

    # 归约
    def smallize_row(self):
        for i in range(len(self.matrix)):
            row_min = min(self.matrix[i])
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] -= row_min

    def smallize_col(self):
        for i in range(len(self.matrix[0])):
            b = [x[i] for x in self.matrix]
            col_min = min(b)
            for j in range(len(self.matrix)):
                self.matrix[j][i] -= col_min

    # 计算每行每列的0元素的个数
    def countZero(self, row, col):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.matrix[i][j] == 0:
                    row[i] = row[i] + 1
                    col[j] = col[j] + 1

    def markZero(self,row,col,visited):
        count = 0
        while sum(row) + sum(col) >0:
            # 检查行
            for i in range(0, self.size):
                if row[i] == 1:
                    # 若该元素为0 且 未被圆括号标记 且未被双引号标记 再进行访问操作
                    for j in range(0, self.size):
                        if self.matrix[i][j] == 0 and visited[i][j] != 1 and visited[i][j] != -1:
                            visited[i][j] = 1
                            count += 1
                            row[i] -= 1
                            col[j] -= 1
                            for m in range(0, self.size):
                                if self.matrix[m][j] == 0 and visited[m][j] != 1 and visited[m][j] != -1:
                                    visited[m][j] = -1
                                    row[m] -= 1
                                    col[j] -= 1

            # 检查列
            for j in range(0, self.size):
                if col[j] == 1:
                    for i in range(0, self.size):
                        if self.matrix[i][j] == 0 and visited[i][j] != 1 and visited[i][j] != -1:
                            visited[i][j] = 1
                            count += 1
                            row[i] -= 1
                            col[j] -= 1
                            for m in range(0, self.size):
                                if self.matrix[i][m] == 0 and visited[i][m] != 1 and visited[i][m] != -1:
                                    visited[i][m] = -1
                                    row[i] -= 1
                                    col[m] -= 1

            # 对多行多列存在两个及两个以上的为标记的0的操作
            for i in range(0, self.size):
                if row[i] >= 2:
                    for j in range(0, self.size):
                        if self.matrix[i][j] == 0 and visited[i][j] != 1 and visited[i][j] != -1:
                            visited[i][j] = 1
                            count += 1
                            print(row)
                            print(col)
                            row[i] -= 1
                            col[j] -= 1

                            for m in range(0, self.size):
                                if self.matrix[m][j] == 0 and visited[m][j] != 1 and visited[m][j] != -1:
                                    visited[m][j] = -1
                                    row[m] -= 1
                                    col[j] -= 1
                            for n in range(0, self.size):
                                if self.matrix[i][n] == 0 and visited[i][n] != 1 and visited[i][n] != -1:
                                    visited[i][n] = -1
                                    row[i] -= 1
                                    col[n] -= 1

            for j in range(0, self.size):
                if col[j] >= 2:
                    for i in range(0, self.size):
                        if self.matrix[i][j] == 0 and visited[i][j] != 1 and visited[i][j] != -1:
                            visited[i][j] = 1
                            count += 1
                            row[i] -= 1
                            col[j] -= 1
                            for m in range(0, self.size):
                                if self.matrix[i][m] == 0 and visited[i][m] != 1 and visited[i][m] != -1:
                                    visited[i][m] = -1
                                    row[i] -= 1
                                    col[m] -= 1
                            for n in range(0, self.size):
                                if self.matrix[n][j] == 0 and visited[n][j] != 1 and visited[n][j] != -1:
                                    visited[n][j] = -1
                                    row[n] -= 1
                                    col[j] -= 1
        return count




    def print_zero(self,row,col):
        print()
        print("---------count zero------------", )
        print(row)
        print(col)
        print("---------count zero------------", )
        print()
        pass



    def find_min_line(self):
        line = 0
        mark_row = [0 for i in range(self.size)]
        mark_col = [0 for i in range(self.size)]
        for i in range(0, self.size):
            if 1 not in self.visit[i]:
                mark_row[i] = 1


        while True:
            for i in range(0, self.size):
                if mark_row[i] == 1:
                    for j in range(0, self.size):
                        if -1 in self.visit[i][j]:
                            mark_col[j] = 1










    def show_result(self):
        self.show_matrix(self.visit)
        result = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.visit[i][j] == 1:
                    result.append(str(j+1))

        print(" ".join(result))

    def hungary(self):
        self.smallize_row()
        self.smallize_col()
        self.show_matrix(self.matrix)
        row = [0 for i in range(self.size)]
        col = [0 for i in range(self.size)]
        self.countZero(row,col)
        self.print_zero(row,col)
        count = self.markZero(row,col,self.visit)
        self.show_matrix(self.visit)
        self.print_zero(row,col)

        if count == self.size:
            print("ok",)
            self.show_result()
        else:
            self.find_min_line()






if __name__ == '__main__':
    test_case = int(stdin.readline())
    for index in range(test_case):
        n = int(stdin.readline())
        str_arr = stdin.readline().split(",")
        S = Solution(n)
        for my_str in str_arr:
            strs=my_str.split()
            x = int(strs[0])
            y = int(strs[1])
            z = int(strs[2])
            S.add_matrix(x,y,z)
        S.show_matrix(S.matrix)
        S.hungary()
    # n = int(4)
    # str_arr = "2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4".split(",")
    # S = Solution(n)
    # for my_str in str_arr:
    #     strs=my_str.split()
    #     x = int(strs[0])
    #     y = int(strs[1])
    #     z = int(strs[2])
    #     S.add_matrix(x,y,z)
    # S.show_matrix(S.matrix)
    # S.hungary()

"""

1
3
1 2 5,1 1 5,1 3 5,2 1 5,2 2 5,2 3 5,3 1 5,3 2 5,3 3 5


"""
