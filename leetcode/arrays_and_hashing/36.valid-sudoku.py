#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Horizontal traversal
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)
        #Vertical 
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                if item != '.':
                    s.add(item)
        #Boxes
        box_values = [(0, 0), (0, 3), (0, 6),
                      (3, 0), (3, 3), (3, 6),
                      (6, 0), (6, 3), (6, 6)]
        for n, m in box_values:
            x = set()
            for row in (n, n + 3):
                for col in (m, m + 3):
                    num = box_values[row][col]
                    if num in x:
                        return False
                    elif num != '.':
                        x.add(num)
        return True

# @lc code=end

