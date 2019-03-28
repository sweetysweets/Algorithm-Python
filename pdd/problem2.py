"""

趣味字母卡片

时间限制：C/C++ 1秒，其他语言 2秒
空间限制：C/C++ 32768K，其他语言 65536K
64bit IO Format: %lld
本题可使用本地IDE编码，不做跳出限制，编码后请点击“保存并调试”按钮进行代码提交。
题目描述
小明给儿子小小明买了一套英文字母卡片（总共包含52张，区分大小写），小小明把卡片丢在地上玩耍，并从中取出若干张排成一排，形成了一个卡片序列。
此时，小明需要将卡片序列中的重复字母剔除（同一个字母的大小写只保留一个）。
请问，所有可能的结果中，字母序最小（不区分大小写）的序列的第一张卡片上是哪个字母？
输入描述:
一行输入，包含一个非空字符串，表示卡片序列，长度为N（1<=N<=52）。
输出描述:
一行输出，包含一个字母（如果结果是大写字母，则需要转成小写）。
示例1输入输出示例仅供调试，后台判题数据一般不包含示例
输入
复制
xaBXY
输出
复制
a
说明
剔除完后的结果为abxy


"""
import sys

my_dict = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l'
,'M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x'
,'Y':'y','Z':'z',
'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k','l':'l'
,'m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x'
,'y':'y','z':'z'}
def get_min_letter(line):
    n = len(line)
    my_list = list(line)
    for i in range(n):
        my_list[i] = my_dict[my_list[i]]
        j = 1
        while j< len(my_list):
            if my_list[0] == my_list[j]:
                if ord(my_list[0]) < ord(my_list[1]):
                    my_list.pop(j)
                    j = 1
                    continue
                else:
                    my_list.pop(0)
                    j = 1
                    continue
            j+= 1
    return my_list[0]

if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    print(get_min_letter(line))