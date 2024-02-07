# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        tmp = ans = ListNode(0)
        q = 0
        while l1 or l2 or q:
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + q
            q, tmp.next = v // 10, ListNode(v % 10)
            l1, l2, tmp = l1.next if l1 else None, l2.next if l2 else None, tmp.next
        return ans.next
