import csv 

def add_numbers(input, num_array):
    for i in num_array:
        for x in num_array:
                if int(i) + int(x) + int(input) == 2020:
                    print(input, x, i)
                    print (int(input) * int(i) * int(x))



with open('1-input.txt', 'r') as f:
    ints = f.readlines() 
    cleanints = []
    for i in ints:
        cleanints.append(i.strip())
    print(cleanints)

for a in cleanints:
    add_numbers(a, cleanints)
    
