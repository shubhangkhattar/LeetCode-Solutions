class Solution {
	public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        if(n == 0){
            return;
        }

		int i = 0;
		int j = 0;

		while (i < m) {

			if (nums1[i] > nums2[j]) {
				
				swap(i,j,nums1,nums2);
				
				while( j+1 < nums2.length && nums2[j+1] < nums2[j]) {
					swap(j,j+1,nums2,nums2);
					j++;
					
				}
				
				j = 0;
					

			}

			i++;

		}
		

		while(j<n) {
			
			nums1[i] = nums2[j];
			j++;
			i++;
		}
		


	}
	

	public void swap(int i, int j, int[] arr1, int[] arr2) {

		int temp = arr1[i];
		arr1[i] = arr2[j];
		arr2[j] = temp;

	}
}