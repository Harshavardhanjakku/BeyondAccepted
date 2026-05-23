# Problem: Minimum Absolute Difference
# Difficulty: Easy
# Topic: Array
# Language: c
# Submission: 1

#include <stdlib.h>
#include <limits.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    qsort(arr, arrSize, sizeof(int), compare);
    int minDiff = INT_MAX;
    for (int i = 1; i < arrSize; i++) {
        int diff = arr[i] - arr[i - 1];
        if (diff < minDiff) {
            minDiff = diff;
        }
    }
    int** result = (int**)malloc((arrSize - 1) * sizeof(int*));
    *returnColumnSizes = (int*)malloc((arrSize - 1) * sizeof(int));
    int count = 0;

    for (int i = 1; i < arrSize; i++) {
        int diff = arr[i] - arr[i - 1];
        if (diff == minDiff) {
            result[count] = (int*)malloc(2 * sizeof(int));
            result[count][0] = arr[i - 1];
            result[count][1] = arr[i];
            (*returnColumnSizes)[count] = 2;
            count++;
        }
    }

    *returnSize = count;
    return result;
}

