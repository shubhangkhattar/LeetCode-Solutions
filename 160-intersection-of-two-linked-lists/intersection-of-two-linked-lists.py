# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        dummy1 = headA
        dummy2 = headB

        while dummy1 != dummy2:
            if dummy1 is None:
                dummy1 = headB
            else:
                dummy1 = dummy1.next

            if dummy2 is None:
                dummy2 = headA
            else:
                dummy2 = dummy2.next

        return dummy1