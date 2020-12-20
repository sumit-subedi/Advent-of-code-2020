file = open('day7.txt', 'r')

string = file.read().split('\n')



###  Part-1 Solution
# dict = {}

# for inp in string:
#   org_bag = inp.split('contain')
#   org_bag[0] = org_bag[0][: org_bag[0].index('bag')].strip()
#   containing_bags = org_bag[1].split(', ')
#   containing_bags = [i[ : i.index('bag') ].strip() for i in containing_bags]
  
#   dict[org_bag[0]] = containing_bags


# #### VERY TIME CONSUMING NEED TO REFACTOR


# bag_List = []
# total = 0
# for keys in dict:
  
#   for i in range(len(dict[keys])):
#     dict[keys][i] = dict[keys][i] [1 : ].strip() 
#     if 'shiny gold' in dict[keys][i]:
#       bag_List.append(keys)
#       total += 1

# # print(dict)
# # print(bag_List)
# status = True
# newbag_List = bag_List.copy()
# while status:
#   bag_List = newbag_List.copy()
#   status = False
#   for bag in bag_List:
#     for keys in dict:
#       # print(keys, bag)
#       if keys in newbag_List:
#         # print(keys)
#         continue
      

#       if bag in dict[keys]:
#         # print(bag, dict[keys], keys)
#         newbag_List.append(keys)
#         total += 1
#         status = True
        

# # print(bag_List)

# print(total)


#### Part 2 Solution
bag_dict = {}
for line in string:
	key , value = line.split('bags ')
	key = key.strip()
	bag_dict[key] = []
	value = value.replace('contain ', '').split(', ')
	for item in value:
		index = item.find('bag')
		item = item [: index]
		if item == 'no other ':
			item = '0 bag'

		number = item[0]
		bag = item[2:].strip()
		bag_dict[key].append([int(number), bag])

subtotal = 0
def find(bags):
	sum = 0
	global subtotal
	if bag_dict[bags][0][0] == 0:
		return 0
	else:
		for num in bag_dict[bags]:
			sum = num[0] + (num[0] * find(num[1]))
			subtotal += sum
			print(sum, num[1], bags)


		return subtotal



total = 0
for bag in bag_dict['shiny gold']:
	value = find(bag[1])
	print(value, bag[0])
	total += bag[0] + (bag[0] * value) 
	subtotal = 0



	

print(total)


