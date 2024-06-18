import pygame
import os
import random
from itertools import combinations

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000 #Dimensions of the game window
CARD_WIDTH, CARD_HEIGHT = 100, 150 #Dimensions of each card image
CARD_GAP = 30 #Space between cards
FONT_SIZE = 24 
TIMEOUT = 30 #Timelimit for the user to find a SET
INPUT_BOX_COLOR = (200, 200, 200) #Color of the input box
BACKGROUND_COLOR = ("ghostwhite") #Background color of the game window

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Create a game window with specified width and height
pygame.display.set_caption("SET Game") #Sets the window title

# Card attributes
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']

# Generate all possible cards
list_of_81_cards_computer = [f"{col}{sym}{shad}{num}" 
                    for col in color
                    for sym in symbol
                    for shad in shading
                    for num in number]

# these 2 lists are identical, only the way the list is constructed is different
list_of_81_cards = [[col, sym, shad, num] 
                        for col in color
                        for sym in symbol
                        for shad in shading
                        for num in number]

list_of_81_random_numbers = random.sample(range(0, 81), 81)

list_12_random_numbers = list_of_81_random_numbers[:12]

# Load card images into a dictionary
card_images = {name: pygame.image.load(f'kaarten/{name}.gif') for name in list_of_81_cards_computer}


# Game variables
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']
list_of_81_cards = [[col, sym, shad, num] for col in color for sym in symbol for shad in shading for num in number] #generate all possible combinations of card attributes, resulting in 81 cards
list_of_81_random_numbers = random.sample(range(0, 81), 81) #list of 81 unique random numbers from 0 to 80, used to shuffle the deck

# Fonts
font = pygame.font.Font(None, FONT_SIZE) #Creates a font object with the specified size

# Timer
start_ticks = pygame.time.get_ticks() #Records the initial time when the game starts

class SET: 
    def __init__(self, cardlist): 
        self.color = cardlist[0]     
        self.symbol = cardlist[1]
        self.shading = cardlist[2]
        self.number = cardlist[3]

    def compare(self, other1, other2):
        def compare_color(self, other1, other2):
            return (self.color == other1.color == other2.color) or (self.color != other1.color != other2.color != self.color)

        def compare_symbol(self, other1, other2):
            return (self.symbol == other1.symbol == other2.symbol) or (self.symbol != other1.symbol != other2.symbol != self.symbol)

        def compare_number(self, other1, other2):
            return (self.number == other1.number == other2.number) or (self.number != other1.number != other2.number != self.number)

        def compare_shading(self, other1, other2):
            return (self.shading == other1.shading == other2.shading) or (self.shading != other1.shading != other2.shading != self.shading)

        return (compare_color(self, other1, other2) and
                compare_symbol(self, other1, other2) and
                compare_number(self, other1, other2) and
                compare_shading(self, other1, other2))

    def give_values(self, other1, other2):
        return ([self.color, self.symbol, self.shading, self.number],
                [other1.color, other1.symbol, other1.shading, other1.number],
                [other2.color, other2.symbol, other2.shading, other2.number])

def find_all_sets(cards):
    combs = list(combinations(range(12), 3))  
    valid_sets = []
    for combi in combs:
        card1, card2, card3 = cards[combi[0]], cards[combi[1]], cards[combi[2]]
        if card1.compare(card2, card3):
            valid_sets.append([combi[0] + 1, combi[1] + 1, combi[2] + 1])
    return valid_sets

# Function to display instructions on the screen
def draw_instructions(): 
    instructions = [
        "Find a SET among the 12 cards displayed.",
        "A SET consists of 3 cards where each attribute (color, shape, shading, number)",
        "is either all the same or all different.",
        "Enter the numbers of the 3 cards you think form a SET (e.g., 1, 5, 8).",
        "You have 30 seconds to find a SET."
    ]
    for i, line in enumerate(instructions): #Iterates through each instruction line
        text = font.render(line, True, (0, 0, 0)) #Renders the instruction text
        screen.blit(text, (20, 20 + i * 30)) #Draws the text on the screen at the specified position

def draw_timer(): #Displays the remaining time on the screen
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000 #Calculates the elapsed time in seconds
    remaining_seconds = max(TIMEOUT - elapsed_seconds, 0) #Calculates the remaining time, ensuring it does not go below zero
    timer_text = font.render(f"Time left: {remaining_seconds} seconds", True, (0, 0, 0)) #Renders the timer text
    screen.blit(timer_text, (SCREEN_WIDTH - 250, 20)) #Draws the timer text on the screen at the specified position
    return remaining_seconds > 0 #Returns True if there is time left, False otherwise

def draw_cards(card_indices): #Draws the cards on the screen
    for i, card_index in enumerate(card_indices): #Iterates through each card index
        card = list_of_81_cards[card_index] #Retrieves the card attributes
        card_name = ''.join(card) #Concatenates card attributes to form the card name
        card_image = card_images[card_name] #Retrieves the card image
        x = (i % 4) * (CARD_WIDTH + CARD_GAP) + 50 #Calculates the position to draw the card
        y = (i // 4) * (CARD_HEIGHT + CARD_GAP + 30) + 160 #Calculates the position to draw the card
        screen.blit(card_image, (x, y)) #Draws the card image on the screen
        number_text = font.render(str(i + 1), True, (0, 0, 0)) #Renders the card number
        screen.blit(number_text, (x + 45, y + 170)) #Draws the card number above the card

def get_user_input(): #Captures user input from the keyboard
    user_input = "" #Stores the user's input string
    input_active = True #Controls the input loop
    while input_active: 
        for event in pygame.event.get(): #Handles Pygame events
            if event.type == pygame.QUIT: #Exits the game if the window is closed
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN: #Handles key presses
                if event.key == pygame.K_RETURN: #Ends input on pressing Enter
                    input_active = False
                elif event.key == pygame.K_BACKSPACE: # Deletes the last character on pressing Backspace
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode #Appends the pressed key to the input string

        screen.fill(BACKGROUND_COLOR) #Clears the screen
        draw_cards(list_12_random_numbers) #Redraws the cards, instructions, and timer
        draw_instructions()
        if not draw_timer():
            input_active = False
        pygame.draw.rect(screen, INPUT_BOX_COLOR, pygame.Rect(20, 800, 760, 30)) #Draws the input box
        input_text = font.render(user_input, True, (0, 0, 0)) #Renders the input text
        screen.blit(input_text, (25, 555)) #Draws the input text
        pygame.display.flip()

    return user_input.split(', ')

# Main game loop
while len(list_of_81_random_numbers) > 11:
    list_12_random_numbers = list_of_81_random_numbers[:12]
    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]
    valid_sets = find_all_sets(cards)

    screen.fill(BACKGROUND_COLOR)
    draw_cards(list_12_random_numbers)
    draw_instructions()
    pygame.display.flip()

    user_input = get_user_input()

    if user_input and user_input[0]:
        user_input = list(map(int, user_input))
        if sorted(user_input) in valid_sets:
            print("Good Job!")
            for index in sorted(user_input, reverse=True):
                del list_of_81_random_numbers[index - 1] #Removes the cards forming the SET from the list
            start_ticks = pygame.time.get_ticks() #Resets the timer
        else:
            print("Unfortunately not.")
    else:
        print("Timeout! The computer will try.")
        if valid_sets:
            answer_computer = valid_sets[0]
            print(f"Computer found a set: {answer_computer}")
            for index in sorted(answer_computer, reverse=True):
                del list_of_81_random_numbers[index - 1]
        else:
            del list_of_81_random_numbers[9:11] #Removes two cards if no valid SETs are found. If we want to remove 3 cards we need to write [9:12], oronly one [11]
        start_ticks = pygame.time.get_ticks()

    if len(list_of_81_random_numbers) < 12:
        break

pygame.quit()


#####NOTE
# Render sonething means to process and display it visually