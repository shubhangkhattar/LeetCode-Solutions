# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        current = head
        length = 0
        while current != None:
            current = current.next
            length += 1
            
        if length == n:
            head = head.next
            return head
        
        current = head
        count = 0
        while (current != None) and (n != length - count - 1):
            current = current.next
            count += 1
            
            
        current.next = current.next.next
        
        return head
