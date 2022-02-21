class Solution {
	public List<List<Integer>> threeSum(int[] nums) {

		Arrays.sort(nums);

		List<List<Integer>> myResult = new ArrayList<>();

		for (int i = 0; i < nums.length - 2; i++) {
			
			if(i!=0 && nums[i-1] == nums[i]) {
				continue;
			}
			

			int low = i + 1;

			int high = nums.length - 1;

			int target = 0 - (nums[i]);

			while (low < high) {

				if (nums[low] + nums[high] == target) {

					List<Integer> row = new ArrayList<>();

					row.add(nums[i]);
					row.add(nums[low]);
					row.add(nums[high]);

					myResult.add(row);

					while (low < high && nums[low] == nums[low + 1]) {
						low++;
					}
					low++;

					while (low < high && nums[high] == nums[high - 1]) {
						high--;
					}
					high--;

				} else if (nums[low] + nums[high] > target) {
					high--;
				} else {
					low++;
				}

			}

		}

		return myResult;

	}
}