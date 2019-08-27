#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.37%)
# Likes:    1006
# Dislikes: 0
# Total Accepted:    112.3K
# Total Submissions: 285K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(":")", "{":"}", "[":"]"
        }
        stack = []

        for c in s:
            # 左括号压栈
            if c in pairs.keys():
                stack.append(c)
            else:
                # 右括号出栈
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if pairs[top] != c:
                    return False

        if len(stack) > 0:
            return False
        
        return True
        

