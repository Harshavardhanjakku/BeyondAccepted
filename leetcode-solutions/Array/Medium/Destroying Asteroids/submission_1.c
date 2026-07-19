# Problem: Destroying Asteroids
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 1

bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    int freq[100001] = {0};

    for (int i = 0; i < asteroidsSize; i++) {
        freq[asteroids[i]]++;
    }

    long long curr = mass;

    for (int val = 1; val <= 100000; val++) {
        while (freq[val]--) {
            if (curr < val)
                return false;
            curr += val;
        }
    }

    return true;
}
