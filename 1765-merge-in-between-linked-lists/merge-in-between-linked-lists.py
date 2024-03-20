# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1, curr2 = list1, list2
        for _ in range(a-1):
            curr1 = curr1.next
        
        nextt = curr1.next
        while curr2:
            curr1.next = curr2
            curr2 = curr2.next
            curr1 = curr1.next
        
        for _ in range(b-a+1):
            nextt = nextt.next
        
        curr1.next = nextt
        return list1