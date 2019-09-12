#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (49.73%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    41.8K
# Total Submissions: 83.9K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 
# 
# 示例:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = []
        

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._min or x < self._min[-1]:
            self._min.append(x)
        else:
            self._min.append(self._min[-1])

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._min.pop()

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]

    def getMin(self) -> int:
        if self._min:
            return self._min[-1]
    

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

