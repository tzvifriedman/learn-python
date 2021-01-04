import csv

def make_letter_count(password):
  counts = {}
  for c in password:
    counts[c] = counts.get(c,0) + 1
  return counts


def check_policy_2(input):
  p1 = int(input[0].split("-")[0])
  p2 = int(input[0].split("-")[1])
  letter = input[1].strip(":")
  string = input[2]
  print(p1,p2,letter,string)
  if bool(string[p1 - 1] == letter) ^ bool(string[p2-1] == letter):
    is_valid = True
  else:
    is_valid = False
  return is_valid 


def check_policy(input):
  letter_count = make_letter_count(input[2])
  measured_letter = input[1].strip(":")
  lower = input[0].split("-")[0]
  upper = input[0].split("-")[1]
  if measured_letter in letter_count:
    measured_count = letter_count[measured_letter]
  else:
    measured_count = 0
  
  if int(lower) <= int(measured_count) <= int(upper):
    is_valid = True
  else:
    is_valid = False
  print(measured_letter, lower, upper, measured_count)
  return is_valid
  
with open('2-input.txt', 'r') as f:
  lines = [line.rstrip().split(" ") for line in f]

valid = 0
for l in lines:
  if check_policy_2(l):
    valid += 1
print(valid)
