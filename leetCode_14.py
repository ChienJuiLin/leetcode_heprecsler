'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''
# 我不太懂最後這一行，為什麼既然已經用了O(n)的方法，還要找O(nlog n)的方法？


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        i,j,curSum=0,0,0
        curLen,ansLen=0,len(nums)
        success = False

        for x in nums:
            curSum = curSum + x
            while curSum>=s:
                success = True
                curLen = j - i + 1
                if curLen =< ansLen:
                    ansLen = curLen
                curSum = curSum - nums[i]
                i += 1
            j += 1

        if success:
            return ansLen
        else:
            return 0
