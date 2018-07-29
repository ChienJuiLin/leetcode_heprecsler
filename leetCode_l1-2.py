'''
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

else Output: -1

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
 '''

 # 我以兩個list做存取，也要考慮過用mod欺負她的值介於0~99來回傳位置
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1=[0,0]
        n2=[0,0]

        for i in range(len(nums)):
            if nums[i] > n1[0]:
                n2[0] = n1[0]
                n1[0] = nums[i]
                n1[1] = i
            elif n1[0] > nums[i] > n2[0]:
                n2[0] = nums[i]
                n2[1] = i

        if n1[0] >= n2[0] * 2:
            return n1[1]

        return -1

# 結果看其他人的解法，直接用num.index()找，阿倫出來評評理啊        
'''
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        elif len(nums)>=2:
            max_nums = max(nums)
            max_index = nums.index(max_nums)
            nums.remove(max_nums)
            sec_nums = max(nums)
            if max_nums>=2*sec_nums:
                return max_index
            else:
                return -1
'''
