import pygame
import sys
import random
from itertools import combinations
import threading

#Start up pygme
pygame.init()

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

#Finds all valid SETs among 12 cards
def find_all_sets(cards):
    combs = list(combinations(range(12), 3))  
    valid_sets = []
    for combi in combs:
        card1, card2, card3 = cards[combi[0]], cards[combi[1]], cards[combi[2]]
        if card1.compare(card2, card3):
            valid_sets.append([combi[0] + 1, combi[1] + 1, combi[2] + 1])
    print("The valid sets: ",valid_sets)
    return valid_sets

# Determine the screen 
screen = pygame.display.set_mode((600, 650))
clock = pygame.time.Clock()
pygame.display.set_caption("SET: Malou ter Horst, Lotte Bussche, Laura Mercenier, Julia van Oostrom")
font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(450, 80, 170, 32) #(left, top, width, height)
#submit_box = pygame.Rect(450, 120, 170, 32)     #a button that you can click to submit your answers
#button_text = font.render('submit', True, 'black', 'green')
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive       #to know if the input rectangle has been clicked
active = False

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

# Determine positions to display some cards
display_cards = []
for j in range(0,12):
    display_cards.append(list_of_81_cards_computer[list_12_random_numbers[j]])

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



#Takes input from the user
def get_user_input(input_of_user):
    result = input("What SET did you find? ").split(', ')
    input_of_user.extend(result)
#Sets a timeout for input collection.
def get_input_with_timeout(timeout):
    input_of_user = []
    input_thread = threading.Thread(target=get_user_input, args=(input_of_user,))
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        return None
    else:
        return input_of_user

# Game loop, neccesery to end the game
running = True
while running:
    screen.fill(('beige'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
                if len(user_text) == 7:
                    input_user = user_text
                    print(input_user)
                    get_user_input(input_user)
    
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen, color, input_rect)
    text_surface = font.render(user_text, True, (255, 255, 225))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    

    # Image the cards
    for i, card_name in enumerate(display_cards):
        card_image = card_images[card_name]
        screen.blit(card_image, card_positions[i])
    
    # Keep the screen and pygame updated 
    pygame.display.flip()


#the following is all code from our previous codes

while len(list_of_81_random_numbers) > 11:
    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]
    print("The 12 cards: ",list_12_random_numbers)
    valid_sets = find_all_sets(cards)

    if valid_sets:
        answer_computer = valid_sets[0] #This is the same as finding 1 set only!
        answer1 = answer_computer[0]
        answer2 = answer_computer[1]
        answer3 = answer_computer[2]
    else:
        answer_computer = "No SET found among the selected cards."
    
    user_found_set = False
    if answer_computer != "No SET found among the selected cards.":
        print("The computer answer: " + f"{answer1}" + ", " + f"{answer2}" + ", " f"{answer3}")
    else: 
        print(answer_computer)

    user_input = get_input_with_timeout(30)

    if user_input:
        user_input = list(map(int, user_input))
        if sorted(user_input) in valid_sets:
            print("Good Job!")
            user_found_set = True
            for index in sorted(user_input, reverse=True):
                del list_of_81_random_numbers[index - 1]  
        else:
            print("Unfortunately not, the computer will try.")
            if answer_computer == "No SET found among the selected cards.":
                print(answer_computer)
                del list_of_81_random_numbers[9:11]
                print(list_of_81_random_numbers)
        
            else:
                print("The computer found: " + f"{answer1}" + ", " + f"{answer2}" + ", " f"{answer3}")
                for index in sorted(answer_computer, reverse=True):
                    del list_of_81_random_numbers[index - 1]
                
    else:
        print("Timeout! The computer will try.")
        if answer_computer == "No SET found among the selected cards.":
                print(answer_computer)
                del list_of_81_random_numbers[9:11]

        
        else:
            print("Computer found:", answer_computer)
            for index in sorted(answer_computer, reverse=True):
                del list_of_81_random_numbers[index - 1]
                
    if not user_found_set and answer_computer == "No SET found among the selected cards.":
        print("No SET is possible with the current cards.")

    print("The cards that are left: ",list_of_81_random_numbers)



# Quit pygame
pygame.quit()
sys.exit()
