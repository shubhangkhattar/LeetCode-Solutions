class Solution {
	public int lengthOfLongestSubstring(String s) {

		int pointer = 0;
		int anchor = 0;

		int max = 0;

		Set<Character> mySet = new HashSet<>();

		while (pointer < s.length()) {

			if (!mySet.contains(s.charAt(pointer))) {

				mySet.add(s.charAt(pointer));
				max = Math.max(mySet.size(), max);

				pointer++;
			}else {
				mySet.remove(s.charAt(anchor));
				anchor++;
			}

		}

		return max;

	}
}