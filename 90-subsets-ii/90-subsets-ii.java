class Solution {
	public List<List<Integer>> subsetsWithDup(int[] nums) {

		Arrays.sort(nums);
		List<List<Integer>> ansList = new ArrayList<>();
		findSubset(0, nums, new ArrayList<>(), ansList);
        
        return ansList;


	}

	private void findSubset(int ind, int[] nums, List<Integer> ds, List<List<Integer>> ansList) {

		ansList.add(new ArrayList<>(ds));

		for (int i = ind; i < nums.length; i++) {

			if (i != ind && nums[i] == nums[i - 1])
				continue;
			ds.add(nums[i]);
			findSubset(i + 1, nums, ds, ansList);
			ds.remove(ds.size() - 1);

		}
        

	}

}