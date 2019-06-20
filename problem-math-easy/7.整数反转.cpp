/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */
class Solution {
public:
    int reverse(int x) {
        int res = 0;

        // 除10取鱼法
        while(x != 0){
            int temp = x % 10;

            res = res * 10 + temp;
            x = x / 10;
        }

        if((x<0 && res>0) || (x>0 && res<0)){
            return 0;
        }

        return x>=0?res:-res;

    }
};

