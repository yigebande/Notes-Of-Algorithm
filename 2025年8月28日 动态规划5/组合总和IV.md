# 377. 组合总和IV
最难绷的一集，因为没看零钱兑换II的视频讲解，所以不知道**外层遍历物品，内层遍历背包** 和 **外层遍历背包，内层遍历物品** 有什么区别。

我看了文章讲解又看了视频讲解，视频讲解中讲到组合与排列的原理我看了很久都没看懂，看了评论区和弹幕有点似懂非懂，最后自己在平板上推演了一下，理解更加深刻了。

```c++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<vector<int>> dp(nums.size(), vector<int>(target + 1, 0));
        dp[0][0] = 1;
        for (int i = 0; i <= target; i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (j == 0 && i == 0) continue;
                if (i >= nums[j]) {
                    for (int k = 0; k <= j; k++) {
                        if (i >= nums[k] && dp[j][i] <= INT_MAX - dp[j][i - nums[k]])
                            dp[j][i] += dp[j][i - nums[k]];
                    }
                } else {
                    if (j >= 1)
                        dp[j][i] = dp[j - 1][i];
                }
            }
        }
        return dp[nums.size() - 1][target];
    }
};
```

我原本用的二维`dp`去推演，发现二维`dp`要进行的额外操作比较多，比如里面的
```c++
if (i == 0 && j == 0) continue;
...
if (j >= 1) 
    dp[j][i] = dp[j - 1][i];
```