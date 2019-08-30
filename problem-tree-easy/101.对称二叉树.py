#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (48.13%)
# Likes:    422
# Dislikes: 0
# Total Accepted:    50.8K
# Total Submissions: 105.4K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 初步思想，如果一棵树是对称的，那么每一层都是对称的
        if root is None: return True
        
        queue = [root]
        while queue != []:
            # 首先判断 queue 是对称的
            lenQueue = len(queue)
            for i in range(lenQueue // 2):
                left = queue[i]
                right = queue[lenQueue - 1 -i]

                if left is None or right is None:
                    if left != right:   return False
                elif left is not None and right is not None:
                    if left.val != right.val:   return False

            # 推出 queue 全部节点，加入新节点（层）
            newLayer = []
            for r in queue:
                if r is not None:
                    newLayer.append(r.left)
                    newLayer.append(r.right)
            queue = newLayer
        
        return True

        

