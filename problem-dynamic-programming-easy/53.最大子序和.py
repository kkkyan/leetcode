#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.00%)
# Likes:    1150
# Dislikes: 0
# Total Accepted:    86K
# Total Submissions: 182.6K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        s = 0
        for n in nums:
            # s >=0 对后续结果有意义
            if s >= 0:
                s += n
            # s < 0 对后续结果没有意义
            else:
                s = n

            ret = max(ret, s)

        return ret
        

