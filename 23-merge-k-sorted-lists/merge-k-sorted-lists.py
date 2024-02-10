# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        qu = []
        for i, node in enumerate(lists):
            if node:
                heappush(qu, (node.val, i, node))
        
        dummy = ListNode(-1)
        curr = dummy
        while qu:
            val, i, node = heappop(qu)
            curr.next = node
            curr = curr.next
            if curr.next:
                heappush(qu, (curr.next.val, i, curr.next))
        return dummy.next