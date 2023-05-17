# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next
        
        start = curr.next
        curr.next = None
        prev = None
        while start:
            nextt = start.next
            start.next = prev
            prev = start
            start = nextt
        
        ans = 0
        while head and prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next
        return ans