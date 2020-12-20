file = open('day8.txt', 'r')

string = file.read().split('\n')


### Part 1 Solution

# i = 0
# visited = []
# acc = 0
# # print(string)
# while i < len(string):
#     # print(visited, i)
#     if i in visited:
#         break
   
    # if 'nop' in (string[i]):
    #     visited.append(i)
    #     i += 1
    #     continue
    # if 'acc' in (string[i]):
    #     num = string[i].replace('acc ', '')
    #     num = int(num)
    #     acc += num
    #     visited.append(i)

    #     i += 1
    #     continue

    # if 'jmp' in (string[i]):
    #     num = string[i].replace('jmp ', '')
    #     num = int(num)
    #     visited.append(i)

    #     i += num
    #     continue

# print(acc)
    


###Part 2 Solution
lines = []
for line in string:
    line = line.rstrip().split(' ')
    lines.append([line[0], int(line[1])])

def find(lines):
    visited = []
    i = 0
    accu = 0
    while True:
        if i >= len(lines):
            return accu
        
        if i in visited:
            return False
        
        if lines[i][0] == 'nop':
            visited.append(i)
            i += 1
            continue

        if lines[i][0] == 'acc': 
            accu += lines[i][1]
            visited.append(i)
            i += 1
            continue

        if lines[i][0] == 'jmp':
            visited.append(i)
            i += lines[i][1]
            continue


for i in lines:
    prev = i[0]
    if i[0] == 'jmp':
        i[0] = 'nop'
    elif i [0] == 'nop':
        i[0] =='jmp'

    acc = find(lines)
    if acc:
        print(acc)
        break
    else:
        i[0] = prev