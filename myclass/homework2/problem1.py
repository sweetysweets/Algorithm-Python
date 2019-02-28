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

    def __init__(self):
        self.resultMap=[]

    def public_sub_sequence(self, arr1, arr2):
        result = ""

        if len(arr1)==0:
            return ""
        if len(arr2)==0:
            return ""

        i = 0
        j = 0
        if arr1[i] == arr2[j]:
            result += arr1[i] + self.public_sub_sequence(arr1[i+1:],arr2[j+1:])
        else:
            result1 = self.public_sub_sequence(arr1[i+1:],arr2[j:])
            result2 = self.public_sub_sequence(arr1[i:], arr2[j+1:])
            if len(result2)>len(result1):
                result += result2
            elif len(result2)<len(result1):
                result += result1
            else:
                result += result2
        return result

    def public_sub_sequence_main(self, arr1, arr2 ):
        result = ""
        result_map = []
        self.public_sub_sequence_v2(arr1,arr2,result_map,result)
        print(result_map)

    def public_sub_sequence_v2(self, arr1, arr2,result_map,this_result):
        if len(arr1) == 0:
            result_map.append(this_result)
            return
        if len(arr2) == 0:
            result_map.append(this_result)
            return

        i = 0
        j = 0
        if arr1[i] == arr2[j]:
            this_result += arr1[i] + self.public_sub_sequence_v2(arr1[i + 1:], arr2[j + 1:],result_map,this_result)
        else:
            result1 = self.public_sub_sequence_v2(arr1[i + 1:], arr2[j:],result_map,this_result)
            result2 = self.public_sub_sequence_v2(arr1[i:], arr2[j + 1:],result_map,this_result)
            if len(result2) > len(result1):
                this_result += result2
            elif len(result2) < len(result1):
                this_result += result1
            else:
                this_result += result2

        return this_result


    

if __name__ == '__main__':
    S = Solution()
    str1 = sys.stdin.readline().strip('\n')
    str2 = sys.stdin.readline().strip('\n')
    str3 = [i for i in str1 if i in str2]
    str4 = [i for i in str2 if i in str1]
    print(S.public_sub_sequence_main(str3, str4))
