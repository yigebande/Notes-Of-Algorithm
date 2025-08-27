# 1049. 最后一块石头的重量 II
完全想不到是找出两个包含不同元素的子集，让两个子集分别总和之差最小。

```c++
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        if (stones.size() == 1) return stones[0];
        int sum = 0;
        for (const auto& elem: stones) {
            sum += elem;
        }
        int half = sum / 2;
        vector<int> dp(1501, 0);
        for (int i = stones[0]; i <= half; i++) {
            dp[i] = stones[0];
        }
        for (int i = 1; i < stones.size(); i++) {
            for (int j = half; j >= stones[i]; j--) {
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }
        return sum - dp[half] - dp[half];
    }
};
```