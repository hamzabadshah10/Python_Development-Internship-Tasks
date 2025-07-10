print("Billing System with Discount")

try:

    number_of_products = int(input("Enter number of products: "))
    total_price = float(input("Enter total price: "))

    if total_price > 1000 and number_of_products > 3:
        discount = 0.15 * total_price

    elif total_price > 500:
        discount = 0.10 * total_price

    else:
        discount = 0.0

    final_amount = total_price - discount

    print("\n--- Final Bill ---")
    print(f"Original Price {total_price}")
    print(f"Discount Applied {round(discount,2)}")
    print(f"Final Amount to Pay {round(final_amount,2)}")

except ValueError:

    print("Invalid input. Please enter numeric values only.")
