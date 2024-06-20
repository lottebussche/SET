color = ['red', 'green', 'purple']
symbol = ['oval', 'squiggle', 'diamond']
number = ['1', '2', '3']
shading = ['filled', 'shaded', 'emply']

list_of_81_cards = [[a, b, c, d] 
                for a in color
                for b in symbol
                for c in shading
                for d in number]
print(list_of_81_cards)
