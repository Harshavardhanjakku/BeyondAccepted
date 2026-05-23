# Problem: Four Divisors
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 1

#include <math.h>

int sumFourDivisors(int* nums, int numsSize) {
    int ans = 0;

    for (int idx = 0; idx < numsSize; idx++) {
        int num = nums[idx];
        int cnt = 0;
        int tot = 0;

        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                int j = num / i;
                if (i == j) {          
                    cnt += 1;
                    tot += i;
                } else {
                    cnt += 2;
                    tot += i + j;
                }
            }
            if (cnt > 4) {
                tot = 0;
                break;
            }
        }
        if (cnt == 4)
            ans += tot;
    }
    return ans;
}

