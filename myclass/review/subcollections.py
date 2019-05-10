# def gen_binary(i):
#     return i <<
#
#
# def sub_collections(arr,n):
#
#     for i in range(2**n):
#         str = gen_binary(i)
#
#
# if __name__ == '__main__':
#     sub_collections(['a','b','c'],3)

class Solution(object):
    def  get_subset(self,n,s,str):

        for i in range(n):
            print("s", s)
            print("i",1<<i)   ## 1 往左移动几i位 与0～7做与运算
            res = s & (1 << i)
            if res != 0:
                print(str[i],end=" ")
        print()

    def test(self):
        str = input('please input str:')
        n = len(str)
        lenth = 1 << n    ###左边移动n位，高位丢弃，低位补0 相当于 2**n
        for i in range(lenth): ##8 times
            self.get_subset(n,i,str)

if __name__ == '__main__':
    S = Solution()
    S.test()