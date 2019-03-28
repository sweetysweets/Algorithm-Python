
# https://www.jianshu.com/p/25f4a183ede5
class Solution:

    # 函数c[i, w]表示到第i个元素为止，在限制总重量为w的情况下我们所能选择到的最优解。
    def bag(self,v,w,n,c):
        res = [ [-1 for i in range(c+1)] for j in range(n+1)]

        for j in range(c+1):
            res[0][j] = 0

        for i in range(1,n+1):
            for j in range(1,c+1):
                res[i][j] = res[i-1][j]
                if j >= w[i-1] and res[i][j] < res[i-1][j-w[i-1]]+v[i-1]:
                    res[i][j] = res[i-1][j-w[i-1]]+v[i-1]
        return res

    def show(self,n, c, w, res):
        print('最大价值为:', res[n][c])
        x = [False for i in range(n)]
        j = c
        for i in range(1, n + 1):
            if res[i][j] > res[i - 1][j]:
                x[i - 1] = True
                j -= w[i - 1]
        print('选择的物品为:')
        for i in range(n):
            if x[i]:
                print('第', i, '个,', end='')

    def show_matrix(self, res):
        for i in range(len(res)):
            for j in range(len(res[0])):
                print(res[i][j],end=" ")
            print()


if __name__ == '__main__':
    S =Solution()
    vi = [6,3,5,4,6]
    wi = [2,2,6,5,4]
    n= 5
    c = 10
    res = S.bag(vi,wi,n,c)
    S.show_matrix(res)
