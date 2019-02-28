import sys


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        height = [0] * N
        res = 0
        for row in matrix:
            for i in range(N):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, self.maxRectangleArea(height))
        return res

    def maxRectangleArea(self, height):
        if not height: return 0
        res = 0
        stack = list()
        height.append(0)
        for i in range(len(height)):
            cur = height[i]
            while stack and cur < height[stack[-1]]:
                w = height[stack.pop()]
                h = i if not stack else i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res


if __name__ == '__main__':

    S = Solution()
    matrix = []
    for line in sys.stdin:
        if not line:
            break
        if line == '\n':
            break
        arr = line.replace(' ', '').replace('\n', '')
        matrix.append(arr)
        print(matrix)
    max_area = S.maximalRectangle(matrix)
    print(max_area)

