# 347. 前K个高频元素

完全不会做，虽然我想到了可以用优先队列，但一直以来我都是用Python和MATLAB中自带或者让AI写好的优先队列，C++的优先队列我真没接触过。

看了视频也不会。

很多C++的特性我完全不知道，比如说`bool operator()`重载操作符

还有`priority_queue`的排序函数，以及遍历`unordered_map`的迭代器，还有`it`是一个指针

这些都不知道

答案基本是抄文章讲解的

```c++
class Solution {
public:
    class MyComparison {
    public:
        bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
            return lhs.second > rhs.second;
        }
    };
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res(k);
        unordered_map<int, int> umap;
        for (int i = 0; i < nums.size(); i++) {
            umap[nums[i]]++;
        }
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, MyComparison> pri_q;
    for(unordered_map<int, int>::iterator it = umap.begin(); it != umap.end(); it++) {
        pri_q.push(*it);
        if (pri_q.size() > k) {
            pri_q.pop();
        }
    }
    for (int i = k - 1; i >= 0; i--) {
        res[i] = pri_q.top().first;
        pri_q.pop();
    }
     return res;   
    }
};
```