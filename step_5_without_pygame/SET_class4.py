from itertools import combinations
import random

#Define card attribute
color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
shading = ['filled', 'shaded', 'emply']
number = ['1', '2', '3']

#Generate all possible cards
list_of_81_cards = [[a, b, c, d] 
                for a in color
                for b in symbol
                for c in shading
                for d in number] 

#Define SET class
class SET: 
    # Bulletpoint 1 en 2
    # Define what color, symbol, number, and shading it is.
    def __init__(self, cardlist): 
        self.color = cardlist[0]     
        self.symbol = cardlist[1]
        self.shading = cardlist[2]
        self.number = cardlist[3]

    #Compare three cards with each other.
    def compare(self, other1, other2):
        lijst = [] # We have an empty list, where we add True and False
        def compare_color(self, other1, other2): # We are going to compare the colors of the cards
            if self.color == other1.color and self.color == other2.color: # If they all have the same color, the list should append True
                return True
            if self.color != other1.color and self.color != other2.color and other1.color != other2.color: # If they are all different colors, the list should append True
                return True
            else: # If the colors are not all different or the same, the list should append False
                return False  

    
        def compare_symbol(self,other1, other2): # We are going to compare the symbols of the cards
            if self.symbol == other1.symbol and self.symbol == other2.symbol: # If they all have the same symbol, the list should append True
                return True
            if self.symbol != other1.symbol and self.symbol != other2.symbol and other1.symbol != other2.symbol: # If they all have different symbols, the list should append True
                return True
            else: # If the symbols are not all different or the same, the list should append False
                return False
        
        def compare_number(self, other1, other2): # We are going to compare the numbers of the cards
            if self.number == other1.number and self.number == other2.number: # If they all have the same number, the list should append True
                return True
            if self.number != other1.number and self.number != other2.number and other1.number != other2.number: # If they all have different numbers, the list should append False
                return True
            else: # If the numbers are not all different or the same, the list should append False
                return False
        
        def compare_shading(self, other1, other2): # We are going to compare the shade of the cards
            if self.shading == other1.shading and self.shading == other2.shading: # If they all have the same shade, the list should append True
                return True
            if self.shading != other1.shading and self.shading != other2.shading and other1.shading != other2.shading: # If they all have different shades, the list should append False
                return True
            else: # If the shades are not all different or the same, the list should append False
                return False

        if compare_color(self, other1, other2) == False or compare_symbol(self, other1, other2) == False or compare_number(self, other1, other2) == False or compare_shading(self, other1, other2) == False: # If there is False in the list, thus one or more comparisons give False, then it is not a SET.
            return False
        else: # If there is no False in the list, thus only True, all comparisons give True, thus it is a SET, return True.
            return True
    def give_values(self, other1, other2): #for visuals/tests, that we can see what sets are actually true
            return ([self.color, self.symbol, self.shading, self.number],
                    [other1.color, other1.symbol, other1.shading, other1.number],
                    [other2.color, other2.symbol, other2.shading, other2.number])

#Select 12 random cards
list_12_random_numbers = random.sample(range(0, 81), 12) 

print(list_12_random_numbers) # not essential

#12 random cards
kaart1 = SET(list_of_81_cards[list_12_random_numbers[0]])
kaart2 = SET(list_of_81_cards[list_12_random_numbers[1]])
kaart3 = SET(list_of_81_cards[list_12_random_numbers[2]])
kaart4 = SET(list_of_81_cards[list_12_random_numbers[3]])
kaart5 = SET(list_of_81_cards[list_12_random_numbers[4]])
kaart6 = SET(list_of_81_cards[list_12_random_numbers[5]])
kaart7 = SET(list_of_81_cards[list_12_random_numbers[6]])
kaart8 = SET(list_of_81_cards[list_12_random_numbers[7]])
kaart9 = SET(list_of_81_cards[list_12_random_numbers[8]])
kaart10 = SET(list_of_81_cards[list_12_random_numbers[9]])
kaart11 = SET(list_of_81_cards[list_12_random_numbers[10]])
kaart12 = SET(list_of_81_cards[list_12_random_numbers[11]])

#all possible combinations
combination = combinations([kaart1, kaart2, kaart3, kaart4, kaart5, kaart6, kaart7, kaart8, kaart9, kaart10, kaart11, kaart12], 3)
for index in list(combination):
    True_or_False = (index[0].compare(index[1], index[2])) #if a random combination is true or false
    Three_tested_cards = (index[0].give_values(index[1], index[2])) #the corresponding cards that belong to true or false
    if True_or_False == True:
        print (True_or_False, Three_tested_cards)
