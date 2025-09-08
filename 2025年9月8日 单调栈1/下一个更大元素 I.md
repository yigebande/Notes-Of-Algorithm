# 496. 下一个更大元素 I
原本以为是一道难题，但是思考了一下发现其实很好做
```c++
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> umap;
        vector<int> res(nums1.size(), -1);
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums2.size(); i++) {
            while (!st.empty() && nums2[i] > nums2[st.top()]) {
                umap[nums2[st.top()]] = nums2[i];
                st.pop();
            }
            st.push(i);
        }
        for (int i = 0; i < nums1.size(); i++) {
            if (umap[nums1[i]] != 0) {
                res[i] = umap[nums1[i]];
            }
        }
        return res;
    }
};
```

## 思路
因为`nums1, nums2`都没有重复元素，所以可以想到用哈希表来建立数组中元素到 **下一个更大元素** 的映射。

所以就是先在`nums2`中找出每个元素的下一个更大元素，建立好哈希表后，再遍历`nums[1]`中的元素去寻找。  