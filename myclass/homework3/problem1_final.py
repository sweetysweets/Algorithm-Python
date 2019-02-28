"""
分配问题
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
        self.cost = 0
        self.result = []
        self.visit = [ 0 for i in range(n)]



    def init_result(self):
        res_temp = []
        for i in range(self.size):
            self.cost += self.matrix[i][i]
            res_temp.append(i)
        self.result.append(res_temp)



    def add_matrix(self,x,y,z):
        self.matrix[x-1][y-1]=z

    def show_matrix(self,matrix):
        for i in range(self.size):
            print(" ".join(str(test) for test in matrix[i]))
        print()
        pass

    # cost是当前的最小成本
    # count是当前得到的成本
    def hand_out_works(self,i, count, res_temp):
        res_temp_copy = res_temp.copy()
        if i == n:
            if count == self.cost:
                if res_temp_copy not in self.result:
                    self.result.append(res_temp_copy)
            if count < self.cost:
                self.result.clear()
                self.result.append(res_temp_copy)
                self.cost = count
        if count <= self.cost:
            for j in range(n):

                if self.visit[j] == 0:
                    res_temp.append(j)
                    self.visit[j] = 1
                    self.hand_out_works(i+1 , count + self.matrix[i][j], res_temp)
                    res_temp.pop()
                    self.visit[j] = 0


    def show_result(self):
        #排序 ，任务序号大的最前面
        # list的动态多列排序
        # 主要利用的是lambda表达式的eval()
        # 函数，eval函数能够把字符串编译成python代码并运行，从而达到动态根据多个列或属性排序的目的。

        keyset = ""
        for i in range(len(self.result[0])):
            keyset += "x[" + str(i) + "],"
        keyset = keyset.rstrip(",")


        self.result.sort(key=lambda x: eval(keyset), reverse=True)

        tmp = []
        for tmp_list in self.result:
            tmp.append(" ".join([str(test+1) for test in tmp_list]))
        print(",".join(tmp))






if __name__ == '__main__':
    test_case = int(stdin.readline())
    for index in range(test_case):
        n = int(stdin.readline())
        str_arr = stdin.readline().split(",")
        S = Solution(n)
        for my_str in str_arr:
            strs = my_str.split()
            x = int(strs[0])
            y = int(strs[1])
            z = int(strs[2])
            S.add_matrix(x, y, z)
        # S.show_matrix(S.matrix)
        S.init_result()
        S.hand_out_works(0, 0, [])
        S.show_result()
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
    # S.init_result()
    # S.hand_out_works(0, 0, [])
    # S.show_result()


"""

1
3
1 2 5,1 1 5,1 3 5,2 1 5,2 2 5,2 3 5,3 1 5,3 2 5,3 3 5


"""
