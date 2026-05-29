#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer_1 = 0
        pointer_2 = 0
        n = len(nums)
        if n == 1:
            return nums
        else:
            while pointer_2 < n:
                if nums[pointer_2] != 0:
                    nums[pointer_1], nums[pointer_2] = nums[pointer_2], nums[pointer_1]
                    pointer_1 += 1
                pointer_2 += 1
            return nums




# @lc code=end

