# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        second = self.reverse(second)

        first = head

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2


    def reverse(self,head):
        prev = None

        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev