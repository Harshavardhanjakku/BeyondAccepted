# Problem: Four Divisors
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def sumFourDivisors(self, nums):
        def checkdiv(num):
            tot = 0
            cnt = 0
            
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    j = num // i
                    if i == j:          
                        cnt += 1
                        tot += i
                    else:
                        cnt += 2
                        tot += i + j
                if cnt > 4:
                    return 0
            return tot if cnt == 4 else 0

        ans = 0
        for num in nums:
            ans += checkdiv(num)
        return ans

