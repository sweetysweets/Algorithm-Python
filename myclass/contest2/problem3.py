import sys


class Solution:
    # return the maximum element from the array
    def get_max(self, arr, n):
        max = - sys.maxsize
        for i in range(n):
            if arr[i] > max:
                max = arr[i]
        return max

    # return the sum of the elements in the array
    def get_sum(self, arr, n):
        total = 0
        for i in range(n):
            total += arr[i]
        return total

    # find minimum required painters for given maxlen
    # which is the maximum length a painter can paint
    def number_of_painters(self, arr, n, maxlen):
        total = 0
        num_painters = 1
        for i in range(n):
            total += arr[i]
            if total > maxlen:
                # for next count
                total = arr[i]
                num_painters += 1
        return num_painters

    def partition(self, arr, n, k):
        lo = self.get_max(arr, n)
        hi = self.get_sum(arr, n)
        while lo < hi:
            mid = int(lo + (hi - lo) / 2)
            requiredPainters = self.number_of_painters(arr, n, mid)

            # find better optimum in lower half
            # here mid is included because we
            # may not get anything better
            if requiredPainters <= k:
                hi = mid

            # find better optimum in upper half
            # here mid is excluded because it gives
            # required Painters > k, which is invalid
            else:
                lo = mid + 1
        # required
        return lo


if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        str_arr = sys.stdin.readline().split()
        k = int(str_arr[0])
        n = int(str_arr[1])
        str_arr = sys.stdin.readline().split()
        arr = [int(i) for i in str_arr]
        print(S.partition(arr, n, k))
    # str_arr = sys.stdin.readline().split()
    # k = int(str_arr[0])
    # n = int(str_arr[1])
    # str_arr = sys.stdin.readline().split()
    # arr = [int(i) for i in str_arr]
    # print(S.partition(arr, n, k))

"""
2 4
10 10 10 10
https://www.geeksforgeeks.org/painters-partition-problem-set-2/
"""
