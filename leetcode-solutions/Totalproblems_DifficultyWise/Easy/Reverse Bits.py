# Reverse Bits
# Difficulty: Easy
# Language: python

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:].zfill(32)     # get binary without '0b', pad to 32 bits
        reversed_binary = binary[::-1]    # reverse the binary string
        return int(reversed_binary, 2)    # convert back to int

