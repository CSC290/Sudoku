
import pygame
from board import Sudoku
from rectangle import Rectangle

class GUI():
    square_size = 50  # Each square is 50x50
    thick_line = 4  # Every three square is separated with a thick line
    thin_line = 2
    list_rect = []
    nums = ['1','2','3','4','5','6','7','8','9']

    def update_single(self,value,pos,screen):
        if (1<=value<=9):
            numFont = pygame.font.SysFont("Sariff", 50)
            num = numFont.render(str(value),1,(0,0,0))
            screen.blit(num,(pos[0]+15,pos[1]+10))

    def draw_lines(self,screen):
        square_size = self.square_size  # Each square is 50x50
        thick_line = self.thick_line  # Every three square is separated with a thick line
        thin_line = self.thin_line
        top = 0
        BLACK = (10, 10, 10)

        for line in range(10):
            if line % 3 == 0:
                pygame.draw.lines(screen, BLACK, False, [(0, top), (480, top)], thick_line)
                pygame.draw.lines(screen, BLACK, False, [(top, 0), (top, 480)], thick_line)
                top = top + square_size + thick_line
            else:
                pygame.draw.lines(screen, BLACK, False, [(0, top), (480, top)], thin_line)
                pygame.draw.lines(screen, BLACK, False, [(top, 0), (top, 480)], thin_line)
                top = top + square_size + thin_line

    def set_up_rect(self,screen,nums):
        square_size = self.square_size  # Each square is 50x50
        thick_line = self.thick_line  # Every three square is separated with a thick line
        thin_line = self.thin_line
        row_pos = 0
        for row in range(10):
            if row<9:
                self.list_rect.append([])
            col_pos = 0
            if row % 3 == 0:
                row_pos += self.thick_line
            else:
                row_pos += self.thin_line
            for col in range(10):
                if col % 3 == 0:
                    col_pos += thick_line
                else:
                    col_pos += thin_line
                if row < 9 and col < 9:
                    num = nums[row][col]
                    if num in self.nums:
                        rect = Rectangle(num, screen, (224,238,238), (row_pos, col_pos), False)
                    else:
                        rect = Rectangle(num, screen, (250, 250, 250), (row_pos, col_pos),
                                         True)
                    self.list_rect[row].append(rect)
                    screen.blit(rect.get_num_surface(),(row_pos+15,col_pos+10))
                col_pos = col_pos + square_size
            if row % 3 == 0:
                row_pos = row_pos +square_size
            else:
                row_pos = row_pos + square_size

    def gen_index(self,x,y):
        return (x//50,y//50)

    def board(self):

        game = Sudoku("easy")
        # Setting up the screen
        pygame.init()
        screen = pygame.display.set_mode((478,478))
        screen.fill((250,250,250))
        pygame.display.set_caption('CSI Sudoku')
        nums = game.board
        #Setting up the game board
        self.draw_lines(screen)
        # Setting up rectangles and nums for each box.
        self.set_up_rect(screen,nums)

        # Got some issue here, when the mouse button down, the area color is not changing.
        highlight = []
        for i in self.list_rect:
            print(i)
            print(len(i))
        while 1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEMOTION:
                    mouse = pygame.mouse.get_pos()
                    x,y = self.gen_index(mouse[0],mouse[1])
                    if 0<=x<9 and 0<=y <9:
                        if mouse[0]< self.list_rect[x][y].get_position()[0] and mouse[1]< self.list_rect[x][y].get_position()[1]:
                            x = x-1
                            y = y-1
                        elif mouse[0]< self.list_rect[x][y].get_position()[0]:
                            x = x-1
                        elif mouse[1]< self.list_rect[x][y].get_position()[1]:
                            y = y-1
                        rect = self.list_rect[x][y]
                        rect.change_color((127,255,212))
                        position = rect.get_position()
                        if len(highlight)==0 or highlight[0]!=rect:
                            highlight.append(rect)
                        i = len(highlight)
                        while i!=1:
                            old_rect=highlight.pop(0)
                            pos = old_rect.get_position()
                            old_rect.change_color(old_rect.get_color())
                            screen.blit(old_rect.get_num_surface(), ( pos[0]+ 15, pos[1] + 10))
                            i=i-1
                        screen.blit(rect.get_num_surface(), (position[0] + 15, position[1] + 10))
                pygame.display.update()

if __name__=='__main__':
    b=GUI()
    b.board()
    print(b.list_rect)