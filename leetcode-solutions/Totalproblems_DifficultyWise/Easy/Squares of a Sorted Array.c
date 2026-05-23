# Squares of a Sorted Array
# Difficulty: Easy
# Language: c

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc(numsSize * sizeof(int));
    int left = 0, right = numsSize - 1;
    int ind = numsSize - 1;

    while (left <= right) {
        int leftSquare = nums[left] * nums[left];
        int rightSquare = nums[right] * nums[right];
        
        if (leftSquare > rightSquare) {
            result[ind] = leftSquare;
            left++;
        } else {
            result[ind] = rightSquare;
            right--;
        }
        ind--;
    }

    *returnSize = numsSize;
    return result;
}

