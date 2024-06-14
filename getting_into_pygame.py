import pygame
from pygame.locals import *
import os
import sys

#https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
#how it works: we need a event that is entering 3 numbers, in the 'blue box'.

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Basic Pygame program')

    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250)) #color??

    # Display some text
    font = pygame.font.Font(None, 36)                   # Loads the default font at size 36
    text = font.render("SET game", 1, (10, 10, 10))     #titel maken in zwart
    textpos = text.get_rect()                           #Gets the rectangle area of the text
    image = pygame.image.load(os.path.join("kaarten\greendiamondempty1.gif"))   #Loads an image from the specified path
    text_input_box = pygame.Rect(150, 150, 150, 32)     #Creates a rectangular area for the text input box with specified dimensions
    
    textpos.centerx = background.get_rect().centerx #displays picture in the middle top of screen
    # blit makes a picture visible
    background.blit(text, textpos)  #text displayen
    background.blit(image, (10,10)) # shows picture in coordinates (x,y)
    # Blit everything to the screen
    screen.blit(background, (0, 0))     #achtergrond laten zien
    pygame.draw.rect(screen, (0, 0,200), text_input_box)        #text box laten zien, met (a,b,c) de kleurcodes
    pygame.display.flip()                  #alles uploaden ofzo

    # Event loop
    #events are  mouse clicks, keyboard inputs, or screen touches, timers,...
    while True: 
        for event in pygame.event.get(): 
    
        # if user types QUIT then the screen will close 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
                # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                if text_input_box.collidepoint(event.pos):
                # checking if key "A" was pressed
                    if event.key == pygame.K_a:
                        print("Key A has been pressed")
                        
            pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__': main()