# Problem: Search a 2D Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_index = self.find_row(matrix, target)
        if row_index == -1:
            return False
        return self.binary_search(matrix[row_index], target)

    def binary_search(self, row, target):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def find_row(self, matrix, target):
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid 
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1 

