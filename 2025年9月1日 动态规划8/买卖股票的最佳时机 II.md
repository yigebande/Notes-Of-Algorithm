# 122. 买卖股票的最佳时机 II
和121. 有点像

这里之前贪心讲过，就是取全部第`i - 1`天买入，第`i`天卖出所得到的利益之和，当然，取正数之和。
```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> dp(prices.size(), 0);
        for (int i = 1; i < prices.size(); i++) {
            dp[i] = prices[i] - prices[i - 1] > 0 ? 
                    dp[i - 1] + prices[i] - prices[i - 1] : dp[i - 1];
        }
        return dp.back();
    }
};
```