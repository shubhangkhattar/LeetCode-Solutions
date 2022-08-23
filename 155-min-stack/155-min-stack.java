class MinStack {

	Stack<Integer[]> minStack;

	public MinStack() {
		minStack = new Stack<>();
	}

	public void push(int val) {

		Integer[] element = new Integer[2];

		element[0] = val;

		if (!minStack.isEmpty() && minStack.peek()[1] < val) {
			element[1] = minStack.peek()[1];
		} else {
			element[1] = val;
		}

		minStack.push(element);

	}

	public void pop() {

		minStack.pop();

	}

	public int top() {

		return minStack.peek()[0];

	}

	public int getMin() {

		return minStack.peek()[1];

	}
}
