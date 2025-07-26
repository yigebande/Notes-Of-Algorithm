#### 704. 二分查找

我在很久之前就看到了卡哥的讲解二分查找的视频，然后顺手做了这道题目

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        if(right == left) {
            if(nums[left] == target){
                return left;
            }
        }
        else {
            while(left <= right) {
                int mid = (left + right) / 2;
                if(nums[mid] < target) {
                    left = mid + 1;
                }
                else if(nums[mid] > target) {
                    right = mid - 1;
                }
                else {
                    return mid;
                }
            }
        }
        return -1;
    }
};
```

#### 3.5 搜索插入位置
时间过去太久，我忘记了非常多的二分查找的细节，所以我选取了[35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)来重新学习二分查找

刚开始做，我犯了很多错误，比如：
```c++
while (left < right) {  // 什么类型的区间?
    middle = (left + right) >> 1;
    if (nums[left] < target) {  // 这里应该是nums[middle] < target
        left = middle;  // 要不要+1?
    } else {
        right = middle; // 要不要-1?
    }
}
```

我确实记得要区分**左闭右闭**和**左闭右开**区间的做法，但是具体的实现还是忘了

我没有着急去看文章讲解，打算先自己摸索一遍

##### `target`小于`nums`最小值或者大于最大值的情况
我很快就想到了`target < nums[0]`和`target > nums.back()`的情形，不知道二分查找能不能解决这两个问题，所以干脆拎出来讨论
```c++
if (target < nums[0]) {
        return 0;
}
if (target > nums.back()) {
    return nums.size();
}
```

##### 二分查找
解决完两个边界问题，接下来只要讨论二分查找的问题即可

最开始的二分查找的主体如下
```c++
int left = 0;
int right = nums.size();
int middle = 0;
while(left < right) {
    middle = (left + right) >> 1;
    if (nums[middle] < target) {
        left = middle;
    } else {
        right = middle;
    }
}
```

###### 左闭右开区间
循环不变式是`left < right`，`right`取到`nums.size()`，比`nums`中最大索引值还大1，我觉得这个是左闭右开区间

但是我没有想到，如果`target > nums[middle]`，也就说明`nums[middle]`不等于`target`，那么`nums[middle]`肯定就不是希望能够查找到的值，所以`left`应该变为`middle + 1`才对

所以会出现下面的情况
```
nums = [1, 3, 4, 5]
target = 2
------------------------------------------
left = 0, right = 4
middle = 2 --- nums[middle] = 4 > target
update(right)

left = 0, right = 2
middle = 1 --- nums[middle] = 3 > target
update(right)

left = 0, right = 1
middle = 0 --- nums[middle] = 1 < target
update(left)

left = 0, right = 1
middle = 0 --- nums[middle] = 1 < target
update(left)
...
```

我没有对这种二分查找的主体进行一般性讨论，只是通过一两个例子观察发现，最后面陷入无穷循环的时候，`left`就是`target`所在的位置，或者是`target`待插入的位置的左边一个位置（即待插入位置-1）

于是，我把循环不变式改为`left < right - 1`，当`left`和`right`恰好相邻时，就说明已经找到插入位置了

我又想到当`nums`只有两个元素时，可能不一定适用，不过还好实际上是适用的

于是，这一版本的最终代码为
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // check if target is out of range
        if (target < nums[0]) {
            return 0;
        }
        if (target > nums.back()) {
            return nums.size();
        }
        int left = 0;
        int right = nums.size();
        int middle = 0;
        while(left < right - 1) {
            middle = (left + right) >> 1;
            if (target > nums[middle]) {
                left = middle;
            } else {
                right = middle;
            }
        }
        // nums[left]不等于target，意味着target不在nums中
        if (nums[left] < target) { 
            return left + 1;
        }
        return left;
    }
};
```

###### 左闭右闭区间

直接上代码
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // check if target is out of range
        if (target < nums[0]) {
            return 0;
        }
        if (target > nums.back()) {
            return nums.size();
        }
        int left = 0;
        int right = nums.size() - 1;
        int middle = 0;
        while (left < right - 1) {
            middle = (left + right) >> 1;
            if (nums[middle] <= target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        if (nums[left] < target) {
            return left + 1;
        }
        return left;
    }
};
```

和左闭右开区间相比，不同点在于
```c++
int right = nums.size() - 1;
```

我当时以为左闭右开区间和左闭右闭区间就是像上面这样做的，但是去看文章讲解的时候，发现我还是忽略了很多细节

##### 文章讲解答案
###### 左开右闭区间
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0;
        int right = n; // 定义target在左闭右开的区间里，[left, right)  target
        while (left < right) { // 因为left == right的时候，在[left, right)是无效的空间
            int middle = left + ((right - left) >> 1);
            if (nums[middle] > target) {
                right = middle; // target 在左区间，在[left, middle)中
            } else if (nums[middle] < target) {
                left = middle + 1; // target 在右区间，在 [middle+1, right)中
            } else { // nums[middle] == target
                return middle; // 数组中找到目标值的情况，直接返回下标
            }
        }
        // 分别处理如下四种情况
        // 目标值在数组所有元素之前 [0,0)
        // 目标值等于数组中某一个元素 return middle
        // 目标值插入数组中的位置 [left, right) ，return right 即可
        // 目标值在数组所有元素之后的情况 [left, right)，因为是右开区间，所以 return right
        return right;
    }
};
```


###### 左闭右开区间
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0;
        int right = n - 1; // 定义target在左闭右闭的区间里，[left, right]
        while (left <= right) { // 当left==right，区间[left, right]依然有效
            int middle = left + ((right - left) / 2);// 防止溢出 等同于(left + right)/2
            if (nums[middle] > target) {
                right = middle - 1; // target 在左区间，所以[left, middle - 1]
            } else if (nums[middle] < target) {
                left = middle + 1; // target 在右区间，所以[middle + 1, right]
            } else { // nums[middle] == target
                return middle;
            }
        }
        // 分别处理如下四种情况
        // 目标值在数组所有元素之前  [0, -1]
        // 目标值等于数组中某一个元素  return middle;
        // 目标值插入数组中的位置 [left, right]，return  right + 1
        // 目标值在数组所有元素之后的情况 [left, right]， 因为是右闭区间，所以 return right + 1
        return right + 1;
    }
};
```

最早学二分查找的时候我对循环不变式以及`left, right`的更新只是一知半解

尤其是左闭右闭区间的做法，当`left == right`，`mid`刚好等于`left`和`right`时，我会觉得这个时候已经找到了目标位置，不懂为什么还要更新一遍

我用简单的例子模拟了一下过程，发现其实很好理解

到了`left == right == middle`这一步的时候，已经相当于找到了目标位置，目标位置正好是`middle`或者`left`或者`right`

`target`在`nums`中的情形很好理解，比较难理解的是`target`不在`nums`中的情形

如果`target`不在`nums`中，肯定有`target < nums[middle]`，所以会执行`right = middle - 1`，此时`right`在`left`左边，结束循环

由于`left`是目标位置，`left == right + 1`，这里最后的`return right + 1`也可以写成`return left`，不过为了形式和左闭右开区间做法的一致，这里用`right`来写

而两种做法的最终`return`都可以是`return left`

##### 我的答案对比文章答案
###### 循环不变式比较
我的答案里面循环不变式是
```c++
left < right - 1
```

文章答案里的循环不变式分别是
```c++
// 左闭右开区间
left < right

// 左闭右闭区间
left <= right
```

文章答案里的循环不变式更方便记忆和符合数学逻辑，因为我们都知道左闭右开区间的右边的括号的值是取不到的，而左闭右闭区间两边括号的值是可以取到的

###### `left, right`更新比较
我的
```c++
if (target > nums[middle]) {
    left = middle;
} else {
    right = middle;
}
```

文章讲解的
```c++
// 左闭右开区间
if (nums[middle] > target) {
    right = middle; 
} else if (nums[middle] < target) {
    left = middle + 1; 
} else { 
    return middle; 
}

// 左闭右闭区间
if (nums[middle] > target) {
    right = middle - 1; 
} else if (nums[middle] < target) {
    left = middle + 1; 
} else {
    return middle;
}
```
我的答案中的更新其实并没有对区间的开闭进行区分，而文章答案中的答案作了很明显的区分
+ 左闭右开区间
  + 如果`nums[middle] > target`，那么`right = middle`，因为“右开”，`right`取值为`middle`，而不用-1
  + 如果`nums[middle] < target`，那么`left = middle + 1`，因为`nums[middle] != target`所以取`middle`右边的值
  + 循环结束时，`left == right`，`return left`和`return left`都行
+ 左闭右闭区间
  + 根据闭区间性质，`left`和`right`的更新很好理解
  + 循环结束前一步（`target`不在`nums`中），`left == right`，此时`left`即为目标位置
  + 循环结束时，`left == right + 1`