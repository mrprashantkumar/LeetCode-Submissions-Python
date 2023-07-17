# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        def addList(node1, node2):
            carry = 0
            dummy = ListNode(-1)
            ans = dummy

            while node1 or node2 or carry:
                csum = carry
                if node1:
                    csum += node1.val
                    node1 = node1.next
                if node2:
                    csum += node2.val
                    node2 = node2.next
                
                dummy.next = ListNode(csum%10)
                dummy = dummy.next

                carry = csum // 10
            
            return ans.next
        
        head1 = reverse(l1)
        head2 = reverse(l2)
        res = addList(head1, head2)
        return reverse(res)