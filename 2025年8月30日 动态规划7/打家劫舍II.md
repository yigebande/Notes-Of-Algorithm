# 213. 打家劫舍II

本质上还是打家劫舍，只是需要划分头尾来考虑

省空间来做会导致`dp`的数组下标和`nums`的数组下标不对应，做起来很麻烦。
```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);
        // 没有必要为了省空间而用nums.size() - 1
        vector<int> dp(nums.size(), 0);
        // 从第0位到第nums.size() - 2位
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        int maximum = dp[dp.size() - 2];
        // 从第1位到第nums.size() - 1位
        dp[1] = nums[1];
        dp[2] = max(nums[1], nums[2]);
        for (int i = 3; i < nums.size(); i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        return max(maximum, dp.back());
    }
};
```