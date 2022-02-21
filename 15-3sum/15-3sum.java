class Solution {
	public List<List<Integer>> threeSum(int[] nums) {

		Arrays.sort(nums);

		Set<List<Integer>> mySet = new HashSet<>();

		for (int i = 0; i < nums.length-2; i++) {
			


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

					mySet.add(triplet);

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

		List<List<Integer>> result = new ArrayList<>();

		for (List<Integer> triplet : mySet) {
			result.add(triplet);
		}

		return result;

	}
}