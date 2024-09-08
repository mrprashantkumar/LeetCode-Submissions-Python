# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        ans = []

        m = count%k
        size = count//k

        curr = head
        for _ in range(m):
            ans.append(curr)
            prev = None
            for j in range(size+1):
                prev = curr
                curr = curr.next
            prev.next = None
        
        for _ in range(k-m):
            ans.append(curr)
            prev = None
            for j in range(size):
                prev = curr
                if curr.next:
                    curr = curr.next
                else:
                    break
            if prev: prev.next = None

        return ans