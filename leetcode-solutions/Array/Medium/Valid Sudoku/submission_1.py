# Problem: Valid Sudoku
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowcheck(board,row,number): 
            c=0
            for i in board[row]:  
                if i==number:
                    c+=1
            return  False if c==1 else True 
        def colcheck(board,col,number): 
            c=0
            for i in board:
                if i[col] == number:
                    c+=1
            return  False if c==1 else True 
        def subboxcheck(board,row,column,number):
            c=0
            myrow = (row // 3) * 3
            mycol = (column // 3) * 3 
            for i in range(myrow,myrow+3):
                for j in range(mycol,mycol+3):   
                    if board[i][j]==number:
                        c+=1
            return False if c==1 else True   
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue 
                else:
                    if rowcheck(board,i,board[i][j]) or colcheck(board,j,board[i][j]) or subboxcheck(board,i,j,board[i][j]):
                        return False
        return True
