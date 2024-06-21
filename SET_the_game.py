import pygame
import random
from itertools import combinations

# Initialize Pygame
pygame.init()

# Constants
screen_width, screen_height = 1000, 700 #Dimensions of the game window, so what is the height and width. 
card_width, card_height = 100, 150 #Dimensions of each card image, so again what is the height and width.
card_gap = 40 #Space between cards
# Below are the font sizes, so what size are the different texts displayed on the screen.
font_size_1 = 24 
font_size_2 = 50
font_size_3 = 18
timeout = 30 #Timelimit for the user to find a SET at the beginning of the game.
input_box_color = ("orchid4") #Color of the input box (the box at the bottom of the screen, with the blinking cursor)
background_color = ("ghostwhite") #Background color of the game window
score_comp = 0 #start score of computer
score_us = 0 #start score of user

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height)) #Create a game window with specified width and height
pygame.display.set_caption("SET Game") #Sets the window title

# Card attributes. The cards have a color, a symbol, a shade, and a number.
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']

# Generate all possible cards. Each card has its own combination of the attributes that are above.
list_of_81_cards_computer = [f"{col}{sym}{shad}{num}" 
                    for col in color
                    for sym in symbol
                    for shad in shading
                    for num in number]


# There are 81 cards. We want to have a list of these numbers, from 0 to 80, in a random order.
list_of_81_random_numbers = random.sample(range(0, 81), 81)

# The first 12 numbers of the list above are chosen, these are thus random and therefore not in order.
list_12_random_numbers = list_of_81_random_numbers[:12]

# Load card images into a dictionary
card_images = {name: pygame.image.load(f'kaarten/{name}.gif') for name in list_of_81_cards_computer}

# Generate all possible combinations of card attributes, resulting in 81 cards
list_of_81_cards = [[col, sym, shad, num] for col in color for sym in symbol for shad in shading for num in number] 

# Fonts, with the font sizes from above.
font = pygame.font.Font(None, font_size_1)
font1 = pygame.font.Font(None, font_size_2)
font2 = pygame.font.Font(None, font_size_3)

# Timer, this records the initial time when the game starts.
start_ticks = pygame.time.get_ticks()


class SET: 
    # The first function is about the characteristics of the cards. The name of the card contains all the characteristics (color, symbol, shade, and number).
    # The first word is the colour, the second word is the symbol, the third word is the shade, and the fourth word is the number.
    def __init__(self, cardlist): 
        self.color = cardlist[0]     
        self.symbol = cardlist[1]
        self.shading = cardlist[2]
        self.number = cardlist[3]

    # The second function is about the comparison of the cards.
    def compare(self, other1, other2):
        def compare_color(self, other1, other2): # First, compare the colours.
            return (self.color == other1.color == other2.color) or (self.color != other1.color != other2.color != self.color)

        def compare_symbol(self, other1, other2): # Secondly, compare the symbols.
            return (self.symbol == other1.symbol == other2.symbol) or (self.symbol != other1.symbol != other2.symbol != self.symbol)

        def compare_number(self, other1, other2): # Thirdly, compare the numbers.
            return (self.number == other1.number == other2.number) or (self.number != other1.number != other2.number != self.number)

        def compare_shading(self, other1, other2): # Fourthly, compare the shadings.
            return (self.shading == other1.shading == other2.shading) or (self.shading != other1.shading != other2.shading != self.shading)

        # It should return what comparisons there are between the cards.
        return (compare_color(self, other1, other2) and
                compare_symbol(self, other1, other2) and
                compare_number(self, other1, other2) and
                compare_shading(self, other1, other2))

    # The third function is about the characterstics of the cards again. This time, the colours, symbols, and shadings, and numbers are defind of three cards.
    def give_values(self, other1, other2):
        return ([self.color, self.symbol, self.shading, self.number],
                [other1.color, other1.symbol, other1.shading, other1.number],
                [other2.color, other2.symbol, other2.shading, other2.number])


# The function below is to find all the possible SETs in the 12 cards that are displayed.
def find_all_sets(cards):
    combs = list(combinations(range(12), 3)) # All possible combinations, so (1, 2, 3), (1, 2, 4), etc.
    valid_sets = []
    for combi in combs:
        card1, card2, card3 = cards[combi[0]], cards[combi[1]], cards[combi[2]] 
        if card1.compare(card2, card3): # The function in line 71 is used to see whether the cards form a correct SET.
            valid_sets.append([combi[0] + 1, combi[1] + 1, combi[2] + 1])
    return valid_sets

# The function below displays instructions on the screen
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
        
#The function below displays the remaining time on the screen
def draw_timer(): 
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000 #Calculates the elapsed time in seconds
    remaining_seconds = max(timeout - elapsed_seconds, 0) #Calculates the remaining time, ensuring it does not go below zero
    timer_text = font.render(f"Time left: {remaining_seconds} seconds", True, (0, 0, 0)) #Renders the timer text
    screen.blit(timer_text, (screen_width - 250, 20)) #Draws the timer text on the screen at the specified position
    return remaining_seconds > 0 #Returns True if there is time left, False otherwise

#The function below draws the cards on the screen
def draw_cards(card_indices): 
    for i, card_index in enumerate(card_indices): #Iterates through each card index
        card = list_of_81_cards[card_index] #Retrieves the card attributes
        card_name = ''.join(card) #Concatenates card attributes to form the card name
        card_image = card_images[card_name] #Retrieves the card image
        x = (i % 6) * (card_width + card_gap) + 50 #Calculates the position to draw the card
        y = (i // 6) * (card_height + card_gap + 60) + 160 #Calculates the position to draw the card
        screen.blit(card_image, (x, y)) #Draws the card image on the screen
        number_text = font.render(str(i + 1), True, (0, 0, 0)) #Renders the card number
        screen.blit(number_text, (x + 45, y + 170)) #Draws the card number above the card

# The function below checks whether there are typo's in the input of the user.
def check_format(input_string):
    try:
        numbers = input_string.strip().split(',')
        if len(numbers) != 3:
            return False
        for number in numbers:
            if not number.strip().isdigit():
                return False
        return True
    except ValueError:
        return False

 # The function below captures user input from the keyboard
def get_user_input():
    user_input = "" #Stores the user's input string
    input_active = True #Controls the input loop
    blink = True # Cursor visibility
    timer_of_the_cursor = pygame.time.get_ticks() # Timer for cursor blinking

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
        if pygame.time.get_ticks() - timer_of_the_cursor > 450: # Toggle cursor every 450ms. This part is to implement a blink cursor.
            blink = not blink
            timer_of_the_cursor = pygame.time.get_ticks()

        screen.fill(background_color) #Clears the screen
        draw_cards(list_12_random_numbers) #Redraws the cards, instructions, and timer
        draw_instructions()
        if not draw_timer():
            return "", "timeout"
        
        pygame.draw.rect(screen, input_box_color, pygame.Rect(160, 640, 100, 30)) #Draws the input box
        comment = font2.render("What SET did you find?", True, (0,0,0))
        screen.blit(comment, (25, 650))
        input_text = font.render(user_input, True, "white") #Renders the input text
        screen.blit(input_text, (170, 648)) #Draws the input text
        if blink:
            cursor_x = 170 + input_text.get_width() + 2
            pygame.draw.line(screen, "white", (cursor_x, 648), (cursor_x, 668), 2)
        pygame.display.flip()
    
    
    if not check_format(user_input):
        return "Oops! Wrong format. Please enter the numbers in the correct format.", "format_error"

    return user_input.split(','), "valid"

# The function below is to display the score of the computer.
def draw_score_computer(score_computer):
    text = font.render(f"Score Computer: {score_computer}", True, (0,0,0))
    screen.blit(text, (screen_width - 250, 40))
    pygame.display.flip()

# The function below is to display the score of the user.
def draw_score_user(score_user):
    text = font.render(f"Score user: {score_user}", True, (0,0,0))
    screen.blit(text, (screen_width - 250, 60))
    pygame.display.flip()

# Main game loop
while len(list_of_81_random_numbers) > 11: # As long as the list of the 81 cards is bigger than 11, so there are 12 cards on the table, the game should run.
    list_12_random_numbers = list_of_81_random_numbers[:12]
    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers] # These are the cards that are displayed. They have a random index from the first 12 numbers of the list of 81 numbers in random order.
    valid_sets = find_all_sets(cards) # The valid sets are found.

    screen.fill(background_color) # The screen is filled with the background color that is discussed at the top.
    draw_cards(list_12_random_numbers) # The cards are displayed on the screen.
    draw_instructions() # The instructions are displayed on the screen.
    pygame.display.flip()
    user_input, status = get_user_input() 

    if status == "format_error":
        text = font1.render(user_input, True, (0,0,0))
        screen.blit(text, (150, 370))
        pygame.display.flip()
        pygame.time.wait(2000)
        continue
   
    if user_input and user_input[0]:
        user_input = list(map(int, user_input))
        if sorted(user_input) in valid_sets: # If the input from the user is a correct SET
            text = font1.render("Good Job!", True, (0,0,0)) # It should display "Good Job!"
            screen.blit(text, (150, 370))
            score_us += 1 # The user gets a point.
            cumulative_score = score_us - score_comp # Calculating the difference in score, are you better then the computer?
            if cumulative_score in range(-20,-1): # If the score of the user is below the score of the computer, you get 40 seconds instead of 30 seconds.
                timeout = 40
            if cumulative_score in range(2,5): # If the score of the user is above the score of the computer (with more than 2 or less than 5), you get 25 seconds to find a SET.
                timeout = 25
                if cumulative_score == 2: # If you have more than 2 points more than the computer, you go a level up. 
                    text = font1.render("Level 2: time is now 25 seconds!", True, (0,0,0))
                    screen.blit(text, (300, 640))
            if cumulative_score in range(5,8): # If the score of the user is more than 5 points, and less than 8 points more than the computer, you have only 20 seconds to find a SET.
                timeout = 20
                if cumulative_score == 5: # If you have 5 points more than the computer, you go a level up.
                    text = font1.render("Level 3: time is now 20 seconds!", True, (0,0,0))
                    screen.blit(text, (300, 640))
            if cumulative_score >= 8: # When you have more than 8 points more than the computer, you only have 15 seconds to find a SET. 
                timeout = 15 
                if cumulative_score == 8: # If you have 8 points more than the computer, you go to the final level.
                    text = font1.render("Final level: time is now 15 seconds!", True, (0,0,0))
                    screen.blit(text, (300, 640))
            else: 
                timeout = 30
            draw_score_user(score_us)       # show score of user
            draw_score_computer(score_comp) # show score of computer
            pygame.display.flip()
            pygame.time.wait(2000) # it should wait, since otherwise the game would immediately continue and the message is shown for a very short time. 
            for index in sorted(user_input, reverse=True):
                del list_of_81_random_numbers[index - 1] #Removes the cards forming the SET from the list
            start_ticks = pygame.time.get_ticks() #Resets the timer
        else: # If the input from the user is an incorrect SEt
            text = font1.render("Unfortunately not.", True, (0,0,0)) # It should display "Unfortunately not."
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(2000)
    else: # If the user did not find a SET, the computer will try.
        text = font1.render("Time out! The computer will have a try.", True, (0,0,0))
        screen.blit(text, (150, 370))
        pygame.display.flip()
        pygame.time.wait(1000)
        if valid_sets: # If there are SETs in the 12 cards on the table, it should say what SET the computer found.
            pygame.display.flip()
            pygame.time.wait(1000)
            answer_computer = valid_sets[0]
            text = font1.render(f"Computer found a set: {answer_computer[0], answer_computer[1], answer_computer[2]}", True, (0,0,0))
            screen.blit(text, (300, 640))
            score_comp += 1 # The computer gets a point.
            cumulative_score = score_us - score_comp
            # The part below is already discussed in the part where the user is correct. This is the same as before.
            if cumulative_score in range(-20,-1): 
                timeout = 40
                if cumulative_score == -2:
                    text = font1.render("Level down: time is now 40 seconds!", True, (0,0,0))
                    screen.blit(text, (300, 400))
            if cumulative_score in range(2,5):
                timeout = 25
            if cumulative_score in range(5,8):
                timeout = 20
            if cumulative_score >= 8:
                timeout = 15
            draw_score_computer(score_comp)
            draw_score_user(score_us)
            
            pygame.display.flip()
            pygame.time.wait(2000)
            for index in sorted(answer_computer, reverse=True): # It should delete the cards which form a SET.
                del list_of_81_random_numbers[index - 1]
        else: #If there are no SETs in the 12 cards on the table
            text = font1.render("No SET found among these cards.", True, (0,0,0))
            screen.blit(text, (300, 640))
            cumulative_score = score_us - score_comp
            # The part below is already discussed in the part where the user is correct. This is the same as before.
            if cumulative_score in range(-20,-1): 
                timeout = 40
            if cumulative_score in range(2,5):
                timeout = 25
            if cumulative_score in range(5,8):
                timeout = 20
            if cumulative_score >= 8:
                timeout = 15
            draw_score_computer(score_comp)
            draw_score_user(score_us)
            pygame.display.flip()
            pygame.time.wait(1000)
            del list_of_81_random_numbers[9:12] #Removes the last three cards if no valid SETs are found.
        start_ticks = pygame.time.get_ticks()

    # The part below does not work unfortunately, but we tried the following to have the word Finished! displayed when the game is over.
    if len(list_of_81_random_numbers) < 12 and len(valid_sets) == 0:
            text = font1.render("FINISHED!", True, (0,0,0)) 
            screen.blit(text, (150, 370))
            pygame.display.flip()
            pygame.time.wait(5000)
            break

            
pygame.quit()

