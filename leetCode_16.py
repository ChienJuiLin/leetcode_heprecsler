'''

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]

        curIndex = 1
        ans = [1,1]

# 更新版有算進 O(k) extra space 嗎？
        while rowIndex > curIndex:
            i = len(ans) - 1
            ans.append(1)
            while 1 <= i:
                ans[i] = ans[i-1] + ans[i]
                i -= 1
            curIndex += 1

        return ans



'''
        while rowIndex > curIndex:
            i = 0
'''
# 傳指標和傳內容以後一定要注意
'''
            newRow = ans[:]
            while curIndex > i:
                i += 1
                newRow[i] = ans[i-1] + ans[i]
            newRow.append(1)
            ans = newRow
            curIndex += 1

        return ans
'''

'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        inplaceRow = []
        for row in range(rowIndex+1):
            inplaceRow.append(1)
'''
# 倒過來加就可以避免重複加到的問題
'''
            for i in reversed(range(1, len(inplaceRow)-1)):
                inplaceRow[i] = inplaceRow[i-1]+inplaceRow[i]
        return inplaceRow
'''
