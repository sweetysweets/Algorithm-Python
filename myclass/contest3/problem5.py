"""
Description

In a given cartesian plane, there are N points. We need to find the Number of Pairs of points(A,B) such that

Point A and Point B do not coincide.
Manhattan Distance and the Euclidean Distance between the points should be equal.
Note : Pair of 2 points(A,B) is considered same as Pair of 2 points(B,A).

Manhattan Distance = |x2-x1|+|y2-y1|

Euclidean Distance = ((x2-x1)^2 + (y2-y1)^2)^0.5 where points are (x1,y1) and (x2,y2).

Constraints:1<=T <= 50, 1<=N <= 2*10 ^ 5, 0<=(|Xi|, |Yi|) <= 10^9


Input

First Line Consist of T - number of test cases. For each Test case:First Line consist of N , Number of points. Next line contains N pairs contains two integers Xi and Yi，i.e, X coordinate and the Y coordinate of a Point


Output

Print the number of pairs as asked above.


Sample Input 1

1
2
1 1
7 5
Sample Output 1

0
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def manhattan_distance(self,Point):
        return  abs(Point.x - self.x) +abs(Point.y - self.y)

    def euclidean_distance(self,Point):
        return  pow(pow(Point.x - self.x,2)+pow(Point.y - self.y,2),0.5)

    def is_same(self,Point):
        return Point.x == self.x and Point.y == self.y


class Solution:
    def __init__(self):
        pass


    def find_same_pairs(self, arr,n):
        count = 0
        for i in range(n):
            PointA = Point(arr[i][0],arr[i][1])
            for j in range(i+1,n):
                PointB = Point(arr[j][0], arr[j][1])
                if not PointA.is_same(PointB):
                    if PointA.euclidean_distance(PointB) == PointA.manhattan_distance(PointB):
                        count += 1
        print(count)








if __name__ == '__main__':
    S = Solution()
    t = input()
    for _ in range(int(t)):
        arr = []
        n = int(input())
        for _ in range(n):
            string = input().split()
            arr.append((int(string[0]),int(string[1])))

        S.find_same_pairs(arr,n)


