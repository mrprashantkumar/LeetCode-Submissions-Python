# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalPoints = []
        prev = head
        curr = head.next
        ind = 1
        while curr and curr.next:
            if prev.val < curr.val > curr.next.val:
                criticalPoints.append(ind)
            elif prev.val > curr.val < curr.next.val:
                criticalPoints.append(ind)
            prev = curr
            curr = curr.next
            ind += 1
        
        mini, maxi = inf, -inf
        n = len(criticalPoints)
        if n < 2:
            return [-1, -1]
        for i in range(n-1):
            mini = min(mini, criticalPoints[i+1] - criticalPoints[i])
        
        return [mini, criticalPoints[n-1]-criticalPoints[0]]