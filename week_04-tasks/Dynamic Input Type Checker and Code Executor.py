User_input = input("Enter any Python value: ")

print("\nYou entered:", User_input)
print("Data type before execution:", type(User_input))

try:
    print("\nExecuting your input using exec():")

    exec(User_input)

except Exception as Error:
    
    print("An error occurred while executing:", Error)