class Solution {
	public boolean isPalindrome(ListNode head) {

		ListNode slow = head;
		ListNode fast = head;

		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}

		slow = reverseLinkedList(slow);

		fast = head;

		while (slow != null) {

			if (slow.val != fast.val) {
				return false;
			}

			slow = slow.next;
			fast = fast.next;

		}

		return true;

	}

	ListNode reverseLinkedList(ListNode head) {

		ListNode newHead = null;

		while (head != null) {

			ListNode next = head.next;
			head.next = newHead;
			newHead = head;
			head = next;

		}

		return newHead;

	}
}