class Solution {
	public int majorityElement(int[] nums) {

		int count = 0;
		int element = nums[0];

		for (int num : nums) {

			if (count == 0) {
				element = num;
                count++;
			} else if (element == num) {
				count++;

			} else {
				count--;
			}

		}

		return element;

	}
}