"""
管道网络
Description

Every house in the colony has at most one pipe going into it and at most one pipe going out of it.
Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.
Find the efficient way for the construction of the network of pipes.


Input

The first line contains an integer T denoting the number of test cases. For each test case, the first line contains two integer n & p denoting the number of houses and number of pipes respectively. Next, p lines contain 3 integer inputs a, b & d, d denoting the diameter of the pipe from the house a to house b.Constraints:1<=T<=50，1<=n<=20，1<=p<=50，1<=a, b<=20，1<=d<=100


Output

For each test case, the output is the number of pairs of tanks and taps installed i.e n followed by n lines that contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.


Sample Input 1

1
9 6
7 4 98
5 9 72
4 6 10
2 8 22
9 7 17
3 1 66
Sample Output 1

3
2 8 22
3 1 66
5 6 10


Approach:
Perform DFS from appropriate houses to find all different connected components. The number of different connected components is our answer t.
The next t lines of the output are the beginning of the connected component, end of the connected component and the minimum diameter from the start to the end of the connected component in each line.
Since, tanks can be installed only on the houses having outgoing pipe and no incoming pipe, therefore these are appropriate houses to start DFS from i.e. perform DFS from such unvisited houses.

Below is the implementation of above approach:


 for (int j = 1; j <= n; ++j)

            /*If a pipe has no ending vertex
            but has starting vertex i.e is
            an outgoing pipe then we need
            to start DFS with this vertex.*/
            if (rd[j] == 0 && cd[j]>0) {
                ans = 1000000000;
                int w = dfs(j);

                // We put the details of
                // component in final output
                // array
                a.add(j);
                b.add(w);
                c.add(ans);
            }

"""

class Solution:

    def __init__(self,n,p,arr):
        self.n = n   #house
        self.p = p  #pipes

        self.rd = [ 0 for i in range(1100)]
        self.wt = [0 for i in range(1100)]
        self.cd = [0 for i in range(1100)]
        # arraylist a, b, c are used to store the  final output


        self.a= []
        self.b = []
        self.c = []
        self.ans = 0
        # print(arr)
        i = 0
        while i < p:
            q = arr[i][0]
            h = arr[i][1]
            t = arr[i][2]
            self.cd[q] = h
            self.wt[q] = t
            self.rd[h] = q
            i += 1
        # print(self.rd,self.wt,self.cd)

    def dfs(self,w):
        if self.cd[w] == 0:
            return w
        if self.wt[w] < self.ans:
            self.ans = self.wt[w]
        return self.dfs(self.cd[w])

    def solve(self):
        for  j in range(1,n+1):
            if self.rd[j] == 0 and self.cd[j] > 0:
                self.ans = 1000000000
                w = self.dfs(j)
                self.a.append(j)
                self.b.append(w)
                self.c.append(self.ans)
        print(len(self.a))
        for j in range(len(self.a)):
            print(str(self.a[j])+" "+str(self.b[j])+" "+str(self.c[j]))



if __name__ == '__main__':
    t = input()

    for _ in range(int(t)):
        str_nums = input().split()
        n = int(str_nums[0])
        p = int(str_nums[1])

        arr = []
        for i in range(p):
            str_nums = input().split()
            a = int(str_nums[0])
            b = int(str_nums[1])
            c = int(str_nums[2])
            arr.append([a,b,c])

        S = Solution(n,p,arr)
        S.solve()


"""

Water Connection Problem
Every house in the colony has at most one pipe going into it and at most one pipe going out of it. Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.’
Given two integers n and p denoting the number of houses and the number of pipes. The connections of pipe among the houses contain three input values: a_i, b_i, d_i denoting the pipe of diameter d_i from house a_i to house b_i, find out the efficient solution for the network.
The output will contain the number of pairs of tanks and taps t installed in first line and the next t lines contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.

Examples:

Input : 4 2
        1 2 60
        3 4 50
Output :2
        1 2 60
        3 4 50
Explanation:
Connected components are: 
1->2 and 3->4
Therefore, our answer is 2 followed by
1 2 60 and 3 4 50.

Input :9 6
       7 4 98
       5 9 72
       4 6 10
       2 8 22
       9 7 17
       3 1 66
Output :3
        2 8 22
        3 1 66
        5 6 10
Explanation:
Connected components are 3->1, 
5->9->7->4->6 and 2->8. 
Therefore, our answer is 3 followed by
2 8 22, 3 1 66, 5 6 10

"""