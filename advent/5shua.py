

#create and read file
with open(r'day5-input.txt') as file:
    x = file.readlines()
    #print(x)
    
# Loop through each line, removing '/n'        
    for string in x:
        string.strip('\n')
        print(string)
        
        #Within the loop, set variables and create numbered list.
        numbers = []
        column = []
        for y in range(0, 128):
            numbers.append(y)
        for z in range(0,8):
          column.append(z)
            
        #Check each letter, dvide the list.   
        for letter in string:
            print(letter)
            if letter == 'F':
                numbers = numbers[:int(len(numbers)/2)]
                print(numbers)
            elif letter == 'B':
                numbers = numbers[-int(len(numbers)/2):]
                print(numbers)
            elif letter == 'L':
                column = column[:int(len(column)/2)]
                print(column)
            elif letter == 'R':
                column = column[-int(len(column)/2):]
                print(column)