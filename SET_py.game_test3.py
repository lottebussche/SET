from itertools import combinations
import random
import threading

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

   

while len(list_of_81_random_numbers) > 11:
    list_12_random_numbers = list_of_81_random_numbers[:12]
    cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]
    print("The 12 cards: ",list_12_random_numbers)
    valid_sets = find_all_sets(cards)

    if valid_sets:
        answer_computer = valid_sets[0] #This is the same as finding 1 set only!
    else:
        answer_computer = "No SET found among the selected cards."
    
    user_found_set = False
    print("The computer answer: ",answer_computer)

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
                print("Computer found:", answer_computer)
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