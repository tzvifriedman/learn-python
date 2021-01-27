import string

with open('6-input.txt') as f:
  lines = f.read()

lines = lines.split('\n\n')
groups = []
for l in lines:
  groups.append(l.split("\n"))

letter_list = list(string.ascii_lowercase)
letter_dict = {}


# 6a
# print(letter_dict)
# total = 0 
# for g in groups:
#   count = 0
#   g = ''.join(g)
#   print(g)
#   for l in letter_list:
#     letter_dict[l] = "False"
#   for letter in letter_dict:
#     if letter in g:
#       letter_dict[letter] = "True"
#   for l in letter_dict:
#     print(l, letter_dict[l])
#   for (key, value) in letter_dict.items():
#     if value == "True":
#       count +=1
#   print(count)    
#   total += count
# print(total)

#6b
print(letter_dict)
total = 0 
for g in groups:
  count = 0
  print(g)
  for l in letter_list:
    letter_dict[l] = "False"
  for letter in letter_dict:
    if (all(letter in elem for elem in g)):
      letter_dict[letter] = "True"
  for l in letter_dict:
    print(l, letter_dict[l])
  for (key, value) in letter_dict.items():
    if value == "True":
      count +=1
      
  print(count)    
  total += count
print(total)