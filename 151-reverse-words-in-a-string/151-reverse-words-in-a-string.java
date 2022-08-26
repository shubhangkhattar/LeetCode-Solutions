class Solution {
	public String reverseWords(String s) {

		s += " ";

		char[] elements = s.toCharArray();

		Stack<String> stack = new Stack<>();

		String temp = "";

		for (int i = 0; i < elements.length; i++) {

			if (elements[i] == ' ') {
				if(temp!= "") {
					stack.push(temp);
					temp = "";
				}
			
			} else {
				temp += elements[i];
			}

		}

		temp = "";

		while (stack.size() != 1) {
			temp += stack.pop() + " ";
		}

		temp += stack.pop();

		return temp;

	}
}