class Solution {
	public boolean searchMatrix(int[][] matrix, int target) {

		for (int i = 0; i < matrix.length; i++) {

			if (i == matrix.length - 1 || matrix[i + 1][0] > target && target >= matrix[i][0]) {
				return binarySearch(matrix[i], target);
			}
		}

		return false;

	}

	boolean binarySearch(int[] row, int target) {

		for (int element : row) {

			if (element == target) {
				return true;
			}
		}

		return false;

	}
}