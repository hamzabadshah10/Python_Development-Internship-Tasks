# Data Type Tester with Boolean Check

UserInput = input("Enter any value: ")

print(f"\nPython sees it as: {type(UserInput)}")

LowerInput = UserInput.lower()

if LowerInput == "true" or LowerInput == "false":
    print("You entered a boolean!")
    
else:
    try:
        ConvertedValue = int(UserInput)
        print("You entered an integer!")

    except ValueError:
        try:

            ConvertedValue = float(UserInput)
            print("You entered a float!")

        except ValueError:
            print("You entered a string!")


