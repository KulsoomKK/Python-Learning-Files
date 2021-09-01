count = [1, 2, 3 , 4]
random_things = ["Billy", 13, ["list in a list"]]

for number in count:
    print("This is count", number)

for thing in random_things:
    print("Thing:", thing)

print("There are this many things:", len(random_things))
print("thing is of type:", type(random_things))

people = []

people.append("Sam")
people.append("Rob")

print(people)
print("First person:", people[0]) 

people.remove("Sam")
print(people)


for n in list(range(1, 11)):        #can do without typing list(..(..)), since range is a type of data function that acts like a list
    print("Square of", n, "=",n*n)

another_list = random_things[-1]    #You can go backwards through the list using negative numbers. The last thing in a list is always [-1]
print(another_list)
print(type(another_list))