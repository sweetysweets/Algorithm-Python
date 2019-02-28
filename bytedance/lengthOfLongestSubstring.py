class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        q = 1
        max = 1
        result = []
        while p < len(s):

            while q < len(s):
                if s[p] == s[q]:
                    p += 1
                    if not result or result[-1]<max:
                        result.append(max)
                    max = 0
                else:
                    max += 1
                q += 1
        return result[0]

if __name__ == '__main__':
    S =Solution()
    s = 'abcabcbb'
    print(S.lengthOfLongestSubstring(s))

