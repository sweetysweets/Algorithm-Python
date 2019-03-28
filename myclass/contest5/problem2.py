"""
时间分隔
Description

Given arrival and departure times of all trains that reach a railway station.
Your task is to find the minimum number of platforms required for the railway station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day.
Also, arrival and departure times must not be same for a train.


Input

The first line of input contains T, the number of test cases.
For each test case, first line will contain an integer N, the number of trains.
Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.

Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.

Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359


Output

For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.


Sample Input 1

1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000
Sample Output 1

3
"""
class Solution:
    def __init__(self):
        pass


    def findPlatform(self,arr, dep, n):
        # Sort arrival and departure arrays
        arr.sort()
        dep.sort()

        plat_needed = 1
        result = 1
        i = 1
        j = 0


        while i < n and j < n:

            if arr[i] < dep[j]:

                plat_needed += 1
                i += 1

                if plat_needed > result:
                    result = plat_needed

            else:

                plat_needed -= 1
                j += 1

        return result


if __name__ == '__main__':

    t = input()
    for _ in range(int(t)):
        n = int(input())
        arr_strs = input().split()
        dep_strs = input().split()
        arr = [ int(arr_strs[i]) for i in range(n)]
        dep = [ int(dep_strs[i]) for i in range(n)]
        S = Solution()
        result = S.findPlatform(arr,dep,n)
        print(result)




"""

https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

Minimum Number of Platforms Required for a Railway/Bus Station
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
We need to find the maximum number of trains that are there on the given railway station at a time. A Simple Solution is to take every interval one by one and find the number of intervals that overlap with it. Keep track of maximum number of intervals that overlap with an interval. Finally return the maximum value. Time Complexity of this solution is O(n2).



 

We can solve the above problem in O(nLogn) time. The idea is to consider all events in sorted order. Once we have all events in sorted order, we can trace the number of trains at any time keeping track of trains that have arrived, but not departed.

For example consider the above example.

    arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
    dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

All events sorted by time.
Total platforms at any time can be obtained by subtracting total 
departures from total arrivals by that time.
 Time     Event Type     Total Platforms Needed at this Time                               
 9:00       Arrival                  1
 9:10       Departure                0
 9:40       Arrival                  1
 9:50       Arrival                  2
 11:00      Arrival                  3 
 11:20      Departure                2
 11:30      Departure                1
 12:00      Departure                0
 15:00      Arrival                  1
 18:00      Arrival                  2 
 19:00      Departure                1
 20:00      Departure                0

Minimum Platforms needed on railway station = Maximum platforms 
                                              needed at any time 
                                           = 3  
Following is the implementation of above approach. Note that the implementation doesn’t create a single sorted list of all events, rather it individually sorts arr[] and dep[] arrays, and then uses merge process of merge sort to process them together as a single sorted array.
Note : This approach assumes that trains are arriving and departing on same date.


Algorithmic Paradigm: Dynamic Programming

Time Complexity: O(nLogn), assuming that a O(nLogn) sorting algorithm for sorting arr[] and dep[].

Minimum Number of Platforms Required for a Railway/Bus Station | Set 2 (Map based approach)

This article is contributed by Shivam. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above



"""