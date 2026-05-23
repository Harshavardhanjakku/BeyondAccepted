# Problem: Search a 2D Matrix II
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int m = matrixSize;
    int n = matrixColSize[0]; 

    int i = 0;
    int j = n - 1;

    while (i < m && j >= 0) {
        if (matrix[i][j] == target) {
            return true;
        } else if (matrix[i][j] < target) {
            i++; 
        } else {
            j--;  
        }
    }

    return false;
}

