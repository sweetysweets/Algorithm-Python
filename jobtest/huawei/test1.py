"""
老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩.

输入描述:
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。

输出描述:
对于每一次询问操作，在一行里面输出最高成绩.

输入例子1:
5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
U 4 5
U 2 9
Q 1 5

输出例子1:
5
6
5
9




"""

def getMax(scores, param, param1):
    if param1<param:
        param1 ,param = param ,param1
    tmp = scores[param-1:param1]
    tmp = sorted(tmp)

    return tmp[-1]


def update(scores, param, param1):
    scores[param-1] = param1
    return scores


import sys

if __name__ == '__main__':
    try:
        while True:
            inputs = input().strip().split()
            n = int(inputs[0])
            m = int(inputs[1])
            scores = input().strip().split()
            scores = [int(i) for i in scores ]
            for i in range(m):
                inputs = input().strip().split()
                if inputs[0] == 'Q':
                    res =  getMax(scores,int(inputs[1]),int(inputs[2]))
                    print(res)
                if inputs[0] == "U":
                    scores = update(scores,int(inputs[1]),int(inputs[2]))
    except:
        pass