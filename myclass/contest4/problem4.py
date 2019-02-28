"""
Description

Given an array of strings A[ ], determine if the strings can be chained together to form a circle. Astring X can be chained together with another string Y if the last character of X is same as firstcharacter of Y. If every string of the array can be chained, it will form a circle.For eg for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"


Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.

The first line of each test case contains a positive integer N, denoting the size of the array.

The second line of each test case contains a N space seprated strings, denoting the elements of the array A[ ].

1 <= T <= 100

0 < N <= 30

0 < A[i] <= 10


Output

If chain can be formed, then print 1, else print 0.


Sample Input 1

2
3
abc bcd cdf
4
ab bc cd da
Sample Output 1

0
1
"""

CHARS = 26

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = [[] for x in range(V)]
        self.inp = [0] * V

    # function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.inp[w]+=1

    # Method to check if this graph is Eulerian or not
    def isSC(self):
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.V

        # Find the first vertex with non-zero degree
        n = 0
        for n in range(self.V):
            if len(self.adj[n]) > 0:
                break

        # Do DFS traversal starting from first non zero degree vertex.
        self.DFSUtil(n, visited)

        # If DFS traversal doesn't visit all vertices, then return false.
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        for i in range(self.V):
            visited[i] = False

        # Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.DFSUtil(n, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        return True

    # This function returns true if the directed graph has an eulerian
    # cycle, otherwise returns false
    def isEulerianCycle(self):

        # Check if all non-zero degree vertices are connected
        if self.isSC() == False:
            return False

        # Check if in degree and out degree of every vertex is same
        for i in range(self.V):
            if len(self.adj[i]) != self.inp[i]:
                return False

        return True

    # A recursive function to do DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in range(len(self.adj[v])):
            if not visited[self.adj[v][i]]:
                self.DFSUtil(self.adj[v][i], visited)

    # Function that returns reverse (or transpose) of this graph
    # This function is needed in isSC()
    def getTranspose(self):
        g = Graph(self.V)
        for v in range(self.V):
            # Recur for all the vertices adjacent to this vertex
            for i in range(len(self.adj[v])):
                g.adj[self.adj[v][i]].append(v)
                g.inp[v]+=1
        return g



class Solution:

    def is_chain(self,arr, n):

        # Create a graph with 'aplha' edges
        g = Graph(CHARS)

        # Create an edge from first character to last character
        # of every string
        for i in range(n):
            s = arr[i]
            g.addEdge(ord(s[0])-ord('a'), ord(s[len(s)-1])-ord('a'))

        # The given array of strings can be chained if there
        # is an eulerian cycle in the created graph
        if g.isEulerianCycle():
            return 1
        else:
            return 0




if __name__ == '__main__':
    S = Solution()
    t = input()

    for _ in range(int(t)):
        n = int(input())
        str_arr = input().split()
        print(S.is_chain(str_arr,n))

