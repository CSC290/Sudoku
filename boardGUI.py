
import pygame
from board import Sudoku

class GUI():

    def update_all(self,nums, list_pos, screen):
        numFont = pygame.font.SysFont("Sariff", 50)
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                num = numFont.render(nums[row][col], 1, (0, 0, 0))
                screen.blit(num, (list_pos[row][col][0] + 15, list_pos[row][col][1] + 10))

    def update_single(self, value,pos,screen):
        numFont = pygame.font.SysFont("Sariff", 50)
        num = numFont.render(str(value),1,(0,0,0))
        screen.blit(num,(pos[0]+15,pos[1]+10))


    def board(self):

        game = Sudoku("easy")
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


        # Setting up rectangles for each box.

        list_rect = []
        list_pos = []
        row_pos=0
        for row in range(10):
            col_pos=0
            if row%3==0:
                row_pos+=thick_line
            else:
                row_pos+=thin_line
            list_rect.append([])
            list_pos.append([])
            for col in range(10):
                if col%3==0:
                    col_pos+=thick_line
                    list_pos[row].append((row_pos,col_pos))
                    rect = pygame.draw.rect(screen,(250,250,250),pygame.Rect((row_pos,col_pos),(50,50)),0)
                    list_rect[row].append(rect)
                    col_pos = col_pos+square_size
                else:
                    col_pos += thin_line
                    list_pos[row].append((row_pos, col_pos))
                    rect = pygame.draw.rect(screen, (250, 250, 250), pygame.Rect((row_pos, col_pos), (50, 50)), 0)
                    list_rect[row].append(rect)
                    col_pos = col_pos + square_size
            if row % 3 == 0:
                row_pos = row_pos + square_size
            else:
                row_pos = row_pos + square_size
        #Setting up numbers on the board
        nums = game.board
        self.update_all(nums,list_pos,screen)


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

if __name__=='__main__':
    b=GUI()
    b.board()