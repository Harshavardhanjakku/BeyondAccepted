# Search a 2D Matrix
# Difficulty: Medium
# Language: python

class Solution(object):
    def searchMatrix(self, matrix, target):
        def findrow(matrix, target):
            low = 0
            high = len(matrix) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[mid][-1] < target:
                    low = mid + 1
                elif matrix[mid][0] > target:
                    high = mid - 1
                else: 
                    return mid
            return -1
        
        def findcolumn(matrix, target, row):
            low = 0 
            high = len(matrix[0]) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        myrow = findrow(matrix, target)
        if myrow == -1:
            return False
        return findcolumn(matrix, target, myrow)

