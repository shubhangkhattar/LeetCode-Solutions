class StockSpanner {

	Stack<int[]> myStack;

	public StockSpanner() {
		myStack = new Stack<>();
	}

	public int next(int price) {

		int span = 1;

		while (!myStack.isEmpty() && myStack.peek()[0] <= price) {
			span += myStack.pop()[1];
		}

		myStack.push(new int[] { price, span });

		return span;
	}
}