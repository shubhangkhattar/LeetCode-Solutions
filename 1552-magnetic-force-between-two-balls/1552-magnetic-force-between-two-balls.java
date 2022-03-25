class Solution {

	boolean isPossible(int a[], int n, int cows, int minDist) {
		int cntCows = 1;
		int lastPlacedCow = a[0];
		for (int i = 1; i < n; i++) {
			if (a[i] - lastPlacedCow >= minDist) {
				cntCows++;
				lastPlacedCow = a[i];
			}
		}
		if (cntCows >= cows)
			return true;
		return false;
	}

	int maxDistance(int position[], int m) {

		Arrays.sort(position);

		int low = 1; 
		int high = position[position.length-1] - position[0];

		while (low <= high) {
			int mid = (low + high) >> 1;

			if (isPossible(position, position.length, m, mid)) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}

		return high;

	}

}