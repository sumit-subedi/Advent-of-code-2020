import math


file = open('day5.txt', 'r')

string = file.read().split('\n')
nums = []


#part 1 solution
# for seat in string:
#   low = 0
#   high = 127
#   row = 0
#   column = 0

#   for i in range(7):
   
#     if seat[i] == "F":
#       high = int((low + high) / 2)

#     elif seat[i] == "B":
#       low = int((high - low) / 2)
#       low = high - low
  

#   row = high
#   low = 0
#   high = 7

  

#   for i in range(7, len(seat)):
#     if seat[i] == "L":
#       high = int((low + high) / 2)

#     elif seat[i] == "R":
#       low = int((high - low) / 2)
#       low = high - low
    
#   column = high
#   nums.append(row * 8 + column)
  

# print(max(nums))

###  End of part 1 solution


### Part 2 solution



for seat in string:
  low = 0
  high = 127
  row = 0
  column = 0

  for i in range(7):
   
    if seat[i] == "F":
      high = int((low + high) / 2)

    elif seat[i] == "B":
      low = int((high - low) / 2)
      low = high - low
  

  row = high
  low = 0
  high = 7

  

  for i in range(7, len(seat)):
    if seat[i] == "L":
      high = int((low + high) / 2)

    elif seat[i] == "R":
      low = int((high - low) / 2)
      low = high - low
    
  column = high
  if row == 0 or row == 127:
    continue
  nums.append(row * 8 + column)



for i in range(min(nums) + 1, max(nums)):
  if i not in nums:
    break

print(i)
