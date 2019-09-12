/*
 * @lc app=leetcode.cn id=203 lang=cpp
 *
 * [203] 移除链表元素
 *
 * https://leetcode-cn.com/problems/remove-linked-list-elements/description/
 *
 * algorithms
 * Easy (42.17%)
 * Likes:    281
 * Dislikes: 0
 * Total Accepted:    37.5K
 * Total Submissions: 88.6K
 * Testcase Example:  '[1,2,6,3,4,5,6]\n6'
 *
 * 删除链表中等于给定值 val 的所有节点。
 * 
 * 示例:
 * 
 * 输入: 1->2->6->3->4->5->6, val = 6
 * 输出: 1->2->3->4->5
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* ret = new ListNode(-1);
        ret->next = head;
        ListNode* p = ret;
        while(p->next){
            if(p->next->val == val){
                ListNode* n = p->next;
                p->next = p->next->next;
                delete n;
            }else{
                p = p->next;
            }
        }
        
        return ret->next;
    }
};

