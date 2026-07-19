# Problem: First Element with Unique Frequency
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

int firstUniqueFreq(int* nums, int numsSize) {
    int freq[100001] = {0};
    int freqCount[100001] = {0};

    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
    }

    for (int i = 0; i < 100001; i++) {
        if (freq[i] > 0) {
            freqCount[freq[i]]++;
        }
    }

    for (int i = 0; i < numsSize; i++) {
        if (freqCount[freq[nums[i]]] == 1) {
            return nums[i];
        }
    }

    return -1;
}
