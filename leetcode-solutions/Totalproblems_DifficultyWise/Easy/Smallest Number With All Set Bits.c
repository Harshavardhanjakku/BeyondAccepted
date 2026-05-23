# Smallest Number With All Set Bits
# Difficulty: Easy
# Language: c

int smallestNumber(int n) {
    int c=0;
    while (n>0)
    {
        c+=1;
        n=n>>1;
    }
    return (1<<c)-1;
}
