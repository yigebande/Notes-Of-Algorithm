# 93. 复原IP地址

比131. 切割回文串稍微难一点

```c++
class Solution {
public:
    vector<string> res;
    int dotCount = 0;

    bool isValid(string s, int start, int end) {
        if (end > 3 || end < 1) return false;
        if (s[start] == '0' && end > 1) return false;
        string str = s.substr(start, end);
        int num = stoi(str);
        return num >= 0 && num <= 255;
    }
    
    void backTracking(string s, const string address, int start) {
        if (dotCount > 3) return;
        if (dotCount == 3 && start >= s.length()) {
            res.push_back(address);
        }
        for (int i = start; i < s.length(); i++) {
            if (isValid(s, start, i - start + 1)) {
                if (i < s.length() - 1) {
                    dotCount++;
                    backTracking(s, address + s.substr(start, i - start + 1) + ".", i + 1);
                    dotCount--;
                } else {
                    backTracking(s, address + s.substr(start, i - start + 1), i + 1);
                }
            }
        }
    }

    vector<string> restoreIpAddresses(string s) {
        backTracking(s, "", 0);
        return res;
    }
};
```

首先要判断选取的字符串是否在[1, 255]中
```c++
bool isValid(string s, int start, int end) {
    // 这里的end相当于字符串的长度
    // 刚开始我没做长度判断，总是导致stoi抛出超出范围的异常
    if (end > 3 || end < 1) return false;
    // 排除存在前导0的情况，注意这里必须是'0'，不能是"0"
    if (s[start] == '0' && end > 1) return false;
    string str = s.substr(start, end);
    int num = stoi(str);
    return num >= 0 && num <= 255;
}
```

回溯主体
```c++
void backTracking(string s, const string address, int start) {
    // 记录截取的address中的点的个数，如果超过三，不符合要求
    if (dotCount > 3) return;
    // 如果刚好有三个点，并且start到了s的末尾，就说明这个地址是合法的，插入到res中
    if (dotCount == 3 && start >= s.length()) {
        res.push_back(address);
    }
    for (int i = start; i < s.length(); i++) {
        if (isValid(s, start, i - start + 1)) {
            if (i < s.length() - 1) {
                dotCount++;
                backTracking(s, address + s.substr(start, i - start + 1) + ".", i + 1);
                dotCount--;
            } else {
                backTracking(s, address + s.substr(start, i - start + 1), i + 1);
            }
        }
    }
}
```