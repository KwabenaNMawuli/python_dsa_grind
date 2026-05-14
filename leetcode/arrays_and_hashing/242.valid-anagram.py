#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram_dict = {}
        for i, letter in enumerate(s):
            anagram_dict[letter] = anagram_dict.get(letter, 0) + 1
        for i, letter in enumerate(t):
            if letter not in anagram_dict:
                return False
            anagram_dict[letter] -= 1
            if anagram_dict[letter] == 0:
                del anagram_dict[letter]
        return len(anagram_dict) == 0
# @lc code=end

