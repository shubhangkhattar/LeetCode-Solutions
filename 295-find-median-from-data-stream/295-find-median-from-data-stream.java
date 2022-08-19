import java.util.Collections;
import java.util.PriorityQueue;

class MedianFinder {

	PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
	PriorityQueue<Integer> minHeap = new PriorityQueue<>();

	public void addNum(int num) {

		if (maxHeap.isEmpty() || maxHeap.peek() > num) {

			maxHeap.add(num);

		} else {
			minHeap.add(num);
		}

		if (maxHeap.size() > minHeap.size() + 1) {
			int element = maxHeap.poll();
			minHeap.add(element);
		} else if (minHeap.size() > maxHeap.size() + 1) {
			int element = minHeap.poll();
			maxHeap.add(element);
		}

	}

	public double findMedian() {

		double median = 0;
		if (maxHeap.size() == minHeap.size()) {
			double ele1 = (double) maxHeap.peek();
			double ele2 = (double) minHeap.peek();
			median = (ele1 + ele2) / 2;
		} else if (maxHeap.size() != minHeap.size()) {
			if (maxHeap.size() > minHeap.size()) {
				median = maxHeap.peek();
			} else if (maxHeap.size() < minHeap.size()) {
				median = minHeap.peek();
			}
		}

		return median;

	}
}