# Problem: Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for ch in str(num):
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

    def longest_prefix(self, num):
        node = self.root
        count = 0

        for ch in str(num):
            if ch in node.children:
                count += 1
                node = node.children[ch]
            else:
                break

        return count


class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):

        trie = Trie()

        for num in arr1:
            trie.insert(num)

        ans = 0

        for num in arr2:
            ans = max(ans, trie.longest_prefix(num))

        return ans
