class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        top  = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1

        while top<=bottom and left<=right:
            #movign along top formm left ot right
            for r in range(left,right+1):
                res.append(matrix[top][r])
            top= top +1# pushing bottom to next row
# moving in right form top ot bottom
            for c in range(top, bottom+1):
                res.append(matrix[c][right])
            right=right-1 #pushing wall to the left

            if top<=bottom:
                for c in range(right, left-1,-1):
                    res.append(matrix[bottom][c])
                bottom-=1

            if left<=right:
                for r in range(bottom , top-1,-1 ):
                    res.append(matrix[r][left])
                left+=1
        return res
                




        