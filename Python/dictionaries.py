#Dictionary : key-value pairs
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])
print(type(states))

print(states.get('FL', 'Not Found'))    #'Not Found' is the default value for key FL if it does not have a value pair; used with .get()
print(states.get('CA', 'Not Found'))

print(states.keys())
print(states.values())

#Dictionaries and lists can be inside of each other

animal_sounds = {
    "cat" : ["meow", "purr"],
    "dog" : ["woof", "bark"],
    "fox": []
}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = (mattan, chris, sarah) #The variables inside the list are now all dictionaries. If you print the list, you'll get all the dictionaries. 

print(people)

for person in people:
    print(person['height'])