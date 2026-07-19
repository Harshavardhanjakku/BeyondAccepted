# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 8

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int maxIceCream(int* costs, int costsSize, int coins) {
    qsort(costs, costsSize, sizeof(int), cmp);

    int count = 0;

    for (int i = 0; i < costsSize; i++) {
        if (costs[i] > coins) {
            return count;
        }
        coins -= costs[i];
        count++;
    }

    return count;
}
