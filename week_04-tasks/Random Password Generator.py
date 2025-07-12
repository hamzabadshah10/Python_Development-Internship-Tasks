# Random Password Generator using random library

import random

Characters = "abcde12345@#$%"

Password = ""

for i in range(10):

    Password += random.choice(Characters)

print(F"Generated Random Password is:{Password}")