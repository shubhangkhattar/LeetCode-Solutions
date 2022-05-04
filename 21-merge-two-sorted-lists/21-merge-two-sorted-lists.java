class Solution {
	public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		
		if(list1 == null || list2 == null) {
			return list1 == null ? list2 : list1;
		}

		ListNode newHead = null;

		newHead = list1.val < list2.val ? list1 : list2;

		ListNode prev = new ListNode();

		while (list1 != null && list2 != null) {

			if (list1.val < list2.val) {

				prev.next = list1;
				prev = list1;
				list1 = list1.next;

			} else {

				prev.next = list2;
				prev = list2;
				list2 = list2.next;

			}

		}

		if (list1 == null) {
			prev.next = list2;
		} else {

			prev.next = list1;
		}
		
		return newHead;

	}
}