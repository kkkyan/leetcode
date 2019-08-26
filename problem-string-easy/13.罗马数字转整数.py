#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (58.86%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    87.4K
# Total Submissions: 148.5K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
# 
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 
# 
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 
# 
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 
# 示例 1:
# 
# 输入: "III"
# 输出: 3
# 
# 示例 2:
# 
# 输入: "IV"
# 输出: 4
# 
# 示例 3:
# 
# 输入: "IX"
# 输出: 9
# 
# 示例 4:
# 
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 
# 
# 示例 5:
# 
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 
#
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        # 处理只有1位情况
        if len(s) == 1:
            return dic[s[0]]

        res = 0
        p = 0
        # 只处理前 len(s) - 1 位，最后一位单独处理
        while p < len(s) - 1:
            c = s[p]
            add = s[p+1]
            # 每种情况
            if c == "I":
                # 4 or 9
                if add in ["V", "X"]:
                    res += (dic[add] - 1)
                    p += 1
                else:
                    res += dic[c]
            elif c == "X":
                # 40 90
                if add in ["L", "C"]:
                    res += (dic[add] - 10)
                    p += 1
                else:
                    res += dic[c]
            elif c == "C":
                # 400 900
                if add in ["D", "M"]:
                    res += (dic[add] - 100)
                    p += 1
                else:
                    res += dic[c]
            else:
                res += dic[c]
            
            p += 1

        # 处理最后一位单字
        if (p < len(s)):
            c = s[-1]
            res += dic[c]

        return res
        

