
aliens = []

for new_alien in range(30):
	new_alien = {"color":"green", "points":5, "speed":"slow"}
	aliens.append(new_alien)

print("the size of aliens is :", len(aliens), "\n")
for alien in aliens:
	print(alien)
	

print("\n\n\n**********  a new aliens  ***********")
for alien in aliens[:3]:
	alien["color"] = "yellow"
	alien["points"] = 10
	alien["speed"] = "middle"
	
for alien in aliens:
	print(alien)

print("\n\n****************    6-7 Below list my family member information    *******************")
#this dictionary contains my family's information
family_information = {
    "zoe":{
        "first_name":"zoe",
        "last_name":"chiu",
        "age":7,
        "city":"saskatoon",
    },
    
    "theodore":{
        "first_name":"theodore",
        "last_name":"chiu",
        "age":5,
        "city":"saskatoon",
    },
    
    "lillian":{
        "first_name":"lillian",
        "last_name":"zhang",
        "age":36,
        "city":"saskatoon",
    },
    
    "sebastien":{
        "first_name":"sebastien",
        "last_name":"chiu",
        "age":36,
        "city":"saskatoon",
    },
}

for member,informations in family_information.items():
	print("The family member is:", member)
	#for information in informations:
	print("Full name:", informations["first_name"].title(), informations["last_name"].title())
	print("Age:", informations["age"])
	print("Location:", informations["city"].title())
	print("\n")


kafi = {
    "name":"kafi",
    "species":"cat",
    "owner":"lillian",
}

ponny = {
    "name":"ponny",
    "species":"horse",
    "owner":"theodore",
}

paw_petrol = {
    "name":"paw_petrol",
    "species":"dog",
    "owner":"zoe",
}

donald = {
    "name":"donald",
    "species":"duck",
    "owner":"sebastien",
}

pets = [kafi, ponny, paw_petrol, donald]

print("\n\n\n**********************  6-8 pets ****************************")
for pet in pets:
	print(pet["name"].title(), ":")
	print("Species:", pet["species"].title())
	print("Owner:", pet["owner"].title())
	print("\n")

print("\n\n\n**********************  6-9 favorite places ****************************")

favorite_places = {
    "zoe":["chang_long", "disney", "meng_huan_cheng"],
    "theodore":["chang_long", "meng_huan_cheng"],
    "lillian":["walk_street", "disney", "home"],
    "sebastien":["canada"],
}



for name, favorite_place in favorite_places.items():
	print(name.title(), ":")
	for place in favorite_place:
		print(place.title())
		
	print("\n")
	
	
print("\n\n\n**********************  6-11 cities ****************************")
cities = {
    "vancouver":{
        "country":"canada",
        "population":"2.46 million",
        "fact":"the biggest metropolitan in western canada",
    },
    
    "new york":{
        "country":"usa",
        "population":"15 million",
        "fact":"the financial capital of the world",
    },
    
    "london":{
        "country":"uk",
        "population":"8 million",
        "fact":"the capital of the UK and business center of Europe",
    },
}

for city,information in cities.items():
	print(city.title(),":")
	print("Country:",information["country"].upper())
	print("Population:", information["population"].title())
	print("Fact:", information["fact"].title())
	print("\n")
