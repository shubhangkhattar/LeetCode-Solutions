public class Solution {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

		ListNode dummy1 = headA;
		ListNode dummy2 = headB;

		while (dummy1 != null) {

			while (dummy2 != null) {
				if (dummy1 == dummy2) {
					return dummy1;
				}
				dummy2 = dummy2.next;
			}

			dummy2 = headB;
			dummy1 = dummy1.next;

		}
		
		return null;

	}
}