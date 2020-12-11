file = open('day1.txt', 'r')
numbers = file.read().split('\n')
numbers = list(map(int, numbers))
numbers.sort()

n = len(numbers)
done = False

# Day one Part - 1 solution

# for i in range (n):
#   for j in range (i + 1, n):
#     if numbers[i] + numbers[j] == 2020 :
#       done = True
#       break
#     elif numbers[i] + numbers[j] > 2020:
#       break
#   if done :
#     break
# print (numbers[i], numbers[j])
# print (numbers[i] * numbers[j])

# Day 2 part 2 Solution

for i in range (n):
  for j in range (i + 1, n):
    for k in range (j + 1, n):
      if numbers[i] + numbers[j] + numbers[k] == 2020 :
        done = True
        break
      elif numbers[i] + numbers[j] + numbers[k] > 2020:
        break
    if done :
      break
  if done :
    break
print (numbers[i], numbers[j], numbers[k])
print (numbers[i] * numbers[j] * numbers[k])