/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 求众数
 *
 * https://leetcode-cn.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (60.29%)
 * Likes:    313
 * Dislikes: 0
 * Total Accepted:    66.7K
 * Total Submissions: 110.7K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 * 
 * 你可以假设数组是非空的，并且给定的数组总是存在众数。
 * 
 * 示例 1:
 * 
 * 输入: [3,2,3]
 * 输出: 3
 * 
 * 示例 2:
 * 
 * 输入: [2,2,1,1,1,2,2]
 * 输出: 2
 * 
 * 
 */
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // 拜谒摩尔算法
        int count = 1;
        int target = nums[0];

        for (int i =1; i < nums.size(); i++){
            if (count == 0){
                target = nums[i];
                count = 1;
                continue;
            }

            if (nums[i] == target){
                count++;
            }else{
                count--;
            }
        }

        return target;

        
    }
};

