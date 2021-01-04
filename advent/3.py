with open('3-input.txt', 'r') as f:
  lines = [line.rstrip() for line in f]


index = 0
for l in lines:
  l = l[:index-1] + ">" + l[:index]
  print(index ,l)
index = (index + 3) % len(l)
