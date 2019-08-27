#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.52%)
# Likes:    669
# Dislikes: 0
# Total Accepted:    112.1K
# Total Submissions: 324.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # python技巧：使用 zip与set
        res = ""
        # zip(*) 解压矩阵
        for c in zip(*strs):
            if len(set(c)) > 1:
                break
            
            res += c[0]
        
        return res
        

    # 第一次实现的方法
    # 比较每个字符串的位置，一个一个比
    # T = o(len(strs)) * o(min(str_len))
    def solve_origin(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        res = ""
        arr_len = len(strs)
        p = 0
        while True:
            last = None
            for s in strs:
                # 最短的s已经计算完毕
                if p >= len(s):
                    return res
                
                c = s[p]
                if last == None:
                    last = c
                else:
                    # 这个字符和上次不相等
                    if last != c:
                        return res
                
            # 一轮计算完毕
            p += 1
            res += last


        

