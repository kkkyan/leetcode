#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (30.84%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    39.1K
# Total Submissions: 126.7K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr = s.split()
        # if len(arr) == 0:
        #     return 0
        # return len(arr[-1])
        if len(s) == 0: return 0
        
        ret = 0
        flag = False # flag指示是否遇见了单词
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if flag == False: continue
                else: break
            
            ret += 1
            flag = True
        
        return ret
