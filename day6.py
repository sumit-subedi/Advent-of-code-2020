

file = open('day6.txt', 'r')

string = file.read().split('\n\n')
# print(string)
total = 0
for inp in string:
  status = True
  items = inp.split("\n")
 
  inp = inp.replace("\n", "")
  unique = set(inp)
  # print(unique, items)
  count = 0
  for i in unique:
    status = True
    for j in items:
      # print(i, j)
      if i in j :
        
        continue
      else:
        status = False
        break
    if status:
      count += 1
  
  # print(count , inp)
  total += count

print(total)  

