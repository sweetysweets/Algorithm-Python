
"""
题目描述
一个合法的圆括号表达式满足一下条件：
1. ""空字符串被认为是合法的
2. 如果字符串"X"与"Y"是合法的，则"XY"也被认为是合法的
3. 如果字符串"X"是合法的，则"(X)"也是合法的
例子："", "()", "()()", "(())"这些都是合法的
现给出两个不保证合法的由圆括号组成的字符串，你需要交错这两个圆括号序列(在组成的新字符串中，每个初始字符串都保持原来的顺序)
得到一个新的合法的圆括号表达式（不同的交错方式可能会得到相同的表达式，这种情况分开计数），
求共有多少结果合法的交错方式（无法得到合法的圆括号表达式则输出0），
输出结果模 10^9+7 的值(^符号是乘方的意思)

输入描述:
输入包括两行，分别是两个只有"("和")"组成的字符串，长度小于2500

输出描述:
输出为一个数字，表示合法的交错方式数量模上 10^9+7 的结果。


示例1

(()
())

输出

19

"""


import sys






def get_ok(arr1, arr2):
    count = 0
    first_input = len(arr1) + 1
    for i in range(first_input):
        tmp = arr1
        for j in range(len(arr2)):
            tmp.insert(i,arr2[j])
            i+=1
    return count
def is_vaild(list):
    new = []
    for i in range(len(list)):
        if list[i] == '(':
            new .append(list[i])
        else:
            new.pop()

    return len(new) == 0



if __name__ == '__main__':


    line = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    arr1 = list(line)
    arr2 = list(line2)
    print(get_ok(arr1,arr2))