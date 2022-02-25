class Solution {
    public int[] twoSum(int[] nums, int target) {
        
	
	int a_pointer = 0;
	int b_pointer = nums.length-1;
	
	while(a_pointer<=b_pointer) {
		
		int sum = nums[a_pointer]+nums[b_pointer];
		
		
		if (sum < target) {
			a_pointer += 1;
			
		} else if (sum > target) {
			b_pointer -= 1;
			
		} else {
			
			return new int[] {a_pointer+1, b_pointer +1};
			
		}
	}
	
	
	return new int[] {a_pointer+1, b_pointer +1};
	
    }
}