with open('3-input.txt', 'r') as f:
  lines = [line.rstrip() for line in f]

skip = []
count = 2
for l in lines:
  if count % 2 == 0:
    skip.append(l)
  count += 1
print(len(skip))



# tree = 0
# index = 0
# for l in lines:
#   if l[index] == "#":
#     tree += 1
#   print(index)
#   index = (index + 3) % int(len(l))
# print(tree)

def do_slope(right, down, input):
  trees = 0
  index = 0 
  for l in input:
    if l[index] == "#":
      trees += 1
    index = (index + right) % int(len(l))
  # elif down == 2:
  #   count = 2
  #   index = 0
  #   for l in input:
  #     if count % 2 == 0:
  #       print(l[index])
  #       if l[index] == "#":
  #         trees +=1 
  #     index = (index + right) % int(len(l))
  #     count += 1
  return trees   

total = do_slope(1,1,lines) * do_slope(3,1,lines) * do_slope(5,1,lines) * do_slope(7,1,lines) * do_slope(1,2,skip)

print(total)