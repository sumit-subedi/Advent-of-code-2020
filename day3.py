file = open('day3.txt', 'r')

string = file.read().split('\n')
total = 0
start = 0
right = 1

for i in string[::2]:
  pos = int((start + right) % 31)
  start = pos
  if i[pos] == "#":
    total += 1

print(total)

