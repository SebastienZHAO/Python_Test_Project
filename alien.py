
grades = 0
alien_color = ["green", "yellow", "red"]
if "green" not in alien_color:
	grades = 5
	print("player's grades is ", grades)

request_toppings = ["mushroom", "green peppers", "extra cheese"]
order_guests = ["Janey", "Frank", "Lilian"]
new_pizzas = []

for i in range(0,len(request_toppings)):
	new_pizzas.append(request_toppings[i] + " " + order_guests[i])

print(new_pizzas)

users_list = order_guests[:]
users_list.append("zoe")
users_list.append("theodore")
users_list.append("admin")

#this measure can delete all items of users_list
#del users_list[:]  

if users_list:
	for user in users_list:
		if user == "Admin":
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello ", user, ", thank you for logging in again")
else:
	print("We need to find some users")

current_users = users_list[:]
new_users = ["zoE", "theodore"]
new_users.append("Sebastien")
new_users.append("Benny")
new_users.append("Gorge")

for new_user in new_users:
	if new_user.lower() in current_users or new_user.upper() in current_users or new_user.title() in current_users:
	#if new_user in current_users:
		print(new_user, "has existed in current_users, please use another user name")
	else:
		print(new_user, "has not been uesed yet")
