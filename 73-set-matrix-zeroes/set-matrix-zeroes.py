class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = [] # zero_rows = set() we can use set too as set doesnt allow duplicate so lets supoose if a single row has 4-5 zeros then lsit will store that all entires of rows and column correspondin to every zero but set will store it once adn thsu saves memory but if you use set here then you have to use zero_rows.add(r) there only add works not append
        zero_cols= []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    zero_rows.append(r)
                    zero_cols.append(c)
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c]=0
        