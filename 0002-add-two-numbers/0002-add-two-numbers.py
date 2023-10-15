# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0

        ans = ListNode()
        head = ans

        while l1 != None and l2 != None:
            new_val = l1.val + l2.val + carry
            carry = new_val//10
            new_val = new_val%10

            ans.next = ListNode(new_val)
            ans = ans.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None :
                new_val = l1.val + carry
                carry = new_val // 10
                new_val = new_val % 10
                ans.next = ListNode(new_val)
                ans = ans.next
                l1 = l1.next

        while l2 != None :
                new_val = l2.val + carry
                carry = new_val // 10
                new_val = new_val % 10
                ans.next = ListNode(new_val)
                ans = ans.next
                l2 = l2.next
            
        if carry != 0:
            ans.next = ListNode(carry)

        return head.next