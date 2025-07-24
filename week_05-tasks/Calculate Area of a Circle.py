def calculate_area(Radius):

    return 3.14 * (Radius ** 2)

Radius = float(input("Enter radius: "))
Area = calculate_area(Radius)

print("Area of Circle:",  Area)
