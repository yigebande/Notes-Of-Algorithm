# 541. 反转字符串II

依旧是很简单的题目，不过我的递归版本消耗的空间很大

```c++
class Solution {
public:
    string reverseStr(string s, int k) {
        if (s.length() <= k) {
            reverse(s.begin(), s.end());
            return s;
        } else if (s.length() < 2 * k) {
            reverse(s.begin(), s.begin() + k);
            return s;
        }
        string preTwoK = s.substr(0, 2 * k);
        string left = s.substr(2 * k, -1);
        reverse(preTwoK.begin(), preTwoK.begin() + k);
        return preTwoK + reverseStr(left, k);
    }
};
```