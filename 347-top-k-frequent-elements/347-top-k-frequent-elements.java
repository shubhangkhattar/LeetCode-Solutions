class Solution {
	public int[] topKFrequent(int[] nums, int k) {

		Map<Integer, Integer> mySet = new HashMap<>();

		int[] result = new int[k];

		for (int num : nums) {
			int count = mySet.getOrDefault(num, 0)+1;
			mySet.put(num, count);

		}

		PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

		for(Map.Entry<Integer, Integer> entry : mySet.entrySet()) {
			pq.add(entry);
		}
		
		for (int i = 0; i < k; i++) {
			result[i] = pq.poll().getKey();
		}

		return result;
	}
}