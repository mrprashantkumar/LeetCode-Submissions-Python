# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        seen = []
        curr = head
        ind = 0
        d = {}
        while curr:
            while seen and seen[-1][1] < curr.val:
                i, x = seen.pop()
                d[i] = curr.val
            seen.append([ind, curr.val])
            curr = curr.next
            ind += 1

        ans = [0]*ind
        for i in range(ind):
            ans[i] = d.get(i, 0)
        return ans