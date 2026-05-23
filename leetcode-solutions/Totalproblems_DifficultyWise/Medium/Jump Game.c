# Jump Game
# Difficulty: Medium
# Language: c

#include <stdbool.h>

bool canJump(int* nums, int numsSize) {
    if (numsSize == 1)
        return true;
    if (nums[0] == 0)
        return false;

    int curr = nums[0];
    for (int i = 1; i < numsSize; i++) {
        curr--; 

        if (curr < 0)
            return false;

        if (nums[i] > curr)
            curr = nums[i];

        if (i == numsSize - 1)
            return true;
    }

    return true;
}

