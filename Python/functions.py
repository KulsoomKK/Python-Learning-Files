def greet(name):
    return f"Hey {name}!"

print(greet("Bob"))
print(greet("Bobina"))

def concatenate(word1, word2):
    return word1 + word2

print(concatenate("Bob", "Rib"))
print(concatenate(word2 = "Bob", word1 = "Rib"))


def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(19))

def uppercase_and_reverse(str):
    return (str[::-1]).upper()

print(uppercase_and_reverse("Do not go gentle into that good night."))
#~~~~~ ANOTHER WAY TO DO uppercase_and_reverse(text): ~~~~~~
# def uppercase_and_reverse(text):
#     return reverse(text.upper())
    
# def reverse(text):
#     return text [::-1]

# print(uppercase_and_reverse("banana")) # ANANAB