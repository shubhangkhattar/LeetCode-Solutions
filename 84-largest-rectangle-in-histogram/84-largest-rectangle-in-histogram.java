class Solution {
	public int largestRectangleArea(int[] heights) {

		int max = 0;

		int n = heights.length;

		int[] leftsmall = leftSmall(heights);
		int[] rightsmall = rightSmall(heights);
		
		for (int i = 0; i < n; i++) {
			int vol = (rightsmall[i] - leftsmall[i] + 1) * heights[i];
			max = Math.max(max, vol);
		}

		return max;

	}

	private int[] leftSmall(int[] heights) {

		int n = heights.length;

		int[] leftArr = new int[n];

		Stack<Integer> stack = new Stack<>();

		for (int i = 0; i < n; i++) {

			while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
				stack.pop();
			}

			if (stack.isEmpty()) {
				leftArr[i] = 0;

			} else {
				leftArr[i] = stack.peek() + 1;
			}

			stack.push(i);

		}

		return leftArr;

	}

	private int[] rightSmall(int[] heights) {

		int n = heights.length;

		int[] righttArr = new int[n];

		Stack<Integer> stack = new Stack<>();

		for (int i = n - 1; i >= 0; i--) {

			while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
				stack.pop();
			}

			if (stack.isEmpty()) {
				righttArr[i] = n - 1;

			} else {
				righttArr[i] = stack.peek() - 1;
			}

			stack.push(i);

		}

		return righttArr;

	}

}