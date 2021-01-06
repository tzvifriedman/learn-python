import re

required_items = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

with open('4-input.txt') as f:
  items = f.read()

items = items.split('\n\n')


pports = []
for i in items:
  item = i.rstrip().replace("\n"," ").split(" ")
  pports.append(item)

def eval_valid(input):
  count = 0
  item = str(input).replace(":", " ")
  valid = "valid"
  for req_item in required_items:
    if req_item not in item:
      valid = "invalid"
  if valid:
    # Nested if to check validation
    count += 1
  return valid    

total_count = 0
for p in pports:
  d = dict(x.split(":") for x in p)
  if eval_valid(p) == "valid":
    print(p)
    valid = "valid"
    for r in required_items:
      # check BYR (4 digits, between 1920 and 2002)
      if valid == "valid":
        if r == 'byr':
          if re.match("^[0-9]{4}$", d[r]):
            if  1920 <= int(d[r]) <= 2002:  
              valid = "valid"
              print(r, d[r],valid)
            else:
              valid = "invalid"
              print(d[r], valid)
          else:
            valid = "invalid"
            print(r, d[r], valid)
        # check IYR (4 digits, between 2010 and 2020)
      if valid == "valid":
        if r == 'iyr':
          if re.match("^[0-9]{4}$", d[r]):
            if 2010  <= int(d[r]) <= 2020:
              valid = "valid"
              print(r, d[r], valid)
            else:
              valid = "invalid"
              print(r, d[r], valid)
          else:
            valid = "invalid"
            print(r, d[r], valid)
        # check EYR (4 digits, between 2020 amd 2030)
      if valid == "valid":  
        if r == 'eyr':
          if re.match("^[0-9]{4}$", d[r]):
            if 2020  <= int(d[r]) <= 2030:
              valid = "valid"
              print(r, d[r], valid)
            else:
              valid = "invalid"
              print(r, d[r], valid)
          else:
            valid = "invalid"
            print(r, d[r], valid)     
        # Check HGT (1 number followed by cm on in, cm is between 150 and 193, in: 59-76)
      if valid == "valid":
        if r == 'hgt':
          if re.match("^[0-9]*(cm|in)$", d[r]):
            if "cm" in d[r]:
              if 150 <= int(d[r].replace("cm", "")) <= 193:
                valid = "valid"
                print(r, d[r], valid)
              else:
                valid = "failed range"
                print(r, d[r], valid)
            elif "in" in d[r]:
              if 59 <= int(d[r].replace("in", "")) <= 76:
                valid = "valid"
                print(r,d[r], valid)
              else:
                valid = "failed range"
                print(r, d[r], valid)
          else:
            valid = "failed regex"
            print(r, d[r], valid)
      # CHeck HCL (# followed by 6 char alphanumeric 0-9,a-f)
      if valid == "valid":
        if r == 'hcl':
          if re.match("^^#[0-9a-f]{6}$", d[r]):
            valid = "valid"
            print (r, d[r], valid)
          else:
            valid = "failed regex"
            print (r, d[r], valid)

      # Check ECL (one of amb, blu, gry, grn, hzl, oth)
      if valid == "valid":
        if r == 'ecl':
          if re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", d[r]):
            valid = "valid"
            print(r, d[r], valid)
          else:
            valid = "failed regex"
            print(r, d[r], valid)

      # Check pid (9 digits, including zeroes?)
      if valid == "valid":
        if r == 'pid':
          if re.match("^[0-9]{9}$", d[r]):
            valid = "valid"
            print( r, d[r], valid)
          else:
            valid = "failed regex"
            print(r, d[r], valid)
      # check CID (don't check)
      # increment total if we get here in one piece
  else:
    valid = "failed key check"
    print(d, valid)    
  if valid == "valid":
    print(total_count)
    total_count += 1

print(total_count)


