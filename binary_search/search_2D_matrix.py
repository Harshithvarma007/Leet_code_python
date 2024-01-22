class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchrow(matrix, target):
            for i in range(len(matrix) - 1):
                if target == matrix[i][0]:  # Assuming the target is in the first column of each row
                    return [i, 0]
                elif target > matrix[i][0] and target < matrix[i + 1][0]:
                    return [i]
            return [len(matrix) - 1]  # Return the last row if not found in previous rows

        row = searchrow(matrix, target)

        if len(row) == 2:
            return True
        else:
            low, high = 0, len(matrix[row[0]]) - 1

            while low <= high:
                mid = (low + high) // 2

                if matrix[row[0]][mid] == target:
                    return True
                elif matrix[row[0]][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False
