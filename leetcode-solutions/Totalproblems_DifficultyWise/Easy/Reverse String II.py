# Reverse String II
# Difficulty: Easy
# Language: python3

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        n = len(s)
        def RevFun(left, right):
            right = min(right, n - 1)
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        for i in range(0, n, 2*k):
            RevFun(i, i + k - 1)
        return "".join(l)

