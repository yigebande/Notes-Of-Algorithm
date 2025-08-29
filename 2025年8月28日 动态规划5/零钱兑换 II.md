# 518. 零钱兑换 II

## 思路
第一道完全背包正式题，想了很久，最终没有做出来。

最开始我在函数的第一行写了一段这样的代码：
```c++
sort(coins.begin(), coins.end());
if (coins[0] > amount) return 0;
```

我用这个案例去测试，发现没有什么问题
```
amount = 1, coins = [2, 5]
```

但是一提交就发现，如果`amount = 0`的话，最后应该返回`1`。

我最开始用一维`dp`去做，想要找到规律，但是找到的规律貌似是01背包的。

后来我觉得用一维`dp`做不利于思考，然后转向二维`dp`，还在Excel中画了表格来推导，但是无论如何总觉得推导的递推公式不合理。

这个不合理主要体现在**初始化没有做对**。

因为我第一列的初始化为0，哪怕第一行的初始化是正确的，后面也做不对。

下面是对代码进行分析。

## 二维`dp`
```c++
#include<print>
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<uint64_t>> dp(coins.size(), vector<uint64_t>(amount + 1, 0));
        // 初始化第一行
        for (int j = 0; j <= amount; j++) {
            dp[0][j] = j % coins[0] == 0 ? 1 : 0;
        }
        // 初始化第一行
        for (int i = 0; i < coins.size(); i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i < coins.size(); i++) {
            for (int j = 0; j <= amount; j++) {
                if (j < coins[i]) dp[i][j] = dp[i - 1][j];
                else dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j];
            }
        }
        return dp[coins.size() - 1][amount];
    }
};
```

1. 这个`uint64_t`我是没想到，看了评论才知道要用`unsigned long long`。
2. 初始化第一行不必多说，初始化第一列主要是为了让`amount == 0`时有一个组合，就是什么都不选。
3. 这里的`j`是从0开始遍历，因为`j < coins[i]`的时候，当前行要继承上一行的情况；除此之外，则要考虑当前行当前列的前`coins[i]`个和正上方的情况。

## 一维`dp`
```c++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<uint64_t> dp(amount + 1, 0);
        for (int i = 0; i <= amount; i++) {
            dp[i] = i % coins[0] == 0 ? 1 : 0; 
        }
        for (int i = 1; i < coins.size(); i++) {
            for (int j = coins[i]; j <= amount; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }
        return dp[amount];
    }
};
```
一维`dp`比二维`dp`少很多操作，主要是因为一维`dp`的状态不进行修改时，是“自动”继承上一行的情况的。