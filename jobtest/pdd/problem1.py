"""

最小乘积和
题目描述
给出长度都为n的两个整数数组a[n]和b[n]，特殊运算S=a[0]*b[0] + ... + a[n-1]*b[n-1]，你可以改变a数组的顺序使得运算S得到的值最小，给出最终的最小值。
数组长度n不大于50，对于每个元素x，0<=X<=100。
输入描述:
输入一共三行。
第一行为n，表示两个数组的长度。
第二行包括n个数字，用空格隔开，是a数组的值。
第三行包括n个数字，用空格隔开，是b数组的值。
输出描述:
输出一行，包含一个数字，表示最小的S值。
示例1输入输出示例仅供调试，后台判题数据一般不包含示例
输入
复制
3
1 1 3
10 30 20
输出
复制
80


"""




import sys


def get_min(a,b,n):
    a = sorted(a,reverse=False)
    b = sorted(b,reverse=True)
    result = 0
    for i in range(n):
        result += a[i]*b[i]
    return result


if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    line2 =sys.stdin.readline().strip()
    str_arr1 = line.split()
    str_arr2 = line2.split()
    a = []
    b = []
    for i in range(n):
        a.append(int(str_arr1[i]))
        b.append(int(str_arr2[i]))

    print(get_min(a,b,n))
