new_array = (11,2,53,24,18,99,72,83,59,66,50)

for item in new_array:
	if (item > 50 and item < 60):
		print(item, "is greater than 50 and less than 60")
	elif (item < 50):
		print(item, "is less than 50")
	elif (item < 20 or item > 80):
		print(item, "is a bigger or smaller number")
	elif (item == 50):
		print(item, "is equal to 50")

target_num = 72
if (target_num in new_array):
#for item in new_array:
#	if(item == 7):
#		target_num = item

#if (target_num):
	print(target_num, "target is in new_array")
else:
	print("target is not in the new_array")


car = "audi"
new_car = car[:2]
print(new_car)
print("Is car == 'subaru'? I predict True")
print(car[1])


