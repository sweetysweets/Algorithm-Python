import operator
import sys



class Solution:

    def my_sort(self,nums):
        list_a = nums
        # print("list_a: " + str(nums) + '\n')

        set_a = list(set(list_a))  # 去重得到一个集合
        # print("set_a: " + str(set_a) + '\n')

        count_set_a = {}  # 存放元素和出现次数的字典，key为元素,value为出现次数
        for item in set_a:
            count_set_a[item] = list_a.count(item)
        # print("count_set_a: " + str(count_set_a) + '\n')
        sorted_list_a = sorted(count_set_a.items(), key=operator.itemgetter(1), reverse=True)
        for item in sorted_list_a:  # 按value值从大到小排序
            for i in range(item[1]):
                print(str(item[0]), end=' ')
        print()





if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        k = int(sys.stdin.readline())
        str_arr = sys.stdin.readline().split()
        arr = [int(i) for i in str_arr]
        S.my_sort(arr)



"""
2
5
5 5 4 6 4
5
1 2 3 4 4 5 6 6 6
"""