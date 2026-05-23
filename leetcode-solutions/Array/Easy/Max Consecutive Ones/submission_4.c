# Problem: Max Consecutive Ones
# Difficulty: Easy
# Topic: Array
# Language: c
# Submission: 4

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int l = 0;
    int r = 0;
    int maxi = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            l = r + 1;
        }
        if ((r - l + 1) > maxi) {
            maxi = r - l + 1;
        }
        r++;
    }
    return maxi;
}

