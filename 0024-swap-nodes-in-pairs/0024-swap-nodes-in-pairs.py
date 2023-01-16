# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        n = 0
        while head:
            arr.append(head.val)
            head = head.next
            n += 1
        
        i=0
        while i<n-1:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 2
        
        ans = None
        for i in arr[::-1]:
            ans = ListNode(i, ans)
        return ans