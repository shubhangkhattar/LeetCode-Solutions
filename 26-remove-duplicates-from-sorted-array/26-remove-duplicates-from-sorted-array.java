class Solution {
	public int removeDuplicates(int[] nums) {

		int i = 0;
		int j = 1;
		
		if(nums.length == 0) {
			return 0;
		}

		while (j < nums.length) {

			if (nums[i] == nums[j]) {
				j++;
				continue;
			}

			i++;

			nums[i] = nums[j];

		}
		
		return ++i;

	}
}