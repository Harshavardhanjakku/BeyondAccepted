# Problem: Minimum Time to Type Word Using Special Typewriter
# Difficulty: Easy
# Topic: String
# Language: python3
# Submission: 1

class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        ans = 0
        for ch in word:
            diff = abs(ord(curr) - ord(ch))
            ans += min(diff, 26 - diff) + 1
            curr = ch
        return ans
