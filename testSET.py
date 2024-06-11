from itertools import combinations
import random

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
print("Random card indices:", list_12_random_numbers)

# Create 12 SET objects
cards = [SET(list_of_81_cards[i]) for i in list_12_random_numbers]

# Print the 12 selected cards
print("Selected cards:")
for i in range(12):
    card = list_of_81_cards[list_12_random_numbers[i]]
    print(f"Card {i+1}: {card} (index {list_12_random_numbers[i]})")

# Check all combinations for valid sets
combination = combinations(range(12), 3)  # Use indices directly
for combo in combination:
    card1, card2, card3 = cards[combo[0]], cards[combo[1]], cards[combo[2]]
    if card1.compare(card2, card3):
        print(f"SET found with card numbers: {combo[0] + 1}, {combo[1] + 1}, {combo[2] + 1}")

