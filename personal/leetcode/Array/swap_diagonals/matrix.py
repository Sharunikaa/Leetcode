class Solution:
    def swapDiagonal(self, mat):
        for i in range(len(mat)):
            mat[i][i],mat[i][n-1-i]=mat[i][n-1-i],mat[i][i]
        return mat
        
                  
