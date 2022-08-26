class Solution {
	public int romanToInt(String s) {

		HashMap<Character, Integer> myMap = new HashMap<>();

		myMap.put('I', 1);
		myMap.put('V', 5);
		myMap.put('X', 10);
		myMap.put('L', 50);
		myMap.put('C', 100);
		myMap.put('D', 500);
		myMap.put('M', 1000);

		int result = 0;

		for (int i = 0; i < s.length(); i++) {

			if (i + 1 < s.length() && myMap.get(s.charAt(i)) < myMap.get(s.charAt(i+1))) {
				result -= myMap.get(s.charAt(i));
			} else {
				result += myMap.get(s.charAt(i));
			}

		}

		return result;

	}
}