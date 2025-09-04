# 188. 买卖股票的最佳时机 IV
由123. 买卖股票的最佳时机 III照葫芦画瓢得来

```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<int> dp(2 * k, 0);
        for (int i = 0; i < dp.size(); i += 2) {
            dp[i] = -prices[0];
        }
        for (int i = 1; i < prices.size(); i++) {
            for (int j = dp.size() - 1; j >= 0; j--) {
                if (j == 0) {
                    dp[j] = max(dp[j], -prices[i]);
                } else {
                    bool sold = j % 2;
                    if (sold) dp[j] = max(dp[j], dp[j - 1] + prices[i]);
                    else dp[j] = max(dp[j], dp[j - 1] - prices[i]);
                }
            }
        }
        return dp.back();
    }
};
```

最核心的思路在于递推公式
```c++
// 如果持有
dp[j][k] = max(dp[j - 1][k], dp[j - 1][k - 1] - prices[i])

// 如果不持有
dp[j][k] = max(dp[j - 1][k], dp[j - 1][k - 1] + prices[i])
```

相信最后一个更新的元素总是期望中的最大值。