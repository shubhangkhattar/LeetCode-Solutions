class Solution {
	public ListNode rotateRight(ListNode head, int k) {

		if (head == null || head.next == null) {
			return head;

		}

		int length = 1;

		ListNode cur = head;

		while (cur.next != null) {
			length++;
			cur = cur.next;
		}

		cur.next = head;

		k = k % length;
		k = length - k;

		while (k-- > 0)
			cur = cur.next;

		head = cur.next;
		cur.next = null;

		return head;

	}
}
