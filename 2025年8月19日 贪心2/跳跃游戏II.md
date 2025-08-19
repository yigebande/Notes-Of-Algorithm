# 45. 跳跃游戏II

不看文章讲解真的做不出来，根本想不出来更新`nextCondition`和`currCondition`的情况。

```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int res = 0;
        int nextCondition = 0;
        int currCondition = 0;    
        for (int i = 0; i < nums.size(); i++) {
            nextCondition = max(nextCondition, i + nums[i]);
            if (i == currCondition) {
                res++;
                currCondition = nextCondition;
                // 更新之后的currCondition
                if (currCondition >= nums.size() - 1) break;
            }
        }
        return res;
    }
};
```

`currCondition`初始化为0，这里有个隐性的`i == currCondition`，说明`nums[0]`不是最后一个元素，应该往后跳一步。