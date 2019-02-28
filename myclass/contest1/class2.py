import sys



class Solution:
    def min_swap(self,nums,n):

        count =0
        order = sorted(nums)

        for i in range(n):
            if nums[i] == order[i]:
                continue
            else:
                index =nums.index(order[i])
                tmp = nums[i]
                nums[i] = nums[index]
                nums[index] = tmp
                count += 1

        return count



if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        k = int(sys.stdin.readline())
        str_arr = sys.stdin.readline().split()
        arr = [int(i) for i in str_arr]
        print(S.min_swap(arr,k))

