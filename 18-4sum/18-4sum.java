class Solution {
	public List<List<Integer>> fourSum(int[] nums, int target) {

		Arrays.sort(nums);

		List<List<Integer>> myResult = new ArrayList<List<Integer>>();

		if (nums == null || nums.length == 0)
			return myResult;

		int n = nums.length;

		for (int i = 0; i < n; i++) {

			int target_3 = target - nums[i];

			for (int j = i + 1; j < n; j++) {

				int target_2 = target_3 - nums[j];

				int low = j + 1;

				int high = n - 1;

				while (low < high) {

					int two_sum = nums[low] + nums[high];

					if (two_sum < target_2)
						low++;

					else if (two_sum > target_2)
						high--;

					else {

						List<Integer> row = new ArrayList<>();

						row.add(nums[i]);
						row.add(nums[j]);
						row.add(nums[low]);
						row.add(nums[high]);

						myResult.add(row);

						while (low < high && nums[low] == row.get(2))
							low++;

						while (low < high && nums[high] == row.get(3))
							high--;

					}

				}

				while (j + 1 < n && nums[j + 1] == nums[j])
					j++;

			}

			while (i + 1 < n && nums[i + 1] == nums[i])
				i++;

		}

		return myResult;

	}
}
