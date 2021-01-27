import re

golds = 0
def contains_gold(color):
  #input should be a dict containing the root node and a list of children
  for (k,v) in color.items():
    # First, do some input sanitizing (should really have this in a new function)
    v = [re.sub('[0-9]','', value).strip() for value in v] 
    # change all 'bag' to 'bags' to keep consistent
    v = [re.sub('bag$','bags', value) for value in v]
    print("searching in ", k)

    # First recursion escape is to check if any immediate sub colors are shiny gold.
    # If it is, set gold to True and return to calling function
    if any("shiny gold bags" in cur_color for cur_color in v):
      gold = True
      return gold
    # If no golds are found, we need to recurse through the next layer of colors for each color
    else:
      for color in v:
        # loop through the master list of dicts and find the one that matches the color we need to search
        for item in dict_rules:
          for key, value in item.items():
            if key == color:
              #run the search again at this new level. This will continue until we find gold, in which case
              # it should go up a level and move to the next color to search. 
              if contains_gold(item):
                gold = True                       
                return gold



# open input file, make it a list of lines
with open('7-input.txt') as f:
  rules  = f.readlines()

#create the list of dicts
dict_rules = []

for r in rules:
  root_split = r.split("contain") ## get the root color by splitting off of contain  
  root = root_split[0].strip() ## remove whitespace
  # After that, we will make a dict that contains the root as the key and the list of possible colors as the value
  # Do this by splitting everything after the first root_split by "," and removing the period
  for n in root_split[1:]:
    children = n.replace(".","").split(", ")
    #print("spaceaz?" , children)

  # make the dict from the root and the colors list
  rule = {root:children}
  #append to full list
  dict_rules.append(rule)

## part 1
# for x, d in enumerate(dict_rules): # Using enumerate here so we can keep track if where we are in the list
#   # for each color in the list, run the search recursively until we find gold or we run out of nodes
#   if contains_gold(d):
#     # increment one per item where golds are found
#     golds += 1
#     print(x, golds)
#   else: 
#     print(x, golds)

## part 2

# 1. Calculate total of shiny bags * children
# 2. For each child,
  # Add total of (find child: input, outer_num) multiplied by its children values
  # recurse this until find child child is 'n'





def total(input_color, input_number = 1):
  children = create_dict([x for x in dict_rules if input_color in x])
  print(children)
  children_sum = sum(children.values())
  print(children_sum)
  total_bags = children_sum * input_number
  
  for k,v in children.items():
    next_child = create_dict([y for y in dict_rules if k in y])
    if next_child != 'no more bags':
      total_bags =+ total(k,v)
      
  print(total_bags)
  return total_bags

def add_lower(input):
  match = create_dict([x for x in dict_rules if input in x])
  total_lower = 0
  for k,v in match.items():
    #print (k, v)
    if v != 'n':
      v = int(v)
      total_lower += v
  print("in each ", k, " there are " , total_lower, "bags" )
  return total_lower


def get_total(input, operand = 1):
  total = 1
  match = create_dict([x for x in dict_rules if input in x])
  print(input , "contins", match.items())
  for k, v in match.items():
    if add_lower(k) ==  0:
      return total
    else:
      lower = add_lower(k)
      total += operand * lower
      
      #print (total)
  return total

def create_dict(input):
  value_dict = {}
  for i in input:
    for k,v in i.items():
      v = [items.strip() for items in v]
      v = [re.sub('bag$','bags', value) for value in v]
      for items in v:
        if v[0] != "no other bags":
          color = items.split(" ")[1:]
          color = ' '.join(color)
          number = items[0]
          value_dict[color] = int(number)
        else:
          color = items.split(" ")[1:]
          color = ' '.join(color)
          number = items[0]
          value_dict[color] = number
    return value_dict

def find_all_colors(color):
  match = create_dict([x for x in dict_rules if color in x])
  print(match)
  for k,v in match.items():
    if v == 'n':
      return match
    else:
      find_all_colors(k, level)

total_lower = 0 
for d in dict_rules:
  if "shiny gold bags" in d.keys():
    gold = d
    value_dict = {}
    for k,v in gold.items():
      v = [items.strip() for items in v]
      for items in v:
        color = items.split(" ")[1:]
        color = ' '.join(color)
        number = items[0]
        #print(color, number)
        value_dict[color] = number
    #for k,v in value_dict.items():
      #print(value_dict)
      total("shiny gold bags")

    




# def add_bags(color_dict):
#   for k,v in color_dict.items():
#     if v = 'no':
#       return total
#     else:
#       total = int(v) * 


  

  
