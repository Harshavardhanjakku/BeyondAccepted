# Problem: First Element with Unique Frequency
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 1

int firstUniqueFreq(int* nums, int numsSize) {
    int maxVal = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal)
            maxVal = nums[i];
    }

    int *freq = calloc(maxVal + 1, sizeof(int));
    int *cnt  = calloc(numsSize + 1, sizeof(int));

    for (int i = 0; i < numsSize; i++)
        freq[nums[i]]++;

    for (int i = 0; i <= maxVal; i++)
        if (freq[i])
            cnt[freq[i]]++;

    for (int i = 0; i < numsSize; i++) {
        if (cnt[freq[nums[i]]] == 1) {
            free(freq);
            free(cnt);
            return nums[i];
        }
    }

    free(freq);
    free(cnt);
    return -1;
}
