# 1005. K次取反后最大化的数组和

没有啥好的思路，就当我以为连这道简单题都要看答案的时候，想到了一个很笨的方法。

```c++
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        while (k > 0) {
            sort(nums.begin(), nums.end());
            nums[0] = -nums[0];
            k--;
        }
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        return sum;
    }
};
```

`k`在逐渐减小的过程中，每次都对`nums`进行排序，并且每次取最小值进行取反。

文章讲解的方法更加巧妙

```c++
class Solution {
    static bool cmp(int a, int b) {
        return abs(a) > abs(b);
    }
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), cmp);
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < 0 && k > 0) {
                nums[i] *= -1;
                k--;
            }
        }
        int sum = 0;
        if (k % 2 == 1) nums[nums.size() - 1] *= -1;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        return sum;
    }
};
```

让`nums`中的元素按照绝对值大小排好序，对小于0的元素进行取反。

完毕后，检查`k % 2`的情况，如果为1，那么只对最小的元素取反即可；如果为0，说明已经尽可能对那些绝对值大的负数取反了，不处理。