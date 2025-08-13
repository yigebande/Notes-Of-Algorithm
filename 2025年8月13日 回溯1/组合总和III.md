# 216. 组合总和III

比较简单的一道题目，主要是要用`start + 1`防止重复。

```c++
class Solution {
public:
    void backTracking(int k, int n, int start, vector<int>& vec, vector<vector<int>>& res) {
        if (n < 0) return;
        if (k == 0) {
            if (n == 0) res.push_back(vec);
            return;
        }
        for (int i = start; i <= 9; i++) {
            vec.push_back(i);
            backTracking(k - 1, n - i, i + 1, vec, res);
            vec.pop_back();
        }   
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> vec;
        backTracking(k, n, 1, vec, res);
        return res;
    }
};
```