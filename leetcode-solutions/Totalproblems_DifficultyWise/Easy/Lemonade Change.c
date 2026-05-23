# Lemonade Change
# Difficulty: Easy
# Language: c

bool lemonadeChange(int* bills, int billsSize) {
    int r5 = 0;
    int r10 = 0;

    for (int i = 0; i < billsSize; i++) {
        if (bills[i] == 5) {
            r5++;
        } 
        else if (bills[i] == 10) {
            if (r5 == 0)
                return false;
            r5--;
            r10++;
        } 
        else { 
            if (r10 > 0 && r5 > 0) {
                r10--;
                r5--;
            } 
            else if (r5 >= 3) {
                r5 -= 3;
            } 
            else {
                return false;
            }
        }
    }
    return true;
}

