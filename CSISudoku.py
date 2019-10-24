from __future__ import annotations
from typing import List,Tuple

class Sudoku():
    """
    Setting up the sudoku board and game mechanism.
    """

    def __init__(self,filename:str):
        """
        Import sudoku starting board values from filename. And sets up the board.

        Note:
            Default board size is 9x9 square.
            Empty space is represented as a'x'.
        """
        # Private attributes
        # filename
        #     The file we import board value from
        # board
        #     All symbols filed board
        # values
        #     All possible values
        filename:str
        board:List[List[str]]
        values:Tuple[str]

        file=open(filename)
        self.board=[]
        self.values=('1','2','3','4','5','6','7','8','9')
        #TODO: Setting up the board based on inputs in file.


    def to_string(self,board:List[List[str]])-> None:
        """
        Print the board in one string.
        """
        #TODO: Finish the print
        values=

        print()


    def move(self,row:int,col:int,value:int)-> None:
        """
        Adding the value to given row and col if the spot is valid to move.
        Check the availability of the spot by has_move method
        """
        #TODO: Complete move


    def has_move(self,row:int,col:int,value:int)-> bool:
        """
        Check if the given row, col spot is available to add the value.
        Check the range of row and col
        Check if the given spot is empty

        Note:
            This method only checks the availability not correctness.
        """
        #TODO: Complete has_move


    def remove(self,row:int,col:int,value:int)-> None:
        """
        Remove the value of given row and col spot to 'x'

        Note:
            In this method, player can remove the starter value.
            The access will be blocked in GUI.
        """
        # TODO: Complete remove

    def check_row(self,row:int) -> bool:
        """
        check if the spots on given row has no duplicated values.
        """
        # TODO:Complete check_row

    def check_col(self,col:int)-> bool:
        """
        check if the spots on given col has no duplicated values.
        """
        # TODO: Complete check_col

    def check_sub(self,s:int)-> bool:
        """
        check if the given sub-square has no duplicated values.
        # Note:
        #   We have 9 sub-squares.
        #   The first row of squares are 0,1,2 sub-square.
        #   The second row of squares are 3,4,5 sub-square.
        #   The Third row of squares are 6,7,8 sub-square
        """
        sub_row=s//3    # sub_row is the row of where the sub-square is
        sub_col=s%3     # sub_col is the col of where the sub-square is
        sub_square=[]
        for row in range(sub_row*3,(sub_row+1)*3):
            sub_square+=self.board[row][sub_col*3:(sub_col+1)*3]
        for v in self.values:
            if not v in sub_square:
                return False
        return True

    def is_filled(self)-> bool:
        """
        check if the board is all filled.
        """
        for row in self.board:
            if 'x' in row:
                return False
        return True

    def game_over(self)-> bool:
        """
        Check if the board is full, and filled properly.
        Will be called when there is no empty space on board.

        Note:
            this also checks correctness.
        """
        if self.is_filled():
            for val in range(len(self.board)):
                if not (self.check_row(val) and self.check_col(val)):
                    return False
            for s in range(9):
                if not (self.check_sub(s)):
                    return False
            return True
        return False
