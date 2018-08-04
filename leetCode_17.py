'''
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        w = False
        tempW = ''
        ans = ''

        for c in s:
            if c == ' ' and w == False:
                continue
            elif c == ' ' and w == True:
                w = False
                ans = ' ' + tempW + ans
                tempW = ''
            else:
                w = True
                tempW = tempW + c

        if tempW != '':
            ans = tempW + ans
            return ans
        else:
            return ans[1:]

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split(' ')
        s = map(lambda x: x.strip(), s)[::-1]
        a = ''
        for i in s:
            if i:
                a = a + ' ' + i
        return a.strip()
'''
