def greet_user(Name, Age):
    return f"Hello {Name}, you are {Age} years old."

UserName = input("Enter your name: ")
UserAge = input("Enter your age: ")

Greeting = greet_user(UserName, UserAge)
print(Greeting)



