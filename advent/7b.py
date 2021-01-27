with open('7-input.txt') as f:
  rules = f.readlines()

dict_rules = []

for r in rules:
  root_split = r.split("contain") ## get the root color by splitting off of contain  
  root = root_split[0].strip() ## remove whitespace
  # After that, we will make a dict that contains the root as the key and the list of possible colors as the value
  # Do this by splitting everything after the first root_split by "," and removing the period
  for n in root_split[1:]:
    children = n.replace(".","").split(", ")
    children = [c.strip() for c in children]
    num_dict = {c.split(" ")[1:3] : c.split(" ")[0] for c in children}
    #print("spaceaz?" , children)

  # make the dict from the root and the colors list
  rule = {root:{num_dict}}
  #append to full list
  dict_rules.append(rule)


print(dict_rules)