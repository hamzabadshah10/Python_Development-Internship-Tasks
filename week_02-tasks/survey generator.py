# Command-Line Survey

FullName = input("What is your full name? ")
FavoriteFood = input("What is your favorite food? ")
BirthYear = int(input("In which year were you born? "))
FavoriteNumber = input("What is your favorite number? ")
FavoriteLanguage = input("What is your favorite programming language? ")

CurrentYear = 2025
Age = CurrentYear - BirthYear

print("\n----- Survey Summary -----")
print(f"Name: {FullName}")
print(f"Age: {Age} years old (Born in {BirthYear})")
print(f"Favorite Food: {FavoriteFood}")
print(f"Favorite Number: {FavoriteNumber}")
print(f"Favorite Programming Language: {FavoriteLanguage}")
print(f"\nThank you, {FullName}, for participating in the survey!")
