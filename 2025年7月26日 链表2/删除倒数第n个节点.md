# 19. 删除链表的倒数第N个节点
还是一道很简单的题目

主要考查双指针

这里我用快慢指针`fast, slow`，并且在头节点前面加上一个虚拟头节点

考虑一般情况，链表如下所示，删除倒数第2个节点`n = 2`
```
ListNode* _dummyHead = new ListNode(-1, head);
head: [1, 2, 3, 4, 5]
```

1. 刚开始的`fast`和`slow`都指向虚拟头节点
![](images/initial.svg)

2. 那么，`fast`向右移动`n = 2`位
![](images/fastAhead.svg)

3. `fast`超前移动完毕后，`fast`和`slow`同步移动
![](images/mov1.svg)
![](images/mov2.svg)

4. 当`fast`刚好移动到最后一个节点，也就是`fast->next == nullptr`时，
   `slow->next`刚好是待删除的节点
![](images/mov3.svg)

这里引入虚拟头节点能够完美解决删除的节点是`head`的问题

由于题目已经说好n不会大于链表节点数量，所以这里没有考虑n大于链表节点数量的情况。
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) {
            delete head;
            return nullptr;
        }
        ListNode* _dummyHead = new ListNode(-1, head);
        ListNode* fast = _dummyHead;
        ListNode* slow = _dummyHead;;
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        ListNode* temp = slow->next;
        slow->next = temp->next;
        delete temp;
        return _dummyHead->next;
    }
};
```