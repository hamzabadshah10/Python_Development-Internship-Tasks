user_expression = input("Enter any Python expression of your choice: ")

try:
    local_scope = {}

    exec("result = " + user_expression, {}, local_scope)
    print("\nResult =" , local_scope['result'])
    print("Data type of result:", type(local_scope['result']))

except Exception as error:

    print("An error occurred while evaluating:", error)
