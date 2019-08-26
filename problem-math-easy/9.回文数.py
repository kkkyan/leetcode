#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.52%)
# Likes:    704
# Dislikes: 0
# Total Accepted:    150.3K
# Total Submissions: 265.9K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
    
    ### 字符串比较
    def solve2(self, x: int) -> bool:
        if (x <0):
            return False
        
        x_s = str(x)
        x_r = x_s[::-1]

        return x_s == x_r
    

    '''
        用头尾比较方法做(不转化字符串)
    '''
    def solve1(self, x: int) -> bool:
        # 负数一定不是
        if (x < 0): 
            return False
    
        if (x < 10):
            return True
        # 不用反转字符串 -> 正数头尾比较 
        # 首先判断x有几位
        div_n = 1
        p_n = 0
        while x >= div_n:
            p_n += 1
            div_n *= 10
        div_n /= 10
        # flag 判断是奇数位还是偶数位
        flag = p_n % 2

        # 对 x 进行头尾判断
        while div_n != flag: 
            header = x // div_n
            ender = x % 10

            if header != ender:
                return False

            # x去除头尾
            x = x % div_n
            x = x // 10

            div_n /= 100
        
        return True


        

