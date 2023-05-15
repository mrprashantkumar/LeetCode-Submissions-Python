# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k-1):
            curr = curr.next
        first = curr

        second = head
        while curr.next:
            curr = curr.next
            second = second.next
        
        # print(first.val, second.val)
        first.val, second.val = second.val, first.val
        return head