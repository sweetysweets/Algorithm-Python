
# 第一题 ：给一个数组，求最长的山谷。
#
# 例：[1, 2, 5, 3, 2, 3, 4,1]
#
# 最长的山谷是 5 3 2 3 4，长度是5.
#
# 本题类似于lettcode 845，求最长山峰。
#
# 以每个数为中心向左右分别枚举，记录最长的长度。
# trick:笔试的输入很坑，没有给定输入长度，导致输入处理很麻烦，导致程序出错。


# class Solution {
#     public int longestMountain(int[] A) {
#         int cnt = 0;
#         int l, r;
#         for(int i = 1; i < A.length-1; i++){
#             if(A[i-1] < A[i] && A[i] > A[i+1]){
#                 l = i-1;
#                 r = i+1;
#                 while(l >= 1 && A[l]>A[l-1]) l--;
#                 while(r < A.length-1 && A[r]>A[r+1]) r++;
#                 cnt = Math.max(cnt, r-l+1);
#             }
#         }
#         return cnt;
#     }
# }