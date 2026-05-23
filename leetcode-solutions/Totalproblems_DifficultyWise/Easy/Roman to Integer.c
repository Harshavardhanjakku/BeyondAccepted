# Roman to Integer
# Difficulty: Easy
# Language: c

int romanToInt(char* s) {
    int val[256] = {0};
    val['I'] = 1;
    val['V'] = 5;
    val['X'] = 10;
    val['L'] = 50;
    val['C'] = 100;
    val['D'] = 500;
    val['M'] = 1000;

    int total = 0;

    for (int i = 0; s[i + 1] != '\0'; i++) {
        if (val[s[i]] < val[s[i + 1]])
            total -= val[s[i]];
        else
            total += val[s[i]];
    }

    return total + val[s[strlen(s) - 1]];
}

