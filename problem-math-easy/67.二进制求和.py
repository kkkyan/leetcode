#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (50.15%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 72.3K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 比较长度，对小字符串长度进行遍历
        short_len = 0
        pstr = None
        if len(a) <= len(b):
            short_len = len(a)
            pstr = b
        else:
            short_len = len(b)
            pstr = a
            
        ret = ""
        # 计算公共部分
        add = 0
        for i in range(-1,-short_len-1,-1):
            # 相加
            n = int(a[i]) + int(b[i]) + add
            add = 0
            # 进位
            if n >= 2:
                n -= 2
                add = 1
            
            # 合并结果
            ret = str(n) + ret
        
        res_len = abs(len(a) - len(b))
        # 计算剩余部分
        resn = pstr[0:res_len]
        for i in range(res_len-1, -1, -1):
            n = int(pstr[i]) + add
            add = 0
            if n >= 2:
                # 有进位
                n -= 2
                add = 1

            ret = str(n) + ret

        if add == 1:
            return "1"+ ret
        else:
            return ret



            



