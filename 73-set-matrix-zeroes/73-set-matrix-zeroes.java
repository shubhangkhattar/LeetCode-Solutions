class Solution {
	public void setZeroes(int[][] matrix) {

		boolean top = true;

		int r = matrix.length;
		int c = matrix[0].length;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {

				if (j == 0 && matrix[i][j] == 0) {
					top = false;
				} else if (matrix[i][j] == 0) {
					matrix[0][j] = 0;
					matrix[i][0] = 0;

				}

			}

		}

		for (int i = r-1; i >= 0; i--) {
			for (int j = c-1; j > 0; j--) {

				if (matrix[0][j] == 0 || matrix[i][0] == 0) {
					matrix[i][j] = 0;

				}

			}

		}

		if (!top) {

			for (int i = 0; i < r; i++) {
				matrix[i][0] = 0;

			}

		}

	}
}