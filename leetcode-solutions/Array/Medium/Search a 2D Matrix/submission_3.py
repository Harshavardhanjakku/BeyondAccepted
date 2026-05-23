# Problem: Search a 2D Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = self.find_row_by_last_element(matrix, target)
        if row == -1:
            return False
        return self.binary_search(matrix[row], target)

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def find_row_by_last_element(self, matrix, target):
        low, high = 0, len(matrix) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] >= target:
                result = mid  
                high = mid - 1
            else:
                low = mid + 1
        return result

