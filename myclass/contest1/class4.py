import sys



class Solution:
    def reverse_num(self,nums,n):
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]>nums[j]):
                    count+=1

        return count



if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        k = int(sys.stdin.readline())
        str_arr = sys.stdin.readline().split()
        arr = [int(i) for i in str_arr]
        print(S.reverse_num(arr,k))

