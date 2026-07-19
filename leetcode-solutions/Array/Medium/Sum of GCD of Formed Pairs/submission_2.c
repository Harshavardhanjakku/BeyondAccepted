# Problem: Sum of GCD of Formed Pairs
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

long long gcdSum(int* nums, int numsSize) {
    int *prefix = (int *)malloc(numsSize * sizeof(int));

    int curr = nums[0];

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > curr)
            curr = nums[i];

        prefix[i] = curr;
    }

    for (int i = 0; i < numsSize; i++) {
        prefix[i] = gcd(prefix[i], nums[i]);
    }

    qsort(prefix, numsSize, sizeof(int), cmp);

    int left = 0;
    int right = numsSize - 1;
    long long tot = 0;

    while (left < right) {
        tot += gcd(prefix[left], prefix[right]);
        left++;
        right--;
    }

    free(prefix);
    return tot;
}
