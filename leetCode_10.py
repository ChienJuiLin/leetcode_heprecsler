'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for x in range(len(s)):
            ans = ans + s[len(s)-x-1]
        return ans
