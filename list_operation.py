magicians = ["alice", "david", "carolina"]
len = len(magicians[1])

print(len)
for magician in magicians:
	print(magician.title())
	#print("I can't wait to see your next trick,", magician.title(), "\n")
	#print("I can't wait to see your next trick," + magician.title() + "\n")


print("Thank you")

str_line1 = ["A1", "B1", "C1"]
str_line2 = ["A2", "B2", "C2"]

str_array = [str_line1, str_line2]
for str_line in str_array:
	print(str_line)
	for string in str_line:
		print(string)
	
	print("\n")

pizza_list = ["super supreme", "seafood supreme", "new orleans", "hawaii", "cheese lover"]
friend_pizzas = pizza_list[:]
pizza_list.append("bacon lover")
friend_pizzas.append("tropical fruit")
print("My favourite pizzas are:")
for my_pizza in pizza_list[0:3]:
	print(my_pizza.title())
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza.title())

for pizza in pizza_list:
	print("I like", pizza, "so much")

print("I really love pizza")

pet_list = ["dog", "cat", "duck", "mouse", "dutch pig"]
for pet in pet_list:
	print("A", pet, "would make a great pet")
	
print("Any of these animals would make a great pet!")
