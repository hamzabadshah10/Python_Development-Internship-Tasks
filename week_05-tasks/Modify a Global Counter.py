Counter = 0

print(f"\nInitialy Counter Value: {Counter}.")

def change_counter():
    global Counter
    Counter += 1
    return Counter

print ("\n")
print("Counter after 1st call:", change_counter())
print("Counter after 2nd call:", change_counter())
print("Counter after 3rd call:", change_counter())
