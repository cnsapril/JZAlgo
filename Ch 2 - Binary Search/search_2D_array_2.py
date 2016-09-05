class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    # Use Binary Search (Time Complexity = O(nlogn))
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or not matrix:
            return 0

        start, end = 0, len(matrix) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] > target:
                end = mid
            else:
                start = mid

        row = -1
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start

        count = 0
        length = len(matrix[0])
        for i in range(row + 1):
            start, end = 0, length - 1
            while start + 1 < end:
                mid = start + (end - start) / 2
                if matrix[i][mid] == target:
                    count += 1
                    break
                elif matrix[i][mid] > target:
                    end = mid
                else:
                    start = mid
            if matrix[i][start] == target:
                count += 1
            elif matrix[i][end] == target:
                count += 1

        return count

    # Fast answer (no binary search technique involved)
    def search_matrix_fast(self, matrix, target):
        if matrix is None or not matrix or not matrix[0]:
            return -1

        row_len, col_len = len(matrix), len(matrix[0])

        # Search from bottom left to top right, since all matrix[x][i] > matrix[x-1][i] and
        # matrix[x][i] > matrix[x][i-1]
        x, y = row_len - 1, 0
        count = 0

        while x >= 0 and y < col_len:
            # If the current item is larger than the target, move up a level to find smaller items
            if matrix[x][y] > target:
                x -= 1
            # If the current item is smaller than the target, move to the next item horizontally
            elif matrix[x][y] < target:
                y += 1
            # If the current item equals to the target, increase count and move to the top right corner by 1 unit
            else:
                count += 1
                x -= 1
                y += 1

        return count


sol = Solution()
lst = [
        [1, 3, 5, 7],
        [3, 4, 7, 8],
        [4, 8, 9, 10]
       ]
print sol.search_matrix_fast(lst, 3)
