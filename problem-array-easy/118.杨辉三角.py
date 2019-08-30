#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (63.69%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    34.6K
# Total Submissions: 54.4K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1], [1,1]]
        if numRows <= 2: return ret[:numRows]
        
        for n in range(3,numRows+1):
            res = [1]
            lastLayer = ret[n-2]
            for i in range(len(lastLayer)-1):
                res.append(lastLayer[i]+lastLayer[i+1])
            res.append(1)
            ret.append(res)
        
        return ret



        

