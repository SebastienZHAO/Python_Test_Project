
for value in range(1,2):
	print(value)

value =1

numbers = [11,2,35,43,5]
print(sorted(numbers, reverse = True))
new_numbers = list(range(1,6))
print(new_numbers)

even_numbers = list(range(0,11,2))
print(even_numbers)

squares = []
for num in range(1,11):
	squares.append(num ** 2)
	
print(squares, min(squares), max(squares))

new_squares = [new_num ** 2 for new_num in range(1,11)]
print(new_squares, min(new_squares), max(new_squares))

num_3_list = []
million_numbers = list(range(1,31))
for number in million_numbers:
	if (number % 3 == 0) :
		num_3_list.append(number)
		
print("num_3_list is:", num_3_list)
print("million_numbers is listed:", million_numbers, "\n",
"minumux number of million_numbers is:", min(million_numbers), "\n" 
"maximum number of million_numbers is:", max(million_numbers), "\n"
"the sum of million_numbers is:", sum(million_numbers))

cubics = []
for num in range(1,11):
	cubics.append(num ** 3)

print(cubics)
cubics = [num ** 3 for num in range(1,11)]
print(cubics)

new_players = []
players = ["charles", "martina", "michael", "florence", "eli"]
new_players = players
print(new_players)
players.append("zoe")
print("players is appendded by new value :", players)
print("new_players:",new_players)
new_players.append("theodore")
print("new_players is appendded by new value:", new_players)
print("players is:", players)
print("The first three items in the list are:", players[:3])
print("Three items from the middle of the list are:", players[2:-2])
print("The last three items in the list are:", players[-3:])

for player in players[:3]:
	print(player.title())
part_of_players = sorted(players[:])
print(part_of_players)
