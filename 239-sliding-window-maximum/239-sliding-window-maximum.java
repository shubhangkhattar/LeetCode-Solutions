class Solution {
	public int[] maxSlidingWindow(int[] nums, int k) {

		int n = nums.length;
		int[] result = new int[n - k + 1];

		Deque<Integer> deque = new ArrayDeque<>();

		int ri = 0;

		for (int i = 0; i < nums.length; i++) {

			if (!deque.isEmpty() && deque.peek() == i - k) {
				deque.poll();

			}

			while (!deque.isEmpty() && nums[deque.peekLast()] <= nums[i]) {
				deque.pollLast();
			}

			deque.offer(i);

			if (i >= k - 1) {
				result[ri++] = nums[deque.peek()];
			}

		}

		return result;

	}
}