class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = sum(nums)
        l = t
        for i in range(len(nums)):

            l = l - nums[i]


            if l == (t-nums[i])/2:
                return i

        return -1
        
