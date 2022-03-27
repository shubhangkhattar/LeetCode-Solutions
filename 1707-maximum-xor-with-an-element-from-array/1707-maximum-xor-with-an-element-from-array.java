class Node {

	Node links[] = new Node[2];

	public Node() {

	}

	boolean containsKey(int ind) {
		return links[ind] != null;
	}

	Node get(int ind) {
		return links[ind];
	}

	void put(int ind, Node node) {
		links[ind] = node;
	}
}

class Trie {

	private static Node root;

	Trie() {

		root = new Node();

	}

	public void insert(int num) {

		Node node = root;

		for (int i = 31; i >= 0; i--) {
			int bit = (num >> i) & 1;

			if (!node.containsKey(bit)) {

				node.put(bit, new Node());

			}

			node = node.get(bit);

		}

	}

	public int getMax(int num) {
		Node node = root;

		int maxNum = 0;

		for (int i = 31; i >= 0; i--) {

			int bit = (num >> i) & 1;

			if (node.containsKey(1 - bit)) {

				maxNum = maxNum | (1 << i);
				node = node.get(1 - bit);

			} else {
				node = node.get(bit);
			}

		}

		return maxNum;
	}

}

class Solution {
	public int[] maximizeXor(int[] nums, int[][] queries) {

		Arrays.sort(nums);
		ArrayList<ArrayList<Integer>> offlineList = new ArrayList<>();

		int m = queries.length;

		for (int i = 0; i < m; i++) {

			ArrayList<Integer> temp = new ArrayList<>();
			temp.add(queries[i][1]);
			temp.add(queries[i][0]);
			temp.add(i);

			offlineList.add(temp);

		}

		Collections.sort(offlineList, new Comparator<ArrayList<Integer>>() {

			@Override
			public int compare(ArrayList<Integer> a, ArrayList<Integer> b) {
				return a.get(0).compareTo(b.get(0));
			}
		});

		int ind = 0;

		int n = nums.length;

		Trie trie = new Trie();

		ArrayList<Integer> ans = new ArrayList<>(m);

		for (int i = 0; i < m; i++)
			ans.add(-1);

		for (int i = 0; i < m; i++) {
			while (ind < n && nums[ind] <= offlineList.get(i).get(0)) {
				trie.insert(nums[ind]);
				ind++;
			}

			int queryInd = offlineList.get(i).get(2);
			if (ind != 0)
				ans.set(queryInd, trie.getMax(offlineList.get(i).get(1)));
			else
				ans.set(queryInd, -1);

		}

		return ans.stream().mapToInt(Integer::intValue).toArray();

	}
}