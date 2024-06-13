from itertools import combinations
import random
import pygame
import time
import os
import threading


#pygame.display.set_mode()

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

list_of_81_random_numbers = random.sample(range(0, 81), 81)
print(list_of_81_random_numbers)


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

while len(list_of_81_random_numbers) > 11: 
    print(list_of_81_random_numbers)
    #cards_on_table():
            # Generate 12 random card indices
    list_12_random_numbers = list_of_81_random_numbers[:12] #the first 12 numbers of our selected 81 cards
    print(list_12_random_numbers)
    list_3_random_numbers = random.sample(range(0,81), 3)
            #print("Random card indices:", list_12_random_numbers)

    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]

    # Create 12 SET objects
    for number in list_3_random_numbers:
        for numbers in list_12_random_numbers:
            if number != numbers:
                extra_cards = (list_of_81_cards[number])

    list_of_cards = []
    # Print the 12 selected cards
    #print("Selected cards:")
    for i in range(12):
        card = list_of_81_cards[list_12_random_numbers[i]]
        filename_card = (list_of_81_cards[list_12_random_numbers[i]][0] + list_of_81_cards[list_12_random_numbers[i]][1] + list_of_81_cards[list_12_random_numbers[i]][2] + list_of_81_cards[list_12_random_numbers[i]][3])
        list_of_cards.append(filename_card)
        #print(f"Card {i+1}: {filename_card} (index {list_12_random_numbers[i]})")


    # Check all combinations for valid sets
    # This below checks all SETS that are possible with 12 random cards. When it is possible, we add it to the list called list_of_all_SET.

    list_of_all_SET = []
    combination = combinations(range(0, 12), 3)  
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
            answer_computer = (f"SET found with card numbers: {combi[0] + 1}, {combi[1] + 1}, {combi[2] + 1}")
            list_answer_computer = list(answer_computer)
            set_found = True
            break

    if not set_found:
        answer_computer = "No SET found among the selected cards."

    # kan nog weg
    print (answer_computer)
    # I suppose we should do here something with that we delete 3 cards, and add 3 cards. And not No SET ...
    list_of_extra_cards = []
    for i in range(3):
        extra_card = list_of_81_cards[list_3_random_numbers[i]]
        filename_extra_card = (list_of_81_cards[list_3_random_numbers[i]][0] + list_of_81_cards[list_3_random_numbers[i]][1] + list_of_81_cards[list_3_random_numbers[i]][2] + list_of_81_cards[list_3_random_numbers[i]][3])
        list_of_extra_cards.append(filename_extra_card)

    # We take the input of the user, this is a list like '1, 3, 6', as mentioned in the assignment.
    def get_user_input():
        global input_of_user
        input_of_user = input("What SET did you find? ") 
        input_of_user = input_of_user.split(', ')
        for index in range(3):
            input_of_user[index] = int(input_of_user[index])

    # We use a timeout as we play the game on time
    def get_input_with_timeout(timeout):
        global input_of_user
        input_of_user = None
        input_goal = threading.Thread(target=get_user_input)
        input_goal.start()
        input_goal.join(timeout=timeout)  

        if input_goal.is_alive():
            print ("Time is up.", answer_computer)
            input_goal.join()  
            return None
            
        return input_of_user

    #Timeout is how many seconds we want to give to the player to find a set
    timeout = 10
    result = get_input_with_timeout(timeout)

    if result is not None:
        print(f"Input is: {result}")


    # Now we look whether the input of the user is a valid SET. We do this by checking whether it is in the list we just created.
    if input_of_user in list_of_all_SET:
        print("Good Job!")
        print(list_of_cards[input_of_user[0] - 1])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[input_of_user[0] - 1])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[input_of_user[1] - 2])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[input_of_user[2] - 3])
        print(list_of_81_random_numbers)


    # If the computer has not found a SET either, then list_of_cards.remove(list_of_cards[0])
        #list_of_cards.remove(list_of_cards[1])
        #list_of_cards.remove(list_of_cards[2])
        #list_of_cards.append(list_of_extra_cards[0]])
        #list_of_cards.append(list_of_extra_cards[1])
        #list_of_cards.append(list_of_extra_cards[2])
    else:
        print("Unfortunately not, the computer will try.")
        print(answer_computer)
        print(list_of_cards[input_of_user[0] - 1])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[list_answer_computer[0] - 1])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[list_answer_computer[1] - 2])
        list_of_81_random_numbers.remove(list_of_81_random_numbers[list_answer_computer[2] - 3])
        print(list_of_81_random_numbers)

    # Remove SET 
    def remove_cards():
        for input_of_user in list_of_all_SET:
            list_of_81_cards.remove(input_of_user) and list_12_random_numbers.remove(input_of_user)
        else: list_of_81_cards.remove(answer_computer) and list_12_random_numbers.remove(answer_computer)



    # Add new cards
    def add_new_cards():
        try: 
            list_12_random_numbers = random.sample(range(0, 81), 12)
        except: print("no cards left")