/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
class Solution {
public:
    /**  
     * O(n) 
     * 做一个map表 key 为 target - num, value为num.index
     * 查 num 是否在 key 内即可
    */
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hash;

        for(int i = 0; i<nums.size(); i++){
          int num = nums[i];
          // 判断hash是否存在 num
          if(hash.count(num)){
            return vector<int>{hash[num], i};
          }else{
            // 不存在 iter, 加入 hashtable
            hash[target - num] = i;
          }
        }

        return vector<int>{};
        
    }
};

