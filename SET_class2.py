color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
number = ['1', '2', '3']
shading = ['filled', 'shaded', 'emply']

class SET: 
    def __init__(self, color,symbol,number,shading): 
        self.color = color      
        self.symbol = symbol
        self.number = number
        self.shading = shading

    def compare(self, other1, other2):
        lijst = []
        def compare_color(self, other1, other2):
            if self.color == other1.color and self.color == other2.color:
                lijst.append(True)
            if self.color != other1.color and self.color != other2.color and other1.color != other2.color:
                lijst.append(True)
            else:
                lijst.append(False)
                
        def compare_symbol(self,other1, other2):
            if self.symbol = other1.symbol and self.symbol == other2.symbol:
                lijst.append(True)
            if self.symbol != other1.symbol and self.symbol != other2.symbol and other1.symbol != other2.symbol:
                lijst.append(True)
            else:
                lijst.append(False)

        def compare_number(self, other1, other2):
            if self.number == other1.number and self.number == other2.number:
                lijst.append(True)
            if self.number != other1.number and self.number != other2.number and other1.number != other2.number:
                lijst.append(True)
            else:
                lijst.append(False)

        def compare_shading(self, other1, other2):
            if self.shading == other1.shading and self.shading == other2.shading:
                lijst.append(True)
            if self.shading != other1.shading and self.shading != other2.shading and other1.shading != other2.shading:
                lijst.append(True)
            else:
                lijst.append(False)

        if False in lijst:
            return False
        else:
            return True

