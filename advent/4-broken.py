required_items = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

with open('4-input.txt', 'r') as f:
  myList = f.readlines()
print(myList)
  #print(i)
  # This is how we're getting all entries into their own list, by splitting the lines by 2 newlines.
  #newstr = ''.join(i).rstrip()
  #print(newstr)
list = (myList.rstrip().split("\n"))
#print(str(f))
count = 0
for l in list:
  item = l.replace("\n"," ").replace(":", " ").split(" ")
  
  valid = True
  for req_item in required_items:
    if req_item not in item:
      valid = False
  if valid:
    # Nested if to check validation
    count += 1
  print(str(item), valid )
print(count)

