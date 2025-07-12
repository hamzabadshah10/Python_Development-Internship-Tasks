import math  

Radius = float(input("Enter the radius of the circle: "))

Area = math.pi * Radius ** 2
Circumference = 2 * math.pi * Radius
SqrtArea = math.sqrt(Area)


print(f"\nArea of Circle: {Area:.4f}")
print(f"Circumference: {Circumference:.4f}")
print(f"Square Root of Area: {SqrtArea:.4f}")
