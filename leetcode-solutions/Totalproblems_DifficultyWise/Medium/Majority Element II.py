# Majority Element II
# Difficulty: Medium
# Language: python3

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums 
        candidate1 = candidate2 = None
        c1 = c2 = 0

        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
            elif c1 == 0:
                candidate1 = num
                c1 = 1
            elif c2 == 0:
                candidate2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1 
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result

