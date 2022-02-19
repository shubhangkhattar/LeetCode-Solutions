class Solution {
	public int[][] merge(int[][] intervals) {

		Arrays.sort(intervals, (a, b) -> Double.compare(a[0], b[0]));

		List<int[]> result = new ArrayList<>();

		int start = intervals[0][0];
		int end = intervals[0][1];

		for (int[] interval : intervals) {

			if (end >= interval[0]) {
				end = Math.max(end, interval[1]);
			} else {

				result.add(new int[] { start, end });
				start = interval[0];
				end = interval[1];

			}

		}

		result.add(new int[] { start, end });

		return result.toArray(new int[1][]);

	}
}