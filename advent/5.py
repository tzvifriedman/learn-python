import math

with open('5-input.txt', 'r') as f:
  lines = [line.rstrip() for line in f]



def find_seat(seats, rows ,input):


  # first case
  frow = 1
  lrow = rows
  fseat = 1
  lseat = seats

  for i in input[0:6]:
    if i == 'B':
      frow = frow + math.ceil((lrow - frow) / 2) 

      print(i, frow,lrow)
    elif i == 'F': 
      lrow = frow + math.floor((lrow - frow) / 2) 

      print(i, frow,lrow)
  
  if input[6] == 'F':
    row = frow - 1
  elif input[6] == 'B':
    row = lrow - 1
  print(input[6],row)
    
  for i in input[7:9]:
    print(i)
    if i == 'R':
      fseat = fseat + math.ceil((lseat - fseat) / 2) 
      #print(i, fseat,lseat)
    elif i == 'L':
      lseat = fseat + math.floor((lseat - fseat) / 2) 
      #print(i, fseat,lseat)
    print(i, fseat,lseat)

  for i in input[9]:
    if i == 'L':
      seat = fseat - 1 
    elif i == 'R':
      seat = lseat - 1
    print(i, seat)

  value = (row * 8) + seat

  print(value)

  return value


values = []
for l in lines:
  values.append(int(find_seat(8, 128,l)))


sorted = sorted(values)
print(sorted)

index = 0

for seat in sorted:
  
  empty = False
  cur_val = sorted[index]
  if cur_val + 1 == sorted[index+1]:
    empty = False 
  else: 
    empty = True
  index += 1
  print (seat, cur_val, empty)