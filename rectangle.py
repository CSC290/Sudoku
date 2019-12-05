
import pygame

class Rectangle():
    """
    Rectangle creates pygame.Rect and stores all the information we needs to use in boardGUI.
    """

    def __init__(self,num,screen,color,position,editable):
        """
        Create pygame.Rect based on given screen, color and position and display num in the center of rectangle.
        If the rectangle is editable then editable is true, false the opposite.
        :param num: string
        :param screen: pygame.display.screen
        :param color: pygame.Color
        :param position: Tuple(row,col)
        :param editable: boolean

        Private Attributes:
            screen: pygame.display.Screen
                The screen that we put rectangles in
            position: Tuple(row,col)
                The position on the screen of rectangle
            rect: pygame.Rect
                The rectangle we display on the screen base on the position and color given
            editable: boolean
                If this rectangle is not prefixed then editable is true.
            numFont: pygame.font
                Set up the font of num we display on the screen
            num: string
                The number at this rectangle on board
            num_surface: rectangle.numFont
                Generate surface for blitting nums on screen
            color: pygame.Color
                Color of this rectangle
            selected: boolean
                If this rectangle is selected on GUI then is true, false the opposite.
        """
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
        """
        If this rectangle is editable, then change the attributes num.
        :param num: string
        :return: None
        """
        if self.editable:
            self.num = num
            self.num_surface= self.numFont.render(num, 1, (0, 0, 0))

    def change_color(self,color):
        """
        change the color of rectangle on display by creating a new pygame.Rect.
        :param color: pygame.Color
        :return: None
        """
        self.rect = pygame.draw.rect(self.screen,color,self.rect,0)

    def select(self):
        """
        change the selected attributes to true
        :return: None
        """
        self.selected=True

    def unselect(self):
        """
        change the selected attributes to false
        :return: None
        """
        self.selected=False