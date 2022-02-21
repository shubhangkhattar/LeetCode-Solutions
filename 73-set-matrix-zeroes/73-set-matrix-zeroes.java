class Solution {
	public void setZeroes(int[][] matrix) {

		boolean[] column = new boolean[matrix[0].length];
		boolean[] row = new boolean[matrix.length];

		int r = matrix.length;
		int c = matrix[0].length;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {

				if (matrix[i][j] == 0) {
					column[j] = true;
					row[i] = true;

				}

			}

		}

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {

				if (column[j] == true || row[i] == true) {
					matrix[i][j] = 0;

				}

			}

		}

	}
}