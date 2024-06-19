lijst = ['greenovalfilled1', 'purpleovalshaded2', 'redovalempty3'] #dit is volgens de regels een set

class SET: 
        def color(index): 
            if 'red' in lijst[index]: 
                return 'red' 
            if 'green' in lijst[index]: 
                return 'green' 
            if 'purple' in lijst[index]: 
                return 'purple'   

        def symbol(index): 

            if 'diamond' in lijst[index]: 
                return 'diamond' 
            if 'oval' in lijst[index]: 
                return 'oval' 
            if 'squiggle' in lijst[index]: 
                return 'squiggle' 
        

        def number(index): 

            if '1' in lijst[index]: 
                return '1' 
            if '2' in lijst[index]: 
                return '2' 
            if '3' in lijst[index]: 
                return '3' 
        
        def shading(index): 
            if 'filled' in lijst[index]: 
                return 'filled' 
            if 'empty' in lijst[index]: 
                return 'empty' 
            if 'shaded' in lijst[index]: 
                return 'shaded' 


def list_of_properties(index): 

        color = color(index) 

        symbol = symbol(index) 

        shading = shading(index) 

        number = number(index) 

        return [color, symbol, shading, number] 

    

    def compare(index): 

        list1 = list_of_properties(index) 

        list2 = list_of_properties(index) 

        list3 = list_of_properties(index) 

    

    for i in range(0, 4): 

        Lijst = [] 

        if list1[i] == list2[i] and list2[i] == list3[i]:  
            Lijst.append(True) 

        if list1[i] != list2[i] and list2[i] != list3[i]: 
            Lijst.append(True) 
        else: 
            Lijst.append(False) 

    

        if False in lijst:
            return False 
        else: 
            return True 
