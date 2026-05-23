# Problem: Max Consecutive Ones III
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

int longestOnes(int* nums, int numsSize, int k) {
    int n = numsSize;
    int zc = 0;
    int l = 0;
    int maxlen = 0;
    for (int r = 0; r < n; r++) {
        if (nums[r] == 0) {
            zc += 1;
        }
        if (zc > k) {
            if (nums[l] == 0) {
                zc -= 1;
            }
            l += 1;
        }
        if (zc <= k) {
            int currentLen = r - l + 1;
            if (currentLen > maxlen) {
                maxlen = currentLen;
            }
        }
    }
    return maxlen;
}

