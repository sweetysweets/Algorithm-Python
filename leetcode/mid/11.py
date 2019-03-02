"""

11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49



[1,1]
[1,2,3]

first find how to compute area

min(height1,height2)*length

think from variables
change from max length to ..


"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        i = 0
        maxArea = 0
        while i < j and i < len(height) - 1 and j > 0:
            height1 = height[i]
            height2 = height[j]
            tmpArea = (j - i) * (height1 if height1 < height2 else height2)
            if maxArea < tmpArea:
                maxArea = tmpArea
            if height1 > height2:
                j -= 1
            else:
                i += 1
        return maxArea
    
 """
 class Solution:
    def maxArea(self, height):
        len_h = len(height)
        i = 0
        k = -1
        s=[]
        while len_h+k-i>=1:
            s.append(min(height[i],height[k])*(len_h+k-i))
            if height[i] <= height[k]:
                i += 1
            else:
                k -= 1
        return max(s)
        
        
暴力
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        for i in range(len(height)):
            for j in range(i,len(height)):
                tmpArea = (j-i)*min(height[i],height[j])
                if maxArea < tmpArea:
                    maxArea = tmpArea
        return maxArea
                
       
       
       
可能很多同学会跟我一样疑惑双向指针为什么不会错过最优解，以下是我的理解. 首先按照解的逻辑是，l,r两个指针，l指向的H[l]比H[r]要小，然后让l指针往左移动， 那么就分析漏掉解。 漏掉就是那些l指针不动，丢失的就是r在这个范围(l<...<r)的解. 那么分析一下这个范围的解，如果我们保持H[l]较小的值不动，去移动H[r]较大的值会出现什么情况？

H[r-1] > H[r],这种情况，毋庸置疑，作为底的(r - l）减少了，由于新的H[r-1]比H[r]更大，那么高必然还是H[l]这个较小的值，所以这个解一定比之前的那个解更小的水容量。
H[r-1] < H[r] 并且H[r-1]>H[l]情况，这种情况其实跟上面一种是一样的，因为相当于底减少了1，高不变，水容量肯定更小。
H[r-1] < H[l]，这种情况，底减少了1，高从本来的H[l]变成了更小的H[r-1]，那么水容量肯定变得更小。
以上三种移动更大的H[r]的情况所得到的解都是得到更小的水容量，然后我们在分析移动更小的l指针会得到什么情况.

最坏的情况，新的H[l+1]比H[l]更小，那么肯定水容量变小.
H[l]<H[l+1]<H[r]，这个情况就有可能出现更优解，因为底虽然减少了，但是最为高的H[l+1]增大的值之后计算出来的水容积是可能比之前那个解大的.
H[l+1]>H[r],这个情况其实跟上面类似，只不过高变成r指针的H[r],一样可以理解为底变小，高变大。
综上，如果移动更小指针的高度，可能得到比原始解更优的解，如果移动更大指针高度，就必然得到比原始解更差的解。这就是我对于这个答 有序列表案指针移动的理解     
        
 """
