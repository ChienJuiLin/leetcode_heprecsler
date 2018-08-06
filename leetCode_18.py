'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
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
                ans = ans + tempW + ' '
                tempW = ''
            else:
                w = True
                tempW = c + tempW

        if tempW != '':
            ans = ans + tempW
            return ans
        else:
            return ans[:len(ans)-1]
'''

        return ' '.join(s.split()[::-1])[::-1]
'''
