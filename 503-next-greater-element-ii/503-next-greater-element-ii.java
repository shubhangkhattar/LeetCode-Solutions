class Solution {
	public int[] nextGreaterElements(int[] nums) {

		Stack<Integer> stack = new Stack<>();

		int n = nums.length;

		int[] result = new int[nums.length];

		for (int i = 2 * n - 1; i >= 0; i--) {

			while (!stack.isEmpty() && stack.peek() <= nums[i%n]) {
				stack.pop();
			}

			if (i < n) {

				if (stack.isEmpty()) {
					result[i] = -1;
				} else {
					result[i] = stack.peek();
				}

			}

			stack.push(nums[i % n]);

		}

		return result;

	}
}