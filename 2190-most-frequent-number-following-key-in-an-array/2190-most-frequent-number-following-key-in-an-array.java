class Solution {
	public int mostFrequent(int[] nums, int key) {

		int max = nums[0];

		int[] frequencyArray = new int[1001];

		for (int i = 1; i < nums.length; i++) {

			if (nums[i - 1] == key) {
				frequencyArray[nums[i]]++;

				max = frequencyArray[nums[i]] > frequencyArray[max] ? nums[i] : max;

			}

		}

		return max;

	}
}