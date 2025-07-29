# 454. 四数相加

刚开始做的时候没有一点思路，看了文章讲解

文章讲解提供的思路是，先用一个`map`来存储`<(nums1的元素 + nums2的元素), 和出现的次数>`，这样子很好地避免了`map`的`key`重复带来的麻烦。

然后再检查`map`中是否有`-(c + d)`的`key`，如果有，那么令`count`加上`map[-(c+d)]`，最后返回`count`

```c++
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                int sum = nums1[i] + nums2[j];
                if (mp.find(sum) == mp.end()) {
                    mp.insert({sum, 1});
                } else {
                    mp[sum]++;
                }
            }
        }
        int count = 0;
        for (int i = 0; i < nums3.size(); i++) {
            for (int j = 0; j < nums4.size(); j++) {
                int sum = nums3[i] + nums4[j];
                if (mp.find(-sum) != mp.end()) {
                    count += mp[-sum];
                }
            }
        }
        return count;
    }
};
```