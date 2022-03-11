class Solution {
    public int mostFrequent(int[] nums, int key) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        int max = 0;
        int target = 0;
        for(int i=0; i<nums.length; i++) {
            if(i<nums.length-1 && nums[i] == key) {
                if(hm.getOrDefault(nums[i+1], 0)+1 > max){
                    max = hm.getOrDefault(nums[i+1], 0)+1;
                    target = nums[i+1];
                }
                hm.put(nums[i+1], hm.getOrDefault(nums[i+1], 0)+1);
            }
        }
        return target;
    }
}