import pygame
import thorpy




application = thorpy.Application(size=(600, 800), caption="SUDOKU")
thorpy.theme.set_theme('human')

title = thorpy.make_text("SUDOKU", 80, (255,255,255))
title.set_topleft((200,200))

#Picture for menu
normal = "sudoku.png"
pic_button = thorpy.make_image_button(normal,
                                    alpha=255,
                                    colorkey=(100,200,100))

#Start Button
start = thorpy.make_button("START")
start.set_font("Bahnschrift SemiBold")
start.set_main_color((0,148,0))
start.set_font_color((255,255,255))
start.set_font_size(40)
start.set_size((200,100))
start.center()

def switch(event):
    easy = thorpy.make_button("EASY")
    easy.set_font("Bahnschrift SemiBold")
    easy.set_main_color((0, 148, 0))
    easy.set_font_color((255, 255, 255))
    easy.set_font_size(40)
    easy.set_size((200, 100))
    easy.center()

    hard = thorpy.make_button("HARD")
    hard.set_font("Bahnschrift SemiBold")
    hard.set_main_color((0, 148, 0))
    hard.set_font_color((255, 255, 255))
    hard.set_font_size(40)
    hard.set_size((200, 100))
    hard.center()

    background2 = thorpy.Background(color=(0, 102, 204),
                               elements=[easy, hard])
    thorpy.store(background2)
    menu = thorpy.Menu(background2)
    menu.play()
reaction = thorpy.Reaction(reacts_to=pygame.MOUSEBUTTONDOWN, reac_func=switch)
start.add_reaction(reaction)



#Quit button
quit = thorpy.make_button("QUIT", func=thorpy.functions.quit_menu_func)
quit.set_font_size(40)
quit.set_font("Bahnschrift SemiBold")
quit.set_main_color((0,148,0))
quit.set_font_color((255,255,255))
quit.set_size((200,100))
quit.center()

#Setting background and adding elements to background
background = thorpy.Background(color=(0, 102, 204),
                               elements=[pic_button, title, start, quit])
thorpy.store(background)

#Adding background to menu and launching menu.
menu = thorpy.Menu(background)
menu.play()


