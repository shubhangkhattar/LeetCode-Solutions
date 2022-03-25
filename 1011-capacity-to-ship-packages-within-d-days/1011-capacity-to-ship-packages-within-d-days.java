class Solution {
	public int shipWithinDays(int[] weights, int days) {

		if (days > weights.length)
			return -1;

		int low = weights[0];
		int high = 0;

		for (int i : weights) {
			high += i;
			low = Math.min(i, low);
		}

		int result = -1;

		while (low <= high) {

			int mid = (low + high) >> 1;

			if (isPossible(weights, mid, days)) {
				result = mid;
				high = mid - 1;
			} else {
				low = mid + 1;
			}

		}

		return low;

	}

	private boolean isPossible(int[] weights, int weight, int days) {

		int count = 0;

		int sumAllocated = 0;

		for (int i = 0; i < weights.length; i++) {

			if (sumAllocated + weights[i] > weight) {

				count++;
				sumAllocated = weights[i];
				if (sumAllocated > weight) return false;

			} else {
				sumAllocated += weights[i];
			}

		}

		if (count < days)
			return true;

		return false;
	}

}