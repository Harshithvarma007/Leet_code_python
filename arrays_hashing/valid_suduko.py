class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def hasduplicates(list):
            seen =set()
            for value in list:
                if value !='.':
                    if value in seen:
                        return True
                    seen.add(value)
            return False
        
        for row in range(9):
            if hasduplicates(board[row]):
                return False
        
        for col in range(9):
            column=[board[row][col] for row in range(9)]
            if hasduplicates(column):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                subbox=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if hasduplicates(subbox):
                    return False
        return True


        