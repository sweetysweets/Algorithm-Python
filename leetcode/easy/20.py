
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""
my_dict = {')':'(','}':'{',']':'['}
class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        for i in range(len(s)):
            tmp = s[i]
            if tmp in my_dict.values():
                stack.append(tmp)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == my_dict[tmp]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0




if __name__ == '__main__':
    S =Solution()
    S.isValid("()")
