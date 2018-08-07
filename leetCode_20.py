'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 0:
            i = 0
            for j in range(len(nums)):
                if nums[j] != 0 and j==i:
                    i += 1
                elif nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    i += 1
