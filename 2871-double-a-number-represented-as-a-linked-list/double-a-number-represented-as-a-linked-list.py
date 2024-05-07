# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr):
            prev = None
            while curr:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            
            return prev
        
        node = reverse(head)
        dummy = ListNode(-1)
        ans = dummy
        carry = 0
        while carry or node:
            s = carry
            if node:
                s += node.val * 2
                node = node.next
            
            ans.next = ListNode(s%10)
            carry = s//10
            ans = ans.next
        
        return reverse(dummy.next)