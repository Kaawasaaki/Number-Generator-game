import random


top_of_range = input("Enter any number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter a number next time")
    quit()
        
generator = random.randint(0, top_of_range)

print("You entered: ", top_of_range)
print("Number by system: ", generator)

if top_of_range == generator:
    print("You have guessed correctly!")
else:
    print("Try again!")

