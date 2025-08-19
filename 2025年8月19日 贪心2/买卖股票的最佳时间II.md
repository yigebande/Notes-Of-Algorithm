# 122. 买卖股票的最佳时机II

没想出来思路，看的文章讲解做的

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sum = 0;
        for (int i = 1; i < prices.size(); i++) {
            sum += max(prices[i] - prices[i - 1], 0);
        }
        return sum;
    }
};
```