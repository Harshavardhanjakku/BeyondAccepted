# Problem: Number of 1 Bits
# Difficulty: Easy
# Topic: Divide and Conquer
# Language: c
# Submission: 1

int hammingWeight(int n) {
    int c=0;
    while (n){
        n=n&(n-1);
        c+=1;
    }
    return c;
}
