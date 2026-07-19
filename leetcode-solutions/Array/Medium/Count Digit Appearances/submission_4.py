# Problem: Count Digit Appearances
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 4

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        tot=0
        for num in nums :
            while num :
                if num%10==digit:
                    tot+=1
                num//=10
        return tot
