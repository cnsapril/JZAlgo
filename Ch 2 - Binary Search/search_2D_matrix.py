"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution(object):
    def search_matrix_twice(self, matrix, target):
        if not matrix or matrix is None:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, down = 0, len(matrix) - 1
        row = None
        while top + 1 < down:
            row_m = top + (down - top)/2
            if target == matrix[row_m][0] or target == matrix[row_m][-1]:
                return True
            elif matrix[row_m][0] <= target <= matrix[row_m][-1]:
                row = row_m
                break
            elif matrix[row_m][0] > target:
                down = row_m
            elif matrix[row_m][-1] < target:
                top = row_m

        if row is None:
            if matrix[top][0] <= target <= matrix[top][-1]:
                row = top
            elif matrix[down][0] <= target <= matrix[down][-1]:
                row = down
            else:
                return False

        left, right = 0, len(matrix[row]) - 1
        while left + 1 < right:
            m = left + (right - left)/2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                right = m
            else:
                left = m

        if matrix[row][left] == target or matrix[row][right] == target:
            return True

        return False

    def search_matrix_once(self, matrix, target):
        if not matrix or matrix is None:
            return False

        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1

        while start + 1 < end:
            mid = start + (end - start)/2
            x, y = mid / m, mid % m
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid
            else:
                start = mid

        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True

        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False


sol = Solution()
print sol.search_matrix_once([[1,5,10,11,16,23,24,26,29,34,41,48,49,56,63,67,71,74,75],[97,118,131,150,160,182,202,226,251,273,289,310,326,349,368,390,401,412,428],[445,455,466,483,501,519,538,560,581,606,631,643,653,678,702,726,748,766,781],[792,817,837,858,872,884,901,920,936,957,972,982,1001,1024,1044,1063,1086,1098,1111],[1129,1151,1172,1194,1213,1224,1234,1250,1267,1279,1289,1310,1327,1348,1371,1393,1414,1436,1452],[1467,1477,1494,1510,1526,1550,1568,1585,1599,1615,1625,1649,1663,1674,1693,1710,1735,1750,1769]], 1086)
