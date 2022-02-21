class Solution {
	public List<Integer> majorityElement(int[] nums) {

		int nums1 = -1;
		int nums2 = -1;

		int c1 = 0;
		int c2 = 0;

		for (int i = 0; i < nums.length; i++) {

			if (nums[i] == nums1) {
				c1++;
			} else if (nums[i] == nums2) {
				c2++;
			} else if (c1 == 0) {
				nums1 = nums[i];
				c1 = 1;
			} else if (c2 == 0) {
				nums2 = nums[i];
				c2 = 1;
			} else {
				c1--;
				c2--;
			}

		}

		int threshhold = nums.length / 3;

		c1 = 0;
		c2 = 0;

		List<Integer> temp = new ArrayList<>();

		for (int i = 0; i < nums.length; i++) {

			if (nums[i] == nums1) {
				c1++;
			} else if (nums[i] == nums2) {
				c2++;
			}
		}

		if (c1 > threshhold)
			temp.add(nums1);

		if (c2 > threshhold)
			temp.add(nums2);
		
		return temp;

	}
}