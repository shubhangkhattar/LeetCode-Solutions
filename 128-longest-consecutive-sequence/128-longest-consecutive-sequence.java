class Solution {
	public int longestConsecutive(int[] nums) {

		Set<Integer> mySet = new HashSet<>();

		for (int i = 0; i < nums.length; i++) {
			mySet.add(nums[i]);
		}

		int max = 0;

		for (int i = 0; i < nums.length; i++) {

			if (mySet.contains(nums[i] - 1)) {
				continue;
			}

			int count = 0;

			int num = nums[i];

			while (mySet.contains(num)) {
				count++;
				num = num + 1;
			}

			max = Math.max(count, max);

		}

		return max;

	}
}