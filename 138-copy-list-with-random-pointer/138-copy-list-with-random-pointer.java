class Solution {
	public Node copyRandomList(Node head) {

		Map<Node, Node> myMap = new HashMap<>();

		Node cur = head;

		while (cur != null) {
			myMap.put(cur, new Node(cur.val));
			cur = cur.next;
		}

		cur = head;

		while (cur != null) {

			Node temp = myMap.get(cur);
			Node next = myMap.get(cur.next);
			Node random = myMap.get(cur.random);
			temp.next = next;
			temp.random = random;
			cur = cur.next;

		}

		return myMap.get(head);

	}
}