'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if matrix == []: return []

        t = len(matrix) * len(matrix[0])

        rlen = len(matrix)
        clen = len(matrix[0])

        r,c = 0,-1

        move = 1

        ans = list()

        rowStep = rlen - 1
        cur_rowStep = 0
        columnStep = clen
        cur_columnStep = 0

        state = 'right'

        for i in range(t):

            if state == 'right':
                c +=1
                ans.append(matrix[r][c])
                cur_columnStep += 1
                if cur_columnStep == columnStep:
                    state = 'down'
                    cur_columnStep = 0
                    columnStep -= 1
            elif state == 'down':
                r +=1
                ans.append(matrix[r][c])
                cur_rowStep += 1
                if cur_rowStep == rowStep:
                    state = 'left'
                    cur_rowStep = 0
                    rowStep -= 1
            elif state == 'left':
                c -=1
                ans.append(matrix[r][c])
                cur_columnStep += 1
                if cur_columnStep == columnStep:
                    state = 'up'
                    cur_columnStep = 0
                    columnStep -= 1
            elif state == 'up':
                r -=1
                ans.append(matrix[r][c])
                cur_rowStep += 1
                if cur_rowStep == rowStep:
                    state = 'right'
                    cur_rowStep = 0
                    rowStep -= 1
        return ans
