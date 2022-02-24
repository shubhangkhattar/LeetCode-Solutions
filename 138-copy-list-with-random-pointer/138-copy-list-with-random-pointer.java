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

			Node next = cur.next;
			Node random = cur.random;

			Node temp = myMap.get(cur);
			temp.next = myMap.get(next);
			temp.random = myMap.get(random);
			
			cur = cur.next;

		}

		return myMap.get(head);

	}
}