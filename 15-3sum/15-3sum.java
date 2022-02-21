class Solution {
	public List<List<Integer>> threeSum(int[] nums) {

		Arrays.sort(nums);

		List<List<Integer>> result = new ArrayList<>();

		for (int i = 0; i < nums.length - 2; i++) {

			if (i == 0 || nums[i] != nums[i - 1]) {

				int target = 0 - nums[i];

				int left = i + 1;
				int right = nums.length - 1;

				while (left < right) {

					int sum = nums[left] + nums[right];

					if (sum == target) {

						List<Integer> triplet = new ArrayList<>();
						triplet.add(nums[i]);
						triplet.add(nums[left]);
						triplet.add(nums[right]);

						result.add(triplet);

						while (left < right && nums[left] == nums[left + 1])
							left++;
						while (left < right && nums[right] == nums[right - 1])
							right--;

						right--;
						left++;
					}

					else if (sum > target) {
						right--;
					}

					else {
						left++;
					}

				}

			}

		}

		return result;

	}
}