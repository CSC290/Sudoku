
import pygame

class Rectangle():

    def __init__(self,num,screen,color,position,editable):
        self.screen = screen
        self.position=position
        self.rect = pygame.Rect(position,(50,50))
        self.editable = editable
        self.rect = pygame.draw.rect(screen,color,self.rect,0)
        self.numFont = pygame.font.SysFont("Sariff", 50)
        self.num = num
        self.num_surface= self.numFont.render(num, 1, (0, 0, 0))
        self.color = color
        self.selected = False

    def change_num(self,num):
        if self.editable:
            self.num = num
            self.num_surface= self.numFont.render(num, 1, (0, 0, 0))

    def change_color(self,color):
        self.rect = pygame.draw.rect(self.screen,color,self.rect,0)

    def select(self):
        self.selected=True

    def unselect(self):
        self.selected=False