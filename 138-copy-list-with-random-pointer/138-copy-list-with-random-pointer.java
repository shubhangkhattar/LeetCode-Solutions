class Solution {
	public Node copyRandomList(Node head) {

		Node iter = head;
		Node front = head;
		Node copy;

		while (iter != null) {
			front = iter.next;
			copy = new Node(iter.val);
			iter.next = copy;
			copy.next = front;
			iter = front;

		}

		iter = head;

		while (iter != null) {
			if (iter.random != null) {
				iter.next.random = iter.random.next;
			}

			iter = iter.next.next;
		}

		iter = head;
		Node pseudoHead = new Node(0);
		copy = pseudoHead;

		while (iter != null) {
			front = iter.next.next;
			copy.next = iter.next;
			iter.next = front;
			copy = copy.next;
			iter = iter.next;
		}

		return pseudoHead.next;

	}
}