#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (54.46%)
# Likes:    218
# Dislikes: 0
# Total Accepted:    34K
# Total Submissions: 62.4K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两棵树同时扫描，广度优先，比对扫描节点
        pQueue = [p]
        qQueue = [q]

        # 不为空继续扫描
        while pQueue != [] and qQueue != []:
            # 取节点
            pRoot = pQueue.pop(0)
            qRoot = qQueue.pop(0)
            # 对比
            # 如果其中一个不为空
            if (pRoot == None and qRoot != None):
                return False
            elif (pRoot != None and qRoot == None):
                return False
            # 如果都不为空
            elif (pRoot != None and qRoot != None):
                if pRoot.val != qRoot.val:
                    return False

            # 添加叶子
            if pRoot != None:
                pQueue.append(pRoot.left)
                pQueue.append(pRoot.right)
            if qRoot != None:
                qQueue.append(qRoot.left)
                qQueue.append(qRoot.right)

        # 当且仅当所有队列都为空
        return pQueue == [] and qQueue == []
        

