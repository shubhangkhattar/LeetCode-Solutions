class Solution {
	public int orangesRotting(int[][] grid) {

		if (grid.length == 0)
			return 0;

		int rows = grid.length;
		int cols = grid[0].length;

		Queue<int[]> queue = new LinkedList<>();

		int total_orranges = 0;

		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {

				if (grid[i][j] == 2) {
					queue.offer(new int[] { i, j });
				} 
				
				if(grid[i][j] != 0) {
					total_orranges++;
				}

			}
		}

		if (total_orranges == 0)
			return 0;

		int timer = 0, count_rottened = 0;

		int[] dx = new int[] { 0, 0, 1, -1 };
		int[] dy = new int[] { 1, -1, 0, 0 };

		while (!queue.isEmpty()) {

			int size = queue.size();
			
			count_rottened += size;

			for (int i = 0; i < size; i++) {
				
				int[] point = queue.poll();
				
				for (int j = 0; j < 4; j++) {

					int x = point[0] + dx[j];
					int y = point[1] + dy[j];

					if (x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] == 0 || grid[x][y] == 2)
						continue;

					grid[x][y] = 2;
					queue.offer(new int[] { x, y });

				}
			}

			if (queue.size() != 0) {
				timer++;
			}

		}

		return total_orranges == count_rottened ? timer : -1;

	}
}