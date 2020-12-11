import re


file = open('day4.txt', 'r')


string = file.read().split('\n\n')
total = 0


## Part - 1 Solution
# for i in string :
  
#   if 'byr' in i and 'iyr' in i and 'eyr' in i and 'hgt' in i and 'hcl' in i and 'ecl' in i and 'pid' in i:
#     total += 1

# print(total)


## Part - 2 Solution


def checkHeight(sec):
  if 'cm' in sec[1]:
    sec[1] = sec[1].replace("cm", '')
    try:
      # print(sec[1])
      n = int(sec[1])
      if n >= 150 and n <= 193:
        return True
    except:
      return False
  
  elif "in" in sec[1]:
    sec[1] = sec[1].replace("in", '')
    try:
      n = int(sec[1])
      if n >= 59 and n <= 76:
        return True
    except:
      return False
  
  return False

def hclChecker(sec):
  if '#' in sec[1]:
    sec[1] = sec[1].replace("#", "")
  else:
    return False
  if re.match("^[a-f0-9]*$", sec[1]):
    return True
  else:
    return False


for i in string :
  if not('byr' in i and 'iyr' in i and 'eyr' in i and 'hgt' in i and 'hcl' in i and 'ecl' in i and 'pid' in i):
    continue
  valid = True
  
  i = i.replace("\n", " ")
  part = i.split(' ')
  # print (part)
  for j in part:
    # print(type(j))
    sec = j.split(':')
    # print(sec[0], sec[1])
    if sec[0] == "byr":
      try : 
        n = int(sec[1])
        if n >= 1920 and n <= 2002:
          continue
        else:
          valid = False
          break
      except:
        valid = False
        break
    
    elif sec[0] == "iyr":
      try : 
        n = int(sec[1])
        if n >= 2010 and n <= 2020:
          continue
        else:
          valid = False
          break
      
      except:
        valid = False
        break

    elif sec[0] == "eyr":
      try : 
        n = int(sec[1])
        if n >= 2020 and n <= 2030:
          continue
        else:
          valid = False
          break
      
      except:
        valid = False
        break
    
    elif sec[0] == "hgt":
      # print(sec)
      status = checkHeight(sec)
      # print(status)
      if status:
        continue
      else:
        valid = False
        break


    elif sec[0] == "hcl":
      status = hclChecker(sec)

      if status:
        continue
      else:
        valid = False
        break

    elif sec[0] == "ecl":
      if sec[1] == "amb" or sec[1] == "blu" or sec[1] == "brn" or sec[1] == "gry" or sec[1] == "grn" or sec[1] == "hzl" or sec[1] == "oth":
        continue
      else:
        valid = False
        break

    elif sec[0] == "pid":
      try:
        n = int(sec[1])
        if len(sec[1]) == 9:
          continue
        else:
          valid = False
          break
      
      except:
        valid = False
        break
    
    
  
  if valid:
    total += 1
    print(i)

print(total)

    
    
