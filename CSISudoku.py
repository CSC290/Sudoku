from __future__ import annotations
from typing import List,Tuple
import random

easyboards = {
    1: [["4","6","9","","7","1","","",""],["","5","1","4","","","","","3"],["","","8","","","","4","","6"],["1","","7","5","9","","8","2",""],["","","4","","","","","",""],["8","","","2","3","","","5",""],["6","","","","","","9","",""],["","","","","","","","",""],["","","","","8","2","","3",""]]
,   2: [["","9","","8","1","5","","3",""],["","","1","","","","4","","9"],["6","","","","","","5","",""],["3","","7","","","","","",""],["","","","","","6","","",""],["","","","","","","9","2","4"],["","","8","","","","","",""],["4","","","","6","","8","","2"],["2","7","","","9","8","3","6",""]]
,   3: [["","","3","","8","4","","2",""],["","","","","","9","","",""],["","","","6","","","","3","5"],["3","1","","","4","","6","","9"],["","9","2","","","","","",""],["","7","4","","","","","5","8"],["","","","","","1","","",""],["","","9","","","","","",""],["8","4","","7","9","5","","",""]]
,   4: [["","","","7","","","1","",""],["","1","","3","","","7","6",""], ["","9","7","","","8","","","2"], ["3","","","","7","1","","4",""], ["2","7","","","","","9","",""], ["1","","","","","2","3","4","5"], ["7","4","","3","","","8","","3"], ["3","5","","4","4","7","","1","9"], ["","","","9","","5","4","2","4"]]
}
hardboards = {
    1: [["","","3","2","9","4","7","",""],["","","","","","","6","8",""],["","","2","","","","","",""],["","","4","3","","","","9",""],["","","","9","1","6","2","",""],["8","","","","","","","",""],["","5","","","","","","","9"],["1","","","","","7","","",""],["","","","","6","","8","",""]],
    2: [["","5","6","","","","","2",""],["9","","4","","","","","",""],["","2","","","6","","","5",""],["","","7","6","","","","",""],["","","","","","1","","7",""],["","6","","","2","","","8",""],["","","","1","","","","","3"],["","7","2","","","","4","",""],["4","","","","","8","2","",""]],
    3: [["6","","7","5","","4","","",""],["4","","","","","","","",""],["","8","","","1","9","","",""],["","","1","","","2","","9","5"],["","4","","","","","","2",""],["2","6","","8","","","4","",""],["","","","6","3","","","5",""],["","","","","","","","","7"],["","","","7","","5","8","","2"]],
    4: [["1","","","","","","","5","6"], ["","","","2","","5","","",""], ["2","5","","7","8","","","",""],["","","","","1","3","","", ""],["6","8","","","","","","",""], ["","","","","","","4","","3"],["7","1","","","","","3","2",""],["","6","","8","5","","","",""],["","","","","","","","5","6"]]
}
class Sudoku():
    """
    Setting up the sudoku board and game mechanism.
    """

    def __init__(self, mode:str):
        """
        Import sudoku starting board values from filename. And sets up the board.

        Note:
            Default board size is 9x9 square.
            Empty space is represented as a'x'.
        """
        # Private attributes
        # mode
        #     The desired difficulty level for the game
        # board
        #     All symbols filed board
        # values
        #     All possible values

        mode:str
        board:List[List[str]]
        values:Tuple[str]

        self.mode = mode
        num = random.randint(1,4)
        if self.mode == "easy":
            self.board = easyboards[num]

        else:
            self.board = hardboards[num]

        self.values = ("1","2","3","4","5","6","7","8","9")

    def __str__(self):
        """
        Print the board in one string.
        """
        board = ""
        # for list in self.board:
        #     printB += str(list)
        #     printB += "\n"

        for i in range(len(self.board)):
            str = ""
            for j in range(len(self.board[i])):
                if self.board[i][j] == "":
                    board += "  |__|  "
                else:
                    board += " | " + self.board[i][j] + " | "
            board += "\n \n"
        return board


    def has_move(self, row:int, col:int, value:int)-> bool:
        """
        Check if the given row, col spot is available to add the value.
        Check the range of row and col
        Check if the given spot is empty

        Note:
            This method only checks the availability not correctness.
        """
        if self.check_row(row, value):
            if self.check_col(col, value):
                if self.check_sub(row, col, value):
                    return True
        return False


    def move(self, row:int, col:int, value:int)-> None:
        """
        Adding the value to given row and col if the spot is valid to move.
        Check the availability of the spot by has_move method
        """
        if row>8 or col>8 or row<0 or col<0:
            return None
        if self.has_move(row, col, value):
            self.board[row][col] = str(value)


    def remove(self,row:int,col:int,value:int)-> None:
        """
        Remove the value of given row and col spot to 'x'

        Note:
            In this method, player can remove the starter value.
            The access will be blocked in GUI.
        """
        self.board[row][col] = ""

    def check_row(self, row:int, value:int) -> bool:
        """
        return True if value not in row
        """
        return not str(value) in self.board[row]

    def check_col(self,col:int, value:int)-> bool:
        """
        return True if the value is not in the column
        """
        for list in self.board:
            if list[col] == str(value):
                return False
        return True

    def check_sub(self, row:int, col:int, value)-> bool:
        """
        check if the given sub-square has no duplicated values.
        # Note:
        #   We have 9 sub-squares.
        #   The first row of squares are 0,1,2 sub-square.
        #   The second row of squares are 3,4,5 sub-square.
        #   The Third row of squares are 6,7,8 sub-square
        """
        sub_row=row//3    # sub_row is the row of where the sub-square is
        sub_col=col//3     # sub_col is the col of where the sub-square is
        sub_square=[]
        for i in range(3):
            for c in range(3):
                sub_square.append(self.board[sub_row+i][sub_col+c])
        return str(value) not in sub_square

    def is_filled(self)-> bool:
        """
        check if the board is all filled.
        """
        for row in self.board:
            if "" in row:
                return False
        return True

    def game_over(self)-> bool:
        """
        Check if the board is full, and filled properly.
        Will be called when there is no empty space on board.

        Note:
            this also checks correctness.
        """
        for row in self.board:
            if set(row) != self.values:
                return False
        for value in range(9):
            for col in range(9):
                if not self.check_col(col, value):
                    return False
        #check subSquares
        return True
