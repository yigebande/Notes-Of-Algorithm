# KMP算法学习

## 前缀函数

此函数给出字符串`s` **最长匹配真前后缀的长度**，记为$\pi_i$，这里的 **真** 表示前缀和后缀中都不包含`s`本身，类似 **真子集** 对于 **子集** 的关系。

| 下标   | 0    | 1    | 2    | 3    | 4     | 5      |
| ------ | ---- | ---- | ---- | ---- | ----- | ------ |
| 字符串 | A    | T    | A    | A    | T     | A      |
| 前缀   | A    | AT   | ATA  | ATAA | ATAAT | ATAATA |
| $\pi$  | 0    | 0    | 1    | 1    | 2     | 3      |

- $\pi_i = $第$i$个前缀（`s`的子串）的最长匹配真前后缀的长度

- 模式串：ATAATA
- 主串：AGCATAATAATTAA

```c++
vector<int> pi(str.size());
for (int i = 1; i < str.size(); i++) {
    int len = pi[i - 1];
    while (len != 0 && str[i] != str[len]) {
        len = pi[len - 1];
    }
    if (str[i] == str[len]) {
        pi[i] = len + 1;
    }
}
```

