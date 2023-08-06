# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if ((head == None) or (head.next == None)): 
            return head

        prev = None
        next = head.next


        while next != None:
            head.next = prev
            prev = head
            head = next
            next = head.next

        head.next = prev

        return head
