# Problem: Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Topic: String
# Language: c
# Submission: 2

char* removeDuplicates(char* s) {
    int top = -1;

    for (int i = 0; s[i]; i++) {
        if (top >= 0 && s[top] == s[i]) {
            top--;
        } else {
            s[++top] = s[i];
        }
    }

    s[top + 1] = '\0';
    return s;
}
