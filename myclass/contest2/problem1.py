import sys


class Solution:

    def super_pow(self, a, b, m):
        ans = 1
        a %= m
        while b:
            if b % 2 == 1:
                # ans *= a
                # ans %= m
                ans = (ans * a) % m
            b = int(b/2)
            a = (a * a) % m
        return ans


if __name__ == '__main__':
    S = Solution()
    test_case = int(sys.stdin.readline())
    for index in range(test_case):
        str_arr = sys.stdin.readline().split()
        arr = [int(i) for i in str_arr]
        result = S.super_pow(arr[0], arr[1], arr[2])
        print(result)

"""
leetcode Super Pow
题目描述：

   superPow(int a, int[] b),b是一个int数组，每个元素都是正的个位数，组合起来表示一个正整数，例如b=[1,2,3]表示123，求解a^b mod 1337.

思路描述：

   本题的难点是当a和b足够大时会造成溢出，因此应考虑其他算法来实现。

   理论支持(转幂算法):

                  (a^b) mod c = ((a mod c)^b) mod c ----公式1

                  (x*y) mod c = ((x mod c) * (y mod c)) mod c  :积的取余等于取余的积的取余。 -----公式2

   基于上述的算法，有：

          首先将a对c取余，不妨设余数值为x，则：(a^b) mod c = （x^b）mod c    ---基于式1

          （x^b）mod c = (((x ^ (b/2)) mod c) * ((x ^ (b/2)) mod c) ) mod c    ：b为偶数

          （x^b）mod c = (((x ^ (b/2)) mod c) * ((x ^ (b/2)) mod c) * x) mod c  ：b为奇数

                                                                                                        ----基于式2

   基于上述分析，问题解决思路如下： 首先将a对1337取余；然后将数组组成的整数除2，然后带入superPow（a, b/2）,递归进行一直到b为0返回。

   其中b/2实现比较绕，可以考虑我们初学除法时的步骤，实现算法与之很类似。

 """




"""
//直接法求欧拉函数
int Euler(int n)
{
    int m=floor(sqrt(n+0.5));
    int ans=n;
    for(int i=2;i<=m;i++){
        if(n%i==0){
            ans=ans/i*(i-1);
            while(n%i==0)
                n/=i;
        }
    }
    if(n>1)
        ans=ans/n*(n-1);
    return ans;
}
//快速乘法
LL Mul(LL a,LL b,LL mod)
{
    LL res=0;
    while(b>0){
        if(b&1) res=(res+a)%mod;
        b>>=1;
        a=(a+a)%mod;
    }
    return res;
}
//快速幂
LL modxp(LL a,LL b,LL mod)
{
    LL res=1;
    while(b>0){
        if(b&1) res=Mul(res,a,mod);
        b>>=1;
        a=Mul(a,a,mod);
    }
    return res;
}

LL Solve(LL a,char str[],LL mod)
{
    LL len=strlen(str);
    LL res=0;
    LL t=Euler(mod);
    if(len<=15){
        for(int i=0;i<len;i++){
            res=res*10+str[i]-'0';
        }
    }
    else{
        for(int i=0;i<len;i++){
            res=res*10+str[i]-'0';
            res%=t;
        }
        if(res<0) res+=mod;
    }
    return res;
}

"""
