import pygame
import random
from itertools import combinations

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700 #Dimensions of the game window
CARD_WIDTH, CARD_HEIGHT = 100, 150 #Dimensions of each card image
CARD_GAP = 40 #Space between cards
FONT_SIZE = 24 
FONT_SIZE1 = 50
FONT_SIZE2 = 18
TIMEOUT = 3 #Timelimit for the user to find a SET
INPUT_BOX_COLOR = ("orchid4") #Color of the input box
BACKGROUND_COLOR = ("ghostwhite") #Background color of the game window
score_comp = 0

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
font1 = pygame.font.Font(None, FONT_SIZE1)
font2 = pygame.font.Font(None, FONT_SIZE2)

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
        x = (i % 6) * (CARD_WIDTH + CARD_GAP) + 50 #Calculates the position to draw the card
        y = (i // 6) * (CARD_HEIGHT + CARD_GAP + 60) + 160 #Calculates the position to draw the card
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
        pygame.draw.rect(screen, INPUT_BOX_COLOR, pygame.Rect(160, 640, 100, 30)) #Draws the input box
        comment = font2.render("What SET did you find?", True, (0,0,0))
        screen.blit(comment, (25, 650))
        input_text = font.render(user_input, True, "white") #Renders the input text
        screen.blit(input_text, (170, 648)) #Draws the input text
        pygame.display.flip()

    return user_input.split(', ')
def draw_score_computer(score_computer):
    text = font.render(f"Score Computer: {score_computer}", True, (0,0,0))
    screen.blit(text, (SCREEN_WIDTH - 250, 40))
    pygame.display.flip()


# Main game loop
while len(list_of_81_random_numbers) > 11:
    list_12_random_numbers = list_of_81_random_numbers[:12]
    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]
    valid_sets = find_all_sets(cards)

    screen.fill(BACKGROUND_COLOR)
    draw_cards(list_12_random_numbers)
    draw_instructions()  
    draw_score_computer(score_comp)
    pygame.display.flip()
    user_input = get_user_input()
   
    if user_input and user_input[0]:
        user_input = list(map(int, user_input))
        if sorted(user_input) in valid_sets:
            text = font1.render("Good Job!", True, (0,0,0))
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(2000)
            for index in sorted(user_input, reverse=True):
                del list_of_81_random_numbers[index - 1] #Removes the cards forming the SET from the list
            start_ticks = pygame.time.get_ticks() #Resets the timer
        else:
            text = font1.render("Unfortunately not.", True, (0,0,0))
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(2000)
    else:
        text = font1.render("Time out! The computer will have a try.", True, (0,0,0))
        screen.blit(text, (150, 370))
        pygame.display.flip()
        pygame.time.wait(1000)
        if valid_sets:
            pygame.display.flip()
            pygame.time.wait(1000)
            answer_computer = valid_sets[0]
            text = font1.render(f"Computer found a set: {answer_computer[0], answer_computer[1], answer_computer[2]}", True, (0,0,0))
            screen.blit(text, (300, 640))
            score_comp += 1
            #draw_score_computer(score_comp)
            
            pygame.display.flip()
            pygame.time.wait(2000)
            for index in sorted(answer_computer, reverse=True):
                del list_of_81_random_numbers[index - 1]
        else:
            text = font1.render("No SET found among these cards.", True, (0,0,0))
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(1000)
            del list_of_81_random_numbers[9:12] #Removes three cards if no valid SETs are found.
        start_ticks = pygame.time.get_ticks()

    if len(list_of_81_random_numbers) < 12 and len(valid_sets) == 0:
            text = font1.render("FINISHED!", True, (0,0,0)) # Dit werkt nog niet.
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(5000)
            break

            
pygame.quit()


#####
# Render sonething means to process and display it visually