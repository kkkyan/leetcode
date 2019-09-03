#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (39.83%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 69.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.BFS(root)
    
    # 广度优先
    # 遇见的第一个叶子节点即为最小深度点
    def BFS(self, root):
        if not root: return 0
        
        deep = 0
        stack = [(1, root)]
        while stack:
            deep, node = stack.pop(0)
            if not node.left and not node.right:
                return deep

            if node.left:
                stack.append((deep+1, node.left))
            if node.right:
                stack.append((deep+1, node.right))


        
        

