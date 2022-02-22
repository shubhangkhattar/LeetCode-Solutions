class Solution {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

		ListNode dummy = new ListNode();
        
        if(l1 == null){
            return l2;
        }
        
          if(l2 == null){
            return l1;
        }
        
        

		ListNode c1 = l1;
		ListNode c2 = l2;

		if (c1.val < c2.val) {
			dummy.val = c1.val;
			c1 = c1.next;
		} else {
			dummy.val = c2.val;
			c2 = c2.next;
		}

		ListNode newHead = dummy;

		while (c1 != null && c2 != null) {

			dummy.next = new ListNode();
			dummy = dummy.next;

			if (c1.val < c2.val) {
				dummy.val = c1.val;
				c1 = c1.next;
			} else {
				dummy.val = c2.val;
				c2 = c2.next;
			}

		}

		while (c1 != null) {

			dummy.next = new ListNode();
			dummy = dummy.next;

			dummy.val = c1.val;
			c1 = c1.next;

		}
		
		while (c2 != null) {

			dummy.next = new ListNode();
			dummy = dummy.next;

			dummy.val = c2.val;
			c2 = c2.next;

		}

		return newHead;

	}
}