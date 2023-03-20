import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

for i in range(1):
    print(f"{random.choice(names)} is going to buy the meal today!")

