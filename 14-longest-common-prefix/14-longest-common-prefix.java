class Solution {
	public String longestCommonPrefix(String[] strs) {

		String res = "";

		for (int i = 0; i < strs[0].length(); i++) {

			char temp_char = strs[0].charAt(i);

			for (int j = 1; j < strs.length; j++) {

				if (i < strs[j].length() && strs[j].charAt(i) == temp_char) {
					continue;
				} else {
					return res;
				}

			}

			res += temp_char;

		}

		return res;

	}
}