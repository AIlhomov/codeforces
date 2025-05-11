borze = input() 

counter = 0

while counter < len(borze):
    
    if borze[counter] == '.':
        print(0, end='')
        counter += 1
    elif borze[counter] == '-':
        #check next one
        if borze[counter+1] == '.':
            print(1, end='')
        else:
            print(2, end='')
        counter += 2
           