#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (40.77%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    49.7K
# Total Submissions: 121.6K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True
        
        import re
        s = re.sub(r"[^a-zA-Z0-9]","",s)
        s = s.lower()

        start = 0
        end = len(s) - 1
        while start < end:
            while s[start] == " " and start < end:
                start += 1
            while s[end] == " " and start < end:
                end -= 1
            
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        
        return True

        

