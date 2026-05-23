# Number of 1 Bits
# Difficulty: Easy
# Language: c

int hammingWeight(int n) {
    int c=0;
    while (n){
        n=n&(n-1);
        c+=1;
    }
    return c;
}
