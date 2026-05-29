#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_nums = {}
        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1
        result = []
        for i in range(k):
            top = max(freq_nums, key=freq_nums.get)
            result.append(top)
            del freq_nums[top]

        return result
        
# @lc code=end

