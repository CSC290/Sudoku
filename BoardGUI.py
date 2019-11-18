
import pygame


class GUI():

    def board(self):
        # Setting up the screen
        pygame.init()
        screen = pygame.display.set_mode((480,480))
        screen.fill((250,250,250))
        pygame.display.set_caption('CSI Sudoku')

        # Setting up the game board
        square_size=50      # Each square is 50x50
        thick_line=4        # Every three square is separated with a thick line
        thin_line=2
        top=0
        BLACK=(10,10,10)

        for line in range(10):
            if line%3==0:
                pygame.draw.lines(screen, BLACK, False, [(0,top),(480,top)], thick_line)
                pygame.draw.lines(screen, BLACK, False, [(top,0), (top,480)], thick_line)
                top=top+square_size+thick_line
            else:
                pygame.draw.lines(screen, BLACK, False, [(0, top), (480, top)], thin_line)
                pygame.draw.lines(screen, BLACK, False, [(top, 0), (top, 480)], thin_line)
                top=top+square_size+thin_line


        # list_pos is storing all the points of each intersection between each line
        # list_pos is a double_nested list of Tuple
        # So we can use the position of points to define which area the mouse is reacting to.
        list_pos = []
        row_pos=0
        for row in range(10):
            col_pos=0
            if row%3==0:
                row_pos+=thick_line
            else:
                row_pos+=thin_line
            list_pos.append([])
            for col in range(10):
                if row%3==0:
                    col_pos+=thick_line
                    list_pos[row].append((row_pos, col_pos))
                    col_pos = col_pos+square_size+thick_line
                else:
                    col_pos += thin_line
                    list_pos[row].append((row_pos, col_pos))
                    col_pos = col_pos + square_size + thin_line
            if row % 3 == 0:
                row_pos = row_pos + square_size + thick_line
            else:
                row_pos = row_pos + square_size + thin_line

        """ list_pos should be something like this refer to the points on board
        [[(0, 0), (0, 54), (0, 108), (0, 162), (0, 216), (0, 270), (0, 324), (0, 378), (0, 432), (0, 486)]
        [(54, 0), (54, 52), (54, 104), (54, 156), (54, 208), (54, 260), (54, 312), (54, 364), (54, 416), (54, 468)]
        [(106, 0), (106, 52), (106, 104), (106, 156), (106, 208), (106, 260), (106, 312), (106, 364), (106, 416), (106, 468)]
        [(158, 0), (158, 54), (158, 108), (158, 162), (158, 216), (158, 270), (158, 324), (158, 378), (158, 432), (158, 486)]
        [(212, 0), (212, 52), (212, 104), (212, 156), (212, 208), (212, 260), (212, 312), (212, 364), (212, 416), (212, 468)]
        [(264, 0), (264, 52), (264, 104), (264, 156), (264, 208), (264, 260), (264, 312), (264, 364), (264, 416), (264, 468)]
        [(316, 0), (316, 54), (316, 108), (316, 162), (316, 216), (316, 270), (316, 324), (316, 378), (316, 432), (316, 486)]
        [(370, 0), (370, 52), (370, 104), (370, 156), (370, 208), (370, 260), (370, 312), (370, 364), (370, 416), (370, 468)]
        [(422, 0), (422, 52), (422, 104), (422, 156), (422, 208), (422, 260), (422, 312), (422, 364), (422, 416), (422, 468)]
        [(474, 0), (474, 54), (474, 108), (474, 162), (474, 216), (474, 270), (474, 324), (474, 378), (474, 432), (474, 486)]]
        """

        # Got some issue here, when the mouse button down, the desired area color is not changing.
        while 1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    for pos in range(len(list_pos)):
                        if mouse[0]<list_pos[pos][0][0]:
                            for pindex in range(pos):
                                if mouse[1]<list_pos[pos][pindex][1]:
                                    pygame.draw.rect(screen, (50,50,50), (list_pos[pos-1][pindex-1][0],
                                                                     list_pos[pos-1][pindex-1][1], 50, 50), 0)
                                    screen.update()
                                break


                pygame.display.update()


if __name__ == '__main__':
    b = GUI()
    b.board()
