# 40. 组合总和II

突发奇想+误打误撞做出来的，做完之后我都不太清楚为什么能通过。

```c++
class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    void backTracking(vector<int>& candidates, int target, int start) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            path.push_back(candidates[i]);
            backTracking(candidates, target - candidates[i], i + 1);
            path.pop_back();
        }
        return;
    }


    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backTracking(candidates, target, 0);
        return res;
    }
};
```

首先，我对`candidates`进行排序。

我最开始想到的是，在一串连续的相同的元素中，最左边的元素掌握着“最大权力”，因为最左边的元素可以和右边的元素任意组合，我想选就选，不想选就不选。

而那些非最左边的元素，因为选出来的组合可能与前面已经选好的组合重复，所以不应该再以他们为开头进行遍历。

下面举个例子。

`candidate = [1, 1, 1, 2, 2, 2, 5], target = 5`

进行第一次的选取的流程如下所示：

蓝色元素中的`start`表示当前循环最开始所选取的元素，蓝色元素右边的元素为进入下一层递归的`candidates`。

![](images/first%20choice0.drawio.svg)

第一次选取完以后，进行第二次选取：

![](images/first%20choice2.drawio.svg)

![](images/first%20choice3.drawio.svg)

简而言之，我在最开始的时候选了最左边的1的时候，我就已经能够找出所有的包含1的符合条件的集合。

如果有一个符合条件的集合里面只有一个1，那么如果再取第二个1进行查找的话，必然会出现重复。

因此，每次查找总是以一串连续元素的最左边的元素开始查找，这样就肯定能够找到所有包含该元素的符合条件的集合。