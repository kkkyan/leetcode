#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (40.47%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    71.9K
# Total Submissions: 177.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 0
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            n = digits[i]
            new_n = n + add # 进位
            add = 0 # 进位归零

            if new_n >= 10:
                new_n -= 10
                add = 1
            digits[i] = new_n

        # 首位进位
        if add == 1:
            digits.insert(0, 1)
        
        return digits


        

