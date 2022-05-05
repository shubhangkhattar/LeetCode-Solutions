class Solution {
	public int removeDuplicates(int[] nums) {

		int i = 0;
		int j = 1;

		if (nums.length <= 1) {
			return nums.length;
		}

		while (j < nums.length) {
			if (nums[j] == nums[i]) {
				j++;
				continue;
			}

			i++;

			nums[i] = nums[j];
		}

		return ++i;

	}
}