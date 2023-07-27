class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        left = len(matrix[0])-1
        down = 0

        while left >= 0 and down < len(matrix):
            print(matrix[down][left],down,left)
            if matrix[down][left] == target:
                return True
            
            if target < matrix[down][left]:
                left -= 1
            else:
                down += 1

        return False
