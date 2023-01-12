# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==1:
            return head
        
        nums = []
        n = 0
        while head:
            nums.append(head.val)
            head = head.next
            n += 1
        
        r = n//k
        for i in range(r):
            nums[i*k:(i+1)*k] = reversed(nums[i*k:(i+1)*k])
        
        ans = None
        for i in nums[::-1]:
            ans = ListNode(i, ans)
        return ans