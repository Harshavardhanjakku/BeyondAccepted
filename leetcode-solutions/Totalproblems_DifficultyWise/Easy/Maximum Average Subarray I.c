# Maximum Average Subarray I
# Difficulty: Easy
# Language: c

double findMaxAverage(int* nums, int numsSize, int k) {
    int i;
    int sum = 0;
    
    for (i = 0; i < k; i++) {
        sum += nums[i];
    }
    
    int maxSum = sum;
    
    for (i = k; i < numsSize; i++) {
        sum = sum - nums[i - k] + nums[i];
        if (sum > maxSum) {
            maxSum = sum;
        }
    }
    
    return (double)maxSum / k;
}

