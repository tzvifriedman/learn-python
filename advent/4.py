required_items = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

f = open('4-input.txt', mode='r',newline="\r\n")
for i in f:
  list = (i.rstrip().split("\n\n"))
count = 0
for l in list:
  item = l.replace("\n"," ").replace(":", " ").split(" ")
  
  valid = True
  for req_item in required_items:
    if req_item not in item: 
  # if all(elem in required_items for elem in list):
      valid = False
  if valid:
    count += 1
  print(str(item), valid )
print(count)

