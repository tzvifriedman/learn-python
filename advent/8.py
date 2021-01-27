with open('8-input.txt') as f:
  ins = [x.rstrip().split(" ") for x in f.readlines()]


  
used_numbers = []
number = 0 
def do_it(start):
  global number
  global used_numbers
  if start in used_numbers:
    infinte = True
    return infinte
  if start not in used_numbers:
    infinte = False
    used_numbers.append(start)
    match = [(i, x) for i, x in enumerate(ins) if i == start]
    #print(match)
    if match[0][1][0] == 'acc':
      number += int(match[0][1][1])
      #print(number)
      if len(ins) < start + 1:
        return False
      return do_it(start + 1)
    elif match[0][1][0] == 'jmp':
      #print(number)
      new_line = match[0][0] + int(match[0][1][1])
      if len(ins) <= start + 1:
        return False
      else:
        return do_it(new_line)
    elif match[0][1][0] == 'nop':
      if len(ins) <= start + 1:
        return False
      else:
        return do_it(start+1)
  #print(number)


# do_it(0)
for i, x in enumerate(ins):
  used_numbers = []
  number = 0 
  if 'jmp' in x:
    x[0] = "nop"
    if do_it(0) == False:
      print(number)
      break
    #print(number)
    x[0] = "jmp" 
  elif 'nop' in x:
    x[0] = "jmp"
    if do_it(0) == False:
      print(number)
      break
    #print(number)
    x[0] = "nop" 
#rint(do_it(619),number)

# list = [a,b,c,d,e]

# for i, l in enumerate(list):
#   cur_item = i