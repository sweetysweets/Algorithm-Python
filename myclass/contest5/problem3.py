"""

时间与收益
Description

Given a set of n jobs where each job i has a deadline and profit associated to it.
Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
We earn the profit if and only if the job is completed by its deadline.
The task is to find the maximum profit and the number of jobs done.


Input

The first line of input contains an integer T denoting the number of test cases.
Each test case consist of an integer N denoting the number of jobs and the next line consist of
Job id, Deadline and the Profit associated to that Job.

Constraints:1<=T<=100，1<=N<=100，1<=Deadline<=100，1<=Profit<=500


Output

Output the number of jobs done and the maximum profit.


Sample Input 1

2
4
1 4 20 2 1 10 3 1 40 4 1 30
5
1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
Sample Output 1

2 60
2 127


https://www.geeksforgeeks.org/job-sequencing-problem-set-1-greedy-algorithm/
"""



class Solution:
    def printJobScheduling(self,arr, t):

        n = len(arr)
        for i in range(n):
            for j in range(n - 1 - i):
                if arr[j][2] < arr[j + 1][2]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        result = [False] * t

        job = ['-1'] * t
        ans = 0
        profit = 0

        for i in range(len(arr)):
            for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
                if result[j] is False:
                    result[j] = True
                    ans += 1
                    profit += arr[i][2]
                    job[j] = arr[i][0]
                    break

        print(ans,profit)





if __name__ == '__main__':
    S = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        deadline = 0
        str_nums = input().split()
        job_list = []
        for i in range(n):
            tmp = i * 3
            J = [int(str_nums[tmp]),int(str_nums[tmp+1]),int(str_nums[tmp+2])]
            deadline = max(int(str_nums[tmp+1]),deadline)
            job_list.append(J)
        S.printJobScheduling(job_list,deadline)






