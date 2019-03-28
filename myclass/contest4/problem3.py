"""

按照要求保留数组元素使得和最大
Description

Given an array of N numbers, we need to maximize the sum of selected numbers.
At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists) and Ai each from the array.
Repeat these steps until the array gets empty.
The problem is to maximize the sum of selected numbers. 必须从大到小选择元素。


Input

The first line of the input contains T denoting the number of the test cases.
For each test case, the first line contains an integer n denoting the size of the array.
 Next line contains n space separated integers denoting the elements of the array. 数组元素已经按照从小到大顺序排列。


Output

For each test case, the output is an integer displaying the maximum sum of selected numbers.


Sample Input 1

1
3
1 2 3
Sample Output 1

4

Input : a[] = {1, 2, 3}
Output : 4
Explanation: At first step we select 1, so 1 and
2 are deleted from the sequence leaving us with 3.
Then we select 3 from the sequence and delete it.
So the sum of selected numbers is 1+3 = 4.


Input : a[] =  {1, 2, 2, 2, 3, 4}
Output : 10
Explanation : Select one of the 2's from the array, so
2, 2-1, 2+1 will be deleted and we are left with {2, 2, 4},
since 1 and 3 are deleted. Select 2 in next two steps,
and then select 4 in the last step.
We get a sum of 2+2+2+4=10 which is the maximum possible.


Our aim is to maximize the sum of selected numbers.
The idea is to pre-calculate the occurrence of all numbers x in the array a[] in a hash ans.
Now our recurrence relation will decide either to select a number or not.
If we select the number then we take the occurrences of that number and the value stored at ans[i-2] as ans[i-1] will be deleted and not be taken to count.
If we do not select the number then we take ans[i-1] which have been pre-calculated while moving forward.

ans[i] = max(ans[i-1], ans[i-2] + ans[i]*i )

At the end, ans[maximum] will have the maximum sum of selected numbers.



"""




class Solution:

    def max_selected(self,n,nums):
        ans = dict.fromkeys(range(0, n + 1), 0)

        for i in range(n):
            ans[nums[i]] += 1

        maximum = max(nums)

        for i in range(2, maximum + 1):
            ans[i] = max(ans[i - 1],
                         ans[i - 2] + ans[i] * i)

        return ans[maximum]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        str_nums = input().split()
        nums = []
        for i in range(n):
            nums.append(int(str_nums[i]))
        S = Solution()
        print(S.max_selected(n,nums))





# Python3 program to Maximize the sum of selected
# numbers by deleting three consecutive numbers.

# function to maximize the sum of
# selected numbers
def maximizeSum(a, n) :

	# stores the occurrences of the numbers
	ans = dict.fromkeys(range(0, n + 1), 0)

	# marks the occurrence of every
	# number in the sequence
	for i in range(n) :
		ans[a[i]] += 1

	# maximum in the sequence
	maximum = max(a)

	# traverse till maximum and apply
	# the recurrence relation
	for i in range(2, maximum + 1) :
		ans[i] = max(ans[i - 1],
					ans[i - 2] + ans[i] * i)

	# return the ans stored in the
	# index of maximum
	return ans[maximum]

# # Driver code
# if __name__ == "__main__" :
#
# 	a = [1, 2, 3]
# 	n = len(a)
# 	print(maximizeSum(a, n))
#
# # This code is contributed by Ryuga
