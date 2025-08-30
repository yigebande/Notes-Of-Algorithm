# 337. 打家劫舍III

我最开始的思路是用递归去做，要么选择当前节点，要么选择左右子节点，然后取较大值，但是提交的时候显示超时了。

我在CS106B中学过记忆化递归，但是这里我突然想不出来应该如何记忆化，看了文章讲解之后发现是用一个`unordered_map`来作为记忆容器。
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<TreeNode*, int> umap;
    int recursion(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return root->val;
        if (umap[root]) return umap[root];
        int haveRoot = root->val;
        if (root->left) 
            haveRoot += recursion(root->left->left) + recursion(root->left->right);
        if (root->right) 
            haveRoot += recursion(root->right->left) + recursion(root->right->right); 
        umap[root] = max(haveRoot, recursion(root->left) + recursion(root->right));
        return umap[root];
    }

    int rob(TreeNode* root) {
        return recursion(root);
    }
};
```
一开始我以为动态规划都必须是一个连续的数组才能做的，秉持着这样的思想，我一直都做不出这道题的动态规划做法。

看了文章讲解才知道这个是树状动态规划。

文章讲解中的树状动态规划才是真的巧妙，不看过真的想不出来。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        vector<int> res = robTree(root);
        return max(res[0], res[1]);
    }

    vector<int> robTree(TreeNode* root) {
        if (root == nullptr) return vector<int>{0, 0};
        vector<int> left = robTree(root->left);
        vector<int> right = robTree(root->right);
        // 偷root，则不偷左右子树
        int val1 = root->val + left[0] +right[0];
        // 不偷root，偷左右子树，取各自的较大值之和
        int val2 = max(left[0], left[1]) + max(right[0], right[1]);
        return {val2, val1};
    }
};
```