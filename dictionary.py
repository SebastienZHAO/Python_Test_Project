alien_0 = {"color":"green", "points":5}

print(alien_0)

alien_0['y_position'] = 0
alien_0['x_position'] = 25
print(alien_0)

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print(favorite_language['edward'].title())

people_information = {
    "first_name":"zoe",
    "last_name":"chiu",
    "age":"7",
    "city":"saskatoon"
}

print(people_information)

print(people_information["first_name"], people_information["last_name"], people_information["age"], people_information["city"])

for name, language in people_information.items():
	print("\nKey: ", name)
	print("Value: ", language)
	
print(sorted(people_information.keys(), reverse = True))
print(sorted(people_information.values()))
for key in people_information.keys():
	print(key.title())
	
for value in people_information.values():
	print(value)


languages = {
    "pascal":"the first language designed for programmer",
    "c":"the most effecient language for programming",
    "java":"suitable for web development",
    "c++":"oriented object based on c language",
    "python":"the greatest language first ever in recording human history",
}

languages["dictionary"] = "a function like a dictionary"
languages["list"] = "an array of characters or digits"
languages["function"] = "that offer an method for special target"
languages["string"] = "a series of characters or digits"
languages["if statement"] = "check current state of program and take steps"
for language,meaning in languages.items():
	print(language.title(), ":\n    ", meaning.title())
	
	
rivers = {
    "nile":"egypt",
    "red river":"manitoba",
    "saskatchewan river":"saskatchewan"
}

print("\n\n\n")
for river,area in rivers.items():
	print("The", river.title(), "runs through", area.title())
	
for river in rivers.keys():
	print(river.title())
	
for country in rivers.values():
	print(country.title())


learned_languages = ["c", "python"]


print("\n\n\n")
for language in languages.keys():
	if language in learned_languages:
		print("Congrats! You have mastered ", language.title())
	elif language not in learned_languages:
		print("You may have to learn", language.title(), "more hard")
