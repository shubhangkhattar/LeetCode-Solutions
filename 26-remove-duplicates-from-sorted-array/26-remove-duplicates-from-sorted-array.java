class Solution {
	public int removeDuplicates(int[] nums) {

		Set<Integer> mySet = new HashSet<>();

		for (int i = 0; i < nums.length; i++) {
			mySet.add(nums[i]);
		}

		int num = nums[0];

		int count = 0;
		int i = 0;
		while(count <=nums.length) {
			
			if(mySet.contains(num)) {
				nums[i] = num;
				i++;
			}
			
			num = num+1;
			
			count++;
			
		}
		
		System.out.println(mySet.size());
        
		return mySet.size();
        

	}
}