'''

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a2 = int(a)
        b2 = int(b)

        ia,ib,p,ans = 0,0,1,0
        while a2 > 0:
            ia = ia+(a2%10)*2*p
            p = p*2
            a2 = a2//10
        p = 1
        while b2 > 0:
            ib = ib+(b2%10)*2*p
            p = p*2
            b2 = b2//10
        p = 1

        c = ia + ib
        while c > 0:
            ans = ans + (c%2)*p
            c = c//2
            p = p*10
        return str(ans)
# 這超賤
'''
return format(int(a,2) + int(b,2),'b')
'''
