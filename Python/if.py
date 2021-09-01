answer = input("Do you want to hear a joke? ").upper()  # can also use .casefold() to strip case sensitivity 

if answer == "YES":
    print("I'm against picketing, but I don't know how to show it.")

elif answer == "NO":
    print("Bye.")

else:
    print("idk")