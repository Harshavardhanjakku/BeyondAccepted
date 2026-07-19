# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 6

int maxIceCream(int* costs, int costsSize, int coins) {
    int freq[100001] = {0};

    for (int i = 0; i < costsSize; i++) {
        freq[costs[i]]++;
    }

    int count = 0;

    for (int cost = 1; cost <= 100000; cost++) {
        if (freq[cost] == 0) continue;

        int can_buy = coins / cost;
        if (can_buy > freq[cost]) {
            can_buy = freq[cost];
        }

        count += can_buy;
        coins -= can_buy * cost;

        if (coins < cost) break;
    }

    return count;
}
