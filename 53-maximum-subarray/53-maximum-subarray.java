class Solution {
    public int maxSubArray(int[] nums) {
    	
    	int max = nums[0];
    	int currentmax = nums[0];
    	
    	for(int i=1 ; i < nums.length ;i++) {
    		currentmax = Math.max(currentmax+nums[i], nums[i]);
    		max = Math.max(currentmax, max);
    	}
    	
    	return max;
        
    }
}