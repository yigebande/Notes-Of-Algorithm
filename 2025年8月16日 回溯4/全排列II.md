# 47. 全排列

就是比全排列多了一个每层的去重，换句话说是同一个位置选择的去重。

```c++
class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    int umap[8] = {0};
    void backTracking(vector<int>& nums) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        int used[21] = {0};
        for (int i = 0; i < nums.size(); i++) {
            if (umap[i]) continue;
            if (used[nums[i] + 10] == 0) {
                used[nums[i] + 10] = 1;
                path.push_back(nums[i]);
                umap[i] = 1;
                backTracking(nums);
                path.pop_back();
                umap[i] = 0;
            }
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        backTracking(nums);
        return res;
    }
};
```

`umap`用于当前位置的选择避免和前面位置的元素相等。
```c++
int umap[8] = {0};

for (int i = 0; i < nums.size(); i++) {
    if (umap[i]) continue;
    ...
}
```

`used`用于当前位置避免选择到重复的元素，比如`nums = [1, 1, 2]`，在第一个位置进行选择时，避免选两次1
```c++
int used[21] = {0};
for (int i = 0; i < nums.size(); i++) {
    if (umap[i]) continue;
    if (used[nums[i] + 10] == 0) {
        used[nums[i] + 10] = 1;
        path.push_back(nums[i]);
        umap[i] = 1;
        backTracking(nums);
        path.pop_back();
        umap[i] = 0;
    }
}
```