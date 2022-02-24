class Solution {
	public int trap(int[] height) {

		int volume = 0;

		int n = height.length;

		int left = 0, right = n - 1;
		
		int maxLeft = 0 , rightMax = 0;
		
		while(left <= right) {
			
			if(height[left] <= height[right]) {
				if(height[left] >= maxLeft) 
					maxLeft = height[left];
				else
					volume += maxLeft - height[left];
				
				left++;
				
			} else {
				if(height[right] >= rightMax)
					rightMax = height[right];
				else 
					volume += rightMax - height[right];
				
				right--;
			}
			
		}
		
		return volume;
	}

}
