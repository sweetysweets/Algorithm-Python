"""
棋盘覆盖问题
Description

棋盘覆盖问题：给定一个大小为2^n2^n个小方格的棋盘，其中有一个位置已经被填充，现在要用一个L型（22个小方格组成的大方格中去掉其中一个小方格）形状去覆盖剩下的小方格。求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。左上方的第一个格子坐标为(0,0)，第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。


Input

输入第一行为测试用例个数，后面每一个用例有两行，第一行为n值和特殊的格子的坐标（用空格隔开），第二行为需要查找其属于同一个L型格子的格子坐标。


Output

输出每一行为一个用例的解，先按照行值从小到大、再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开。


Sample Input 1

1
1 1 1
0 0
Sample Output 1

0 1,1 0
"""

from sys import stdin


class Solution:
    def __init__(self,n):
        self.board = [[0 for i in range(pow(2,n))] for j in range(pow(2,n))]
        self.tile = 1  #骨牌编号
        self.size = pow(2,n)

    def chessboard(self,tr,tc,dr,dc,size):
        if size == 1:
            return

        t = self.tile  # L型骨牌编号
        self.tile += 1
        s = size // 2 #分割棋盘

        #覆盖左上角子棋盘
        if dr < tr + s and dc < tc + s: # 特殊方格在此棋盘中
            self.chessboard(tr, tc, dr, dc, s)
        else: # 特殊方格不在此棋盘中
            #   用编号为t的骨牌覆盖右下角
            self.board[tr + s - 1][tc + s - 1] = t
            #  覆盖其余方格
            self.chessboard(tr, tc, tr + s - 1, tc + s - 1, s)
        # 覆盖右上角子棋盘
        if dr < tr + s and dc >= tc + s: #特殊方格在此棋盘中
            self.chessboard(tr, tc + s, dr, dc, s)
        else: # 特殊方格不在此棋盘中
            #用编号为t的骨牌覆盖左下角
            self.board[tr + s - 1][tc + s] = t
            # 覆盖其余方格
            self.chessboard(tr, tc + s, tr + s - 1, tc + s, s)
        # 覆盖左下角子棋盘
        if dr >= tr + s and dc < tc + s: # 特殊方格在此棋盘中
            self.chessboard(tr + s, tc, dr, dc, s)

        else: # 特殊方格不在此棋盘中
        # 用编号为t的骨牌覆盖右上角
            self.board[tr + s][tc + s - 1] = t
        # 覆盖其余方格
            self.chessboard(tr + s, tc, tr + s, tc + s - 1, s)


        # 覆盖右下角子棋盘
        if dr >= tr + s and dc >= tc + s: # 特殊方格在此棋盘中
            self.chessboard(tr + s, tc + s, dr, dc, s)

        else: # 特殊方格不在此棋盘中
            # 用编号为t的骨牌覆盖左上角
            self.board[tr + s][tc + s] = t
            # 覆盖其余方格
            self.chessboard(tr + s, tc + s, tr + s, tc + s, s)

    def print_chessboard(self):
        for i in range(len(self.board)):
            print(" ".join(str(x) for x in self.board[i]))
        print()

    def find_spec_point(self,x,y):
        tile = self.board[x][y]
        point = []
        begin_x = x-1 if x-1>=0 else 0
        begin_y = y-1 if y-1>=0 else 0
        end_x = x+2 if x+1<self.size else self.size
        end_y = y + 2 if y + 1 < self.size else self.size

        for i in range(begin_x,end_x):
            for j in range(begin_y,end_y):
                if self.board[i][j] == tile and (i!=x or j!=y):
                    point.append((i, j))

        print(",".join(str(str(x[0])+" "+str(x[1])) for x in point))


if __name__ == '__main__':
    test_case = int(stdin.readline())
    for index in range(test_case):
        str_arr = stdin.readline().split()
        n = int(str_arr[0])
        tr = int(str_arr[1])
        tc = int((str_arr[2]))
        str_arr = stdin.readline().split()
        sr = int(str_arr[0])
        sc = int(str_arr[1])
        S = Solution(n)
        S.chessboard(0, 0, tr, tc, pow(2,n))
        # S.print_chessboard()
        S.find_spec_point(sr, sc)

    # S = Solution(2)
    # S.chessboard(0, 0, 2, 3, 4)
    # S.find_spec_point(3,0)


