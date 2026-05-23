# Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Language: c

#include <stdlib.h>

int binarySearch(int* nums, int numsSize, int target) {
    int low = 0, high = numsSize - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target)
            return mid;
        else if (target < nums[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int firstBinarySearch(int* nums, int numsSize, int target) {
    int low = 0, high = numsSize - 1, res = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            res = mid;
            high = mid - 1;
        } else if (target < nums[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return res;
}

int lastBinarySearch(int* nums, int numsSize, int target) {
    int low = 0, high = numsSize - 1, res = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            res = mid;
            low = mid + 1;
        } else if (target < nums[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return res;
}


int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(sizeof(int) * 2);
    
    if (binarySearch(nums, numsSize, target) == -1) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }

    result[0] = firstBinarySearch(nums, numsSize, target);
    result[1] = lastBinarySearch(nums, numsSize, target);
    return result;
}

