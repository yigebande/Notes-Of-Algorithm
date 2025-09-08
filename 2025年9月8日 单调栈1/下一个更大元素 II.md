# 503. 下一个更大元素 II
就是把原数组“复制”一份放在后面，然后进行遍历
```c++
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res(nums.size(), -1);
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums.size() + nums.size(); i++) {
            if (i < nums.size()) {
                while (!st.empty() && nums[i] > nums[st.top()]) {
                    res[st.top()] = nums[i];
                    st.pop();
                }
                st.push(i);
            } else {
                while (!st.empty() && nums[i - nums.size()] > nums[st.top()]) {
                    res[st.top()] = nums[i - nums.size()];
                    st.pop();
                }
                st.push(i - nums.size());
            }
        }
        return res;
    }
};
```