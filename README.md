# Sudoku
Sudoku is a logic-based board game. Our game is implemented using `python`. `pygame` and `tropy`.  

## Navigation
<a name="top"></a> 
1. [Game Description](#intro) 
2. [Game Controls and Features](#feature)
3. [How to Install Flipsies](#install)
4. [Documentation](#documen)
5. [Authors](#Authors)
6. [License Information](#license)
7. [Individual Contribution](#contribution)

## <a name="intro"></a>Game Description 
Sudoku is a single player game built in python.

The rules of Sudoku are very simple. Player needs to use number from 1-9 fill in the board without any repetition of numbers in same row/col/subgrid. 

The player can mouse click on any small box, when the color of selected box turns into green that means player selected successfully. After a box is selected, player can press 1-9 button on your keyboard to input value. However, player is not allowed to select the boxes with grey color since those are intial values. Also, player can change the inputed box by the same action mentioned above. The win condition of Sudoku is that all the boxes are filled and rules are satisfied.

[Back to top](#top)

## <a name="feature"></a>Game Controls and Features 

This game requires both mouse control and keyboard input.

The menu screen contains a 'Play' button and 'Quit' button.
- Click on the 'Play' button to generating game board.
- Click on the 'Quit' button to quit the game.

The board screen contains 9x9 grid (3x3 sub-grid).
- Click on any small box to select and press 1-9 on keyboard to input value.
- Change value by repeating last step.
- The grey box is prefixed. The value in that box cannot be changed.

Once you filled in all the boxes and rules are satisfied, the game quits automatically, that means you won.

[Back to top](#top)

## <a name="install"></a>How to Install Flipsies

First, make sure you have python 3 on your device.

Second, download `Pygame` [here.](https://www.pygame.org/download.shtml)

Third, download `Tropy` [here.](https://tropy.org)

Fourth, clone our repo by `git clone https://github.com/CSC290/Sudoku.git` in Terminal or go to our repo web [here](https://github.com/CSC290/Sudoku) and download the zip file.

Last, run the menuGUI. Then enjoy the game.

[Back to top](#top)

## <a name="documen"></a>Documentation and Directory Structure

`board.py` is the file that creating the game board and game mechanism.(move, game_over, remove and more)

`boardGUI.py` is the file that generates 9x9 grid and filled in with prefixed numbers. This file hooked up with `board.py`. We implement `pygame` here.

`sudoku.png` is a image of sudoku which displays in `menuGUI.py`.

`menuGUI.py` is the file that generates starting menu. This file hooked up with `boardGUI.py`, so player can select 'start' button to run `boardGUI.py`. We implement `tropy` here.

`rectangle.py` is the file that generates `pygame.Rect` and stores all the attributes of rectangle we needed to build small boxes in `boardGUI.py`.

[Back to top](#top)

## <a name="Authors"></a>Authors

CSI (computer science intelligence) is a group of 2nd year computer science stidents at University of Toronto. This project is designed for course requirement in CSC290.

Authors are listed below:
- Kamran
- Huzaifa
- Yousef Akiba
- Litao Chen

[Back to top](#top)

## <a name="license"></a>License Information

MIT License

Copyright (c) [2019] [Litao Chen,Kamran, Yousef, Huzaifa]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back to top](#top)

## <a name="contribution"></a>Individual Contribution

# Litao Chen
For the code part, I contributed doc string and partial codes writing for `board.py`. I also fully contributed `boardGUI.py` and `rectangle.py`.
I contributed all the readMe excpet other people's Individual Contribution and #Sudoku.
 
