"""
1329. Sort the Matrix Diagonally
Dificulty: Medium

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left
to the bottom-right then return the sorted array.

Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
"""

from typing import List


class Solution:

    def top_diag(self, mat, diag):
        result = []
        for i in range(min(diag +1, len(mat))):
            result.append( mat[i][len(mat[0] ) -diag - 1 +i])
        return result

    def top_diag_assign(self, mat, a, diag):
        for i in range(min(diag +1, len(mat))):
            mat[i][len(mat[0] ) -diag - 1 +i] = a[i]

    def bottom_diag(self, mat, diag):
        result = []
        for i in range(diag, min(len(mat), len(mat[0]))):
            result.append(mat[i][ i-diag  ])
        return result

    def bottom_diag_assign(self, mat, a, diag):
        for i in range(diag, min(len(mat), len(mat[0]))):
            mat[i][ i-diag  ] = a[i-diag]

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat[0])):
            a = self.top_diag(mat, i)
            a.sort()
            self.top_diag_assign(mat, a, i)

        for i in range(1, len(mat)):
            a = self.bottom_diag(mat, i)
            a.sort()
            self.bottom_diag_assign(mat, a, i)
        return mat

if __name__ == "__main__":
    s = Solution()
    s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    s.diagonalSort([
        [58],[99],[1],[6],[73],[9],[60],[88],[64],[60],[39],[29],[46],[20],[78],[95],[2],[35],[20],[53],[60],[15],[94],[78],[26],[89],[87],[93],[70],[31],[94],[58],[90],[48],[60],[6],[68],[62],[32],[36],[73],[49],[45],[31],[23],[3],[73],[70],[71],[18],[14],[49],[84],[72],[59],[91],[17],[46],[93],[31],[31],[71],[52],[83],[8],[95],[49],[57],[52],[65],[83],[98],[46],[55],[44],[100],[45],[7],[59],[38],[82],[62],[25],[55],[64],[56],[89],[2],[10],[57],[26],[19],[27],[80],[12],[32],[62],[91],[68],[92]])
    s.diagonalSort([[1,2,3,4,5,1,2,3,4,5]])