def is_even_or_odd(Number):

    if Number % 2 == 0:
        return "Even"
    
    else:
        return "Odd"

Result = is_even_or_odd(18)
print("The number is:", Result)
