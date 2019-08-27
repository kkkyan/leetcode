#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.72%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    75.7K
# Total Submissions: 195.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        if len(haystack) < len(needle) : return -1
        
        start = 0

        while start < len(haystack):
            # 按字符比对
            for i in range(len(needle)):
                # 如果偏移超过长度
                if i + start == len(haystack):
                    return -1
                
                # 没有比对成功，start挪下一个
                if haystack[start + i] != needle[i]:
                    start += 1
                    break
                else:
                    # 比对成功，看看是不是最后一个了
                    if i == len(needle) - 1:
                        return start

        return -1


        

