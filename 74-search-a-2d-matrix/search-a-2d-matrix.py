class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix) #[[1,3,5,7],[10,11,16,20],[23,30,34,60]] in thsi matrix len of matrix is 3 adn column is len of element 0 in matrix whihc is 4
        col = len(matrix[0])
        left = 0
        right = (row * col )-1
        while left<=right:
            mid = (left+right)//2
            row_mid= mid//col # so floor division given answer without decision telling what is row 
            col_mid = mid%col # module givees the reminder telling which column is this
            if matrix[row_mid][col_mid]==target:
                return True
            elif matrix[row_mid][col_mid]<target:
                left = mid+1
            else:
                right = mid-1
        return False


        