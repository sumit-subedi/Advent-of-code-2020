import math


file = open('day5.txt', 'r')

string = file.read().split('\n\n')
nums = []
for seat in string:
  print(seat)
  low = 0
  high = 127
  row = 0
  column = 0

  for i in range(7):
    print("here")
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
  nums.append(row * 8 + column)
  print(row * 8 + column)

print((nums))