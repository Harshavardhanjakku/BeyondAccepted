# Problem: Destroying Asteroids
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

#include <stdlib.h>
#include <stdbool.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    qsort(asteroids, asteroidsSize, sizeof(int), compare);

    long long currMass = mass;

    for (int i = 0; i < asteroidsSize; i++) {
        if (currMass < asteroids[i]) {
            return false;
        }
        currMass += asteroids[i];
    }

    return true;
}
