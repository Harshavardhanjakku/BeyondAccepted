# Reverse Vowels of a String
# Difficulty: Easy
# Language: python

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        sl = list(s)

        while i < j:
            if not (sl[i] == 'a' or sl[i] == 'e' or sl[i] == 'i' or sl[i] == 'o' or sl[i] == 'u' or
                    sl[i] == 'A' or sl[i] == 'E' or sl[i] == 'I' or sl[i] == 'O' or sl[i] == 'U'):
                i += 1
            elif not (sl[j] == 'a' or sl[j] == 'e' or sl[j] == 'i' or sl[j] == 'o' or sl[j] == 'u' or
                      sl[j] == 'A' or sl[j] == 'E' or sl[j] == 'I' or sl[j] == 'O' or sl[j] == 'U'):
                j -= 1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1

        return "".join(sl)

