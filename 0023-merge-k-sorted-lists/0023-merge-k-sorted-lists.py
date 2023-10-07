class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.merge2list(list1,list2))
            lists = mergedList
        return lists[0]

    def merge2list(self,list1, list2):

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        ans = head

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1 != None:
            head.next = list1

        if list2 != None:
            head.next = list2

        return ans