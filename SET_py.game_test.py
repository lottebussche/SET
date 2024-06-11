from itertools import combinations
import random
import pygame
import time
import os

# What we should do:
# So, the input should come from an user. The user says what SET he found.
# Then using find_all_sets <- maybe using this as a definition, check whether the input is a SET.
# If the input is a SET, ...
# If not, then ...



pygame.display.set_mode()

# Card attributes
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'empty']
number = ['1', '2', '3']

# Generate all possible cards
list_of_81_cards = [[col, sym, shad, num] 
                    for col in color
                    for sym in symbol
                    for shad in shading
                    for num in number]

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


# Generate 12 random card indices
list_12_random_numbers = random.sample(range(0, 81), 12)
#print("Random card indices:", list_12_random_numbers)

# Create 12 SET objects
cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]


# Print the 12 selected cards
#print("Selected cards:")
for i in range(12):
    card = list_of_81_cards[list_12_random_numbers[i]]
    filename_card = (list_of_81_cards[list_12_random_numbers[i]][0] + list_of_81_cards[list_12_random_numbers[i]][1] + list_of_81_cards[list_12_random_numbers[i]][2] + list_of_81_cards[list_12_random_numbers[i]][3])
    #print(f"Card {i+1}: {filename_card} (index {list_12_random_numbers[i]})")


# Check all combinations for valid sets
# This below checks all SETS that are possible with 12 random cards. When it is possible, we add it to the list called list_of_all_SET.
list_of_all_SET = []
combination = combinations(range(12), 3)  
for combi in combination:
    card1, card2, card3 = cards[combi[0]], cards[combi[1]], cards[combi[2]]
    if card1.compare(card2, card3):
        list_of_all_SET.append([combi[0] + 1, combi[1] + 1, combi[2] + 1])


# Check all combinations for the first valid set
combination = combinations(range(12), 3)  # Use indices directly
set_found = False
for combi in combination:
    card1, card2, card3 = cards[combi[0]], cards[combi[1]], cards[combi[2]]
    if card1.compare(card2, card3):
        print(f"SET found with card numbers: {combi[0] + 1}, {combi[1] + 1}, {combi[2] + 1}")
        set_found = True
        break

if not set_found:
    print("No SET found among the selected cards.")

# I suppose we should do here something with that we delete 3 cards, and add 3 cards. And not No SET ...


# We take the input of the user, this is a list like '1, 3, 6', as mentioned in the assignment.
input = input("What SET did you find? ").split(', ')
for index in range(3):
    input[index] = int(input[index])

# Now we look whether the input of the user is a valid SET. We do this by checking whether it is in the list we just created.
if input in list_of_all_SET:
    print("Good Job!")
else:
    print("Unfortunately not, try again!")







