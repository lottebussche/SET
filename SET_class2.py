color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
number = ['1', '2', '3']
shading = ['filled', 'shaded', 'emply']

class SET: 
    # Bulletpoint 1 en 2
    # First we are going to define what color, symbol, number, and shading it is.
    def __init__(self, color,symbol,number,shading): 
        self.color = color   
        self.symbol = symbol
        self.number = number
        self.shading = shading

    # Now we are going to compare three cards with each other.
    def compare(self, other1, other2):
        def compare_color(self, other1, other2): # We are going to compare the colors of the cards
            if self.color == other1.color and self.color == other2.color: # If they all have the same color, the list should append True
                return True
            if self.color != other1.color and self.color != other2.color and other1.color != other2.color: # If they are all different colors, the list should append True
                return True
            else: # If the colors are not all different or the same, the list should append False
                return False  
        def compare_symbol(self, other1, other2): # We are going to compare the symbols of the cards
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

kaart1 = SET('purple', 'oval', 'filled', '1')
kaart2 = SET('purple', 'oval', 'shaded', '2')
kaart3 = SET('red' ,'oval', 'shaded', '3')
print(kaart1.compare(kaart2, kaart3))



        
