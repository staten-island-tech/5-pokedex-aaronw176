import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" for i in data:
    print(i['name']) """
# Add a language choice feature and print the pokemons name based on the user input
""" language = input("Select a language english, japanese, french, and chinese: ").lower()
for i in data:
    print(i['name'][language]) """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
""" language = input("Select a language english, japanese, french, and chinese: ").lower()
types = input("Select a pokemon type ")
values = 0
value = []
for i in data:
    try:
        if i['type'][0] == types:
            values += 1
            value.append(i["name"][language])
        elif i['type'][1] == types:
            values += 1
            value.append(i["name"][language])
    except IndexError: 
        "pokemon"
if values != 0:
    print(f"The {types} pokemones are {value}")
else:
    print(f"There are no pokemon of the type {types}") """
""" for i in data:
    if types in i['type']:
        value.append(i['name'][language])
        values = 1
if values == 1:
    print(value)
else: 
    print(f"There is no pokemon with the type {types}") """
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def name(pokemon):
    for i in data:
        for pokemon in i['name']["english"]:
            print(pokemon)
name("char")
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

