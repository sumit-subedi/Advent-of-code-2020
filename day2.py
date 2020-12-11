# 1-3 a: abcde
file = open('day2.txt', 'r')

string = file.read().split('\n')
total = 0


# day2 part 1 Solution
# for i in string:
  
#   pos = i.find ('-')
#   least = int(i[0:pos])
#   most = int(i[pos+1:pos+3])
#   pos2 = i.find(':')

#   char = i[pos2 -1]
#   chars = i[pos2 + 2:]. strip()
#   count = chars.count(char)
#   if count >= least and count <= most:
#     total += 1

# print(total)


#day 2 part 2 solution

for i in string:
  
  pos = i.find ('-')
  least = int(i[0:pos])
  most = int(i[pos+1:pos+3])
  pos2 = i.find(':')

  char = i[pos2 -1]
  chars = i[pos2 + 2:]. strip()
  
  try :
    
    if (chars[least - 1] == char and chars[most - 1] != char) or (chars[most - 1] == char and chars[least - 1] != char):
      total = total + 1
  except:
    continue
print(total)
