#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (34.45%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 34.7K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        # 26一循环
        ret = ""
        while n != 0:
            offset = n % 26
            if offset == 0:
                char = "Z"
                n = n // 26 - 1
            else:
                char = chr(ord('A') + n % 26 - 1)
                n = n // 26

            ret = char + ret

        return ret
        

