public class Solution {
	public ListNode detectCycle(ListNode head) {

		Set<ListNode> mySet = new HashSet<>();

		while (head != null) {

			if (mySet.contains(head)) {
				return head;
			} else {
				mySet.add(head);
				head = head.next;
			}

		}

		return null;

	}
}