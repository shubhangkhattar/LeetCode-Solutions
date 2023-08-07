# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse_list(slow)

        start = head

        while slow is not None:
            if start.val != slow.val:
                return False
            slow = slow.next
            start = start.next

        return True

    def reverse_list(self, head):

        prev = None
        next = head.next

        while next != None:
            head.next = prev
            prev = head
            head = next
            next = head.next

        head.next = prev

        return head
