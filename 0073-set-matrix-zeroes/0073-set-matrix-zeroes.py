class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_0 = [1]*ROWS
        col_0 = [1]*COLS


        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_0[i] = 0
                    col_0[j] = 0 

        for i in range(ROWS):
            for j in range(COLS):
                if row_0[i] == 0 or col_0[j] == 0:
                    matrix[i][j] = 0
        
        