import re

def contains_gold(color):
  #set initial state of gold available to false
  gold = False
  #input should be a dict containing the root node and a list of children
  for (k,v) in color.items(): 
    print("searching in ", k)
    # first recursion escape is if it finds shine gold bags
    if "3 shiny gold bags" in v:
      gold = True
    # second recursion escape is if we're at the bottom of a tree and no more bags can be contained
    elif "no other bags" in v:
      gold = False
      print("No bags can be found in " ,k)
    else:
      # log the colors that can be found in the next level
      print(k, "can contain ", v)   
      # loop through each color at this level
      for bag in v:
        # remove the number from the bags because we'll be searching the list of dicts for the corresponding root color
        bag = re.sub('[0-9]','',bag).strip()
        # loop through the master list, seperate the root, and see if our current color matches it
        for item in dict_rules:
          for key, value in item.items():
            #print(key)
            if key == bag:
              #run the search again at this new level. This will continue until we find gold, or we find no bags, in which case
              # it should go up a level and move to the next color to search. 
              contains_gold(item)                        
  return gold

# open input file, make it a list of lines
with open('7-input.txt') as f:
  rules  = f.readlines()

dict_rules = []

for r in rules:
  root_split = r.split("contain") ## get the root color by splitting off of contain  
  root = root_split[0].strip() ## remove whitespace
  # After that, we will make a dict that contains the root as the key and the list of possible colors as the value
  # Do this by splitting everything after the first root_split by "," and removing the period
  for n in root_split[1:]:
    children = n.replace(".","").split(",")

  # make the dict from the root and the colors list
  rule = {root:children}
  #append to full list
  dict_rules.append(rule)


win_colors = []
is_gold = 0
for d in dict_rules:
  if contains_gold(d):
    win_colors.append(d)
    is_gold +=1

print(is_gold, win_colors)
  # if "pale fuchsia bags" in d:
  #   print(d)



  
