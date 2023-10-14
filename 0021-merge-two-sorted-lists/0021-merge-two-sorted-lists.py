# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        currhead = None

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            currhead = list1
            list1 = list1.next
        else:
            currhead = list2
            list2 = list2.next

        head = currhead

        while list1 != None and list2 !=None:
            
            if list1.val < list2.val:
                currhead.next = list1
                list1 = list1.next
                
            else:
                currhead.next = list2
                list2 = list2.next

            currhead = currhead.next

        if list1 != None:
            currhead.next = list1
        
        if list2 != None:
            currhead.next = list2


        return head
