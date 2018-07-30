class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        ans = [[1],[1,1]]

        for i in range(3,numRows+1):
            new_row = [1]
            for x in range(i-2):
                new_row.append(ans[i-2][x]+ans[i-2][x+1])
            new_row.append(1)
            ans.extend([new_row])

        return ans


# 這方法在操作陣列的手段很騷又迂迴
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows < 3:
            for i in range(1,numRows+1):
                res.append([1] * i)
        else:
            lastRow = self.generate(numRows - 1)
            lastRowPt = lastRow[-1]
            currRow = [1] + [0] * (numRows - 2) + [1]

            for i in range(len(lastRowPt)-1):
                currRow[i+1] = lastRowPt[i] + lastRowPt[i+1]

            res  = lastRow + [currRow]
        return res
'''
