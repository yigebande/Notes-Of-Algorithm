# 123. 买卖股票的最佳时机 III
做了一个多小时，终于做出来了。
```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) return 0;
        // 只买卖一次的情况，和121. 的思路是完全一样的
        vector<int> dpOne(prices.size(), 0);
        int minimum = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            dpOne[i] = max(dpOne[i - 1], prices[i] - minimum);
            minimum = min(minimum, prices[i]);
        }
        // 如果只买卖一次的最大收益全都是0，那么没必要买卖第二次
        if (dpOne.back() == 0) return 0;
        // 买卖第二次的情况
        // 取下标为i + 1到末尾的prices元素中的最大值减去prices[i]
        // 如果有比dpTwo[i + 1]更大的，说明可以在这一天买入，更新最大利益；
        // 否则不应该在这一天买入，不过从这一天到最后一天可获得的最大利润不变，
        // 依然可以是dpTwo[i + 1]
        vector<int> dpTwo(prices.size(), 0);
        int maximum = prices.back();
        for (int i = prices.size() - 2; i >= 1; i--) {
            dpTwo[i] = max(dpTwo[i + 1], maximum - prices[i]);
            maximum = max(maximum, prices[i]);
        }
        // 取买卖一次所获得的最大利益
        int res = dpOne.back();
        for (int i = 1; i < prices.size() - 1; i++) {
            res = max(res, dpOne[i] + dpTwo[i + 1]);
        }
        return res;
    }
};
```
## 思路
比较难的是的是第二次买卖的情况，我想了很久。

我刚开始想，能不能实现一个算法，分别查找一个数组中尽可能在右边的最小值，和尽可能在右边的最大值，但是我想不出来。

然后我就在想，第二次买卖能否根据第一次买卖的情况来进行递推？

画了一下图，发现第二次买卖的情况和第一次买卖没有非常明显的联系，因为并不知道第二次买卖是在什么时候买入。

最后我想到了从后往前遍历，每次取最大值减去当前检查的元素`prices[i]`，类似第一次买卖逆着来的情况。

这样做的话，第一次买卖到第`i`天有符合题目条件最大收益，从第`i + 1`天开始到最后一天的买卖也有符合题目条件的最大收益。

关于遍历起点和终点的一些探讨，第一次买卖总是在第2天才有可能有收益的，所以遍历起点为数组下标`1`，如果只有一次买卖，那么可能在最后一天卖出，所以遍历终点可以到达数组末尾。

如果有第二次买卖，那么说明已经有第一次买卖了，第一次最早卖出是第2天，这里我的第二次买卖的后序遍历终点为数组下标`1`纯属手误，不过不影响最终结果。