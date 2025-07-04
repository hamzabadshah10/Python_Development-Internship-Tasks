# Voting Eligibility Checker

YearOfBirth = int(input("Enter your year of birth: "))

CurrentYear = 2025

Age = CurrentYear - YearOfBirth

print(f"\nYou are {Age} years old.")

if Age >= 18:
    
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote yet.")
