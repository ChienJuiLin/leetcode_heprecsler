'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
'''



class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if matrix == []: return []

        t = len(matrix) * len(matrix[0])

        rlen = len(matrix)
        clen = len(matrix[0])

        r,c = 0,0

        move = 1

        ans = list()

        for i in range(t):

            ans.append(matrix[r][c])

            next_r = r - move
            next_c = c + move

            if rlen-1 < next_r or next_r < 0 or clen-1 < next_c or next_c < 0:
                if move > 0:
                    next_r = r
                    next_c = c + 1

                    if rlen-1 < next_r or next_r < 0 or clen-1 < next_c or next_c < 0:
                        next_r = r + 1
                        next_c = c

                    move = move * (-1)

                else:
                    next_r = r + 1
                    next_c = c

                    if rlen-1 < next_r or next_r < 0 or clen-1 < next_c or next_c < 0:
                        next_r = r
                        next_c = c + 1

                    move = move * (-1)

            r = next_r
            c = next_c

        return ans
