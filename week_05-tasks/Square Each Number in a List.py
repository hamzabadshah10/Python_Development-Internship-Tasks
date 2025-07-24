def square_numbers_list(NumberList):

    SquaredList = [num ** 2 for num in NumberList]

    return (SquaredList)

Original_list= [2, 4, 6, 8]
print ("Original List:",Original_list)

Result = square_numbers_list(Original_list)
print(f"Squared List Numbers:{Result}")
