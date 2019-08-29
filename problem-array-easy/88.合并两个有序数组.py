#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (45.08%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    64.4K
# Total Submissions: 142.8K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 : return        
        
        psave = n + m - 1
        pm = m - 1
        pn = n - 1
        
        while pm >= 0  and pn >= 0:
            if nums1[pm] > nums2[pn]:
                nums1[psave] = nums1[pm] 
                pm -= 1
            else:
                nums1[psave] = nums2[pn] 
                pn -= 1
            psave -= 1
        
        # nums1 还有剩余的时候，
        # 即nums2已经就位，那么nums1剩余元素也是就位的
        # 只处理 nums2 剩余情况就好
        if pn >= 0: 
            for i in range(pn+1):
                nums1[i] = nums2[i]



        

