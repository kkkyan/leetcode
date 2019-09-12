/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 *
 * https://leetcode-cn.com/problems/happy-number/description/
 *
 * algorithms
 * Easy (54.77%)
 * Likes:    156
 * Dislikes: 0
 * Total Accepted:    27.7K
 * Total Submissions: 50.4K
 * Testcase Example:  '19'
 *
 * 编写一个算法来判断一个数是不是“快乐数”。
 * 
 * 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
 * 1。如果可以变为 1，那么这个数就是快乐数。
 * 
 * 示例: 
 * 
 * 输入: 19
 * 输出: true
 * 解释: 
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 * 
 * 
 */
class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = bitSquare(n);
        while(slow != fast){
            slow = bitSquare(slow);
            fast = bitSquare(bitSquare(fast));
        }

        return slow == 1;
    }

    int bitSquare(int n){
        int ret = 0;
        while (n != 0) {
            int bit = n % 10;
            ret += bit * bit;
            n = n / 10;
        }

        return ret;
    }
};

