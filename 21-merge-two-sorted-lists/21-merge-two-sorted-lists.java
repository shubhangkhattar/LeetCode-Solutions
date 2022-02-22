class Solution {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

		if (l1 == null || l2 == null)
			return l1 == null ? l2 : l1;

		ListNode newHead;
		ListNode prev;

		ListNode c1 = l1;
		ListNode c2 = l2;
		
		

		newHead = c1.val < c2.val ? c1 : c2;

		prev = new ListNode();

		
		while (c1 != null && c2 != null) {

			if (c1.val < c2.val) {
				prev.next = c1;
				prev = c1;
				c1 = c1.next;

			} else {

				prev.next = c2;
				prev = c2;
				c2 = c2.next;

			}

		}

		if(c1 == null) {
			prev.next = c2;
		} else {
			prev.next = c1;
		}

		return newHead;

	}
}