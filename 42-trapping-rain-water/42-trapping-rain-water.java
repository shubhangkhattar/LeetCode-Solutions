class Solution {
	public int trap(int[] height) {

		int suffix[] = new int[height.length];
		int prefix[] = new int[height.length];
		int suffix_max = 0;
		int prefix_max = 0;
		int volume = 0;

		for (int i = 0; i < height.length; i++) {

			suffix[i] = Math.max(suffix_max, height[i]);
			suffix_max = suffix[i];

			prefix[height.length - 1 - i] = Math.max(prefix_max, height[height.length - 1 - i]);
			prefix_max = prefix[height.length - 1 - i];

		}

		for (int i = 0; i < height.length; i++) {

			volume += Math.min(suffix[i], prefix[i]) - height[i];

		}

		return volume;
	}

}
