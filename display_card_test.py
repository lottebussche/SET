import pygame
import random
import os

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up the display
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MARGIN = 20
CARD_GAP = 10
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SET Card Display')
clock = pygame.time.Clock()

# Card attributes
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']

# Generate all possible cards
list_of_81_cards = [[a, b, c, d]
                    for a in color
                    for b in symbol
                    for c in shading
                    for d in number]

# Load images
card_images = {}
for card in list_of_81_cards:
    card_name = f"{card[0]}{card[1]}{card[2]}{card[3]}"
    card_images[card_name] = pygame.image.load(os.path.join("kaarten", f"{card_name}.gif"))

# Function to create a SET card object
class SETCard:
    def __init__(self, cardlist, index):
        self.color = cardlist[0]
        self.symbol = cardlist[1]
        self.shading = cardlist[2]
        self.number = cardlist[3]
        self.index = index
        self.selected = False
        self.image = card_images[f"{self.color}{self.symbol}{self.shading}{self.number}"]

    def __str__(self):
        return f"Card {self.index + 1}: {self.color} {self.shading} {self.symbol} {self.number}"

# Function to draw cards on the screen
def draw_cards(cards):
    screen.fill(WHITE)
    for i, card in enumerate(cards):
        x = MARGIN + (CARD_WIDTH + CARD_GAP) * (i % 4)
        y = MARGIN + (CARD_HEIGHT + CARD_GAP) * (i // 4)
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        color = GRAY if card.selected else WHITE
        pygame.draw.rect(screen, color, rect)
        screen.blit(card.image, (x, y))
    pygame.display.flip()

# Create initial set of 12 cards
cards = [SETCard(list_of_81_cards[i], i) for i in random.sample(range(81), 12)]

# Main loop to display the cards
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_cards(cards)

pygame.quit()
