import pygame
import sys
import random

#Start up pygme
pygame.init()

# Determine the screen 
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("SET: Malou ter Horst, Lotte Bussche, Laura Mercenier, Julia van Oostrom")

# Card attributes
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']

# Generate all possible cards
list_of_81_cards = [f"{col}{sym}{shad}{num}" 
                    for col in color
                    for sym in symbol
                    for shad in shading
                    for num in number]

# Load card images into a dictionary
card_images = {name: pygame.image.load(f'kaarten/{name}.gif') for name in list_of_81_cards}

# Determine positions to display some cards
display_cards = random.sample(list_of_81_cards, 12)
print(display_cards)

# Hier denk ik dat het probleem zit, we moeten iets doen dat vanaf kaart 4 en 8 de kaarten lager komen.
card_positions = []
for i in range(0, 4):
    place = [10 + i * 110, 10]
    card_positions.append(place)
for i in range(0, 4):
    place = [10 + i * 110, 225]
    card_positions.append(place)
for i in range(0, 4):
    place = [10 + i * 110, 440]
    card_positions.append(place)
#card_positions.append(10 + i * 110, 50 for i in display_cards[:4])
#card_positions.append(10 + i * 110, 150 for i in display_cards[4:9])
#card_positions.append(10 + i * 110, 250 for i in display_cards[9:13])
print(card_positions)
#for i in range(5):
    #card_positions.append ((40 + i * 110, 100))
#for i in range (5-11): 
    #card_positions.append ((40 + (i-5) * 110, 300))

#Hierdoor print je wel wat maar alles op een rij:
#card_positions = [(10 + i * 110, 50) for i in range(len(display_cards) // 4)]

# Game loop, neccesery to end the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen color
    screen.fill(('Red'))

    # Image the cards
    for i, card_name in enumerate(display_cards):
        card_image = card_images[card_name]
        screen.blit(card_image, card_positions[i])

    # Keep the screen and pygame updated 
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
