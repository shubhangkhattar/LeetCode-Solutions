class Solution {

	public List<String> wordBreak(String s, List<String> wordDict) {

		List<String> results = new ArrayList<>();

		if (s.length() == 0) {
			results.add("");
			return results;
		}

		for (String word : wordDict) {

			if (s.startsWith(word)) {

				String sub = s.substring(word.length());
				List<String> subStrings = wordBreak(sub, wordDict);

				for (String subString : subStrings) {
					String optionalSpace = subString.isEmpty() ? "" : " ";
					results.add(word + optionalSpace + subString);
				}

			}

		}

		return results;

	}
}
