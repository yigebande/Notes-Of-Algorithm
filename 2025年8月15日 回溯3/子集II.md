# 90. 子集II

就是多了去重的步骤

```c++
class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    void backTracking(vector<int>& nums, int start) {
        res.push_back(path);
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            path.push_back(nums[i]);
            backTracking(nums, i + 1);
            path.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        backTracking(nums, 0);
        return res;
    }
};
```