# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Difficulty: Easy
# Topic: Array
# Language: c
# Submission: 1

int min(int a, int b) {
    if (a < b) return a;
    else return b;
}

int cmp(const void *a, const void *b) {
     return *(int*)a - *(int*)b;
}

int minimumDifference(int* nums, int numsSize, int k){
    if (k == 1) return 0;

    qsort(nums, numsSize, sizeof(int), cmp);

    int result = 1000000;
    for (int i = 0; i <= numsSize - k; i++) {
        result = min(nums[i + k - 1] - nums[i], result);
    }
    
    return result;
}
