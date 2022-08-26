class Solution {
	public int myAtoi(String s) {

		int ind = 0;

		while (ind < s.length() && s.charAt(ind) == ' ') {
			ind++;
		}

		if (ind == s.length())
			return 0;

		boolean isNegative = (s.charAt(ind) == '-');
		if (isNegative || s.charAt(ind) == '+')
			ind++;

		int result = 0;

		int maxLimit = Integer.MAX_VALUE / 10;

		while (ind < s.length() && s.charAt(ind) >= '0' && s.charAt(ind) <= '9') {

			int digit = s.charAt(ind) - '0';

			if (result > maxLimit || result == maxLimit && digit > 7)
                //https://youtu.be/z4YsWX0hT1A?t=460
			{
				return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
			}

			result = result * 10 + digit;

			ind++;

		}

		return isNegative ? -result : result;

	}
}