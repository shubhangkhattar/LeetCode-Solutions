public class Solution {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

		ListNode dummy1 = headA;
		ListNode dummy2 = headB;

		while (dummy1 != dummy2) {
			dummy1 = dummy1 == null ? headB : dummy1.next;
			dummy2 = dummy2 == null ? headA : dummy2.next;
		}
		
		return dummy1;

	}
}