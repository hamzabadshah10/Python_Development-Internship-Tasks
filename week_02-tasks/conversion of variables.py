# Variable Declaration with Different Data Types

StringVar = "123"
IntegerVar = 45
FloatVar = 78.9
BooleanVar = True
ComplexVar = 4 + 3j

print("----- Original Values and Types -----")
print(f"StringVar| {StringVar}, Type| {type(StringVar)}")
print(f"IntegerVar| {IntegerVar}, Type| {type(IntegerVar)}")
print(f"FloatVar| {FloatVar}, Type| {type(FloatVar)}")
print(f"BooleanVar| {BooleanVar}, Type| {type(BooleanVar)}")
print(f"ComplexVar| {ComplexVar}, Type| {type(ComplexVar)}")


try:
    ConvertedStringVar = int(StringVar)

except ValueError:
    ConvertedStringVar = "Conversion Failed"

ConvertedIntegerVar = float(IntegerVar)

ConvertedFloatVar = str(FloatVar)

ConvertedBooleanVar = int(BooleanVar)

ConvertedComplexVar = str(ComplexVar)

print("\n----- Converted Values and Types -----")
print(f"ConvertedStringVar| {ConvertedStringVar}, Type| {type(ConvertedStringVar)}")
print(f"ConvertedIntegerVar| {ConvertedIntegerVar}, Type| {type(ConvertedIntegerVar)}")
print(f"ConvertedFloatVar| {ConvertedFloatVar}, Type| {type(ConvertedFloatVar)}")
print(f"ConvertedBooleanVar| {ConvertedBooleanVar}, Type| {type(ConvertedBooleanVar)}")
print(f"ConvertedComplexVar| {ConvertedComplexVar}, Type| {type(ConvertedComplexVar)}")
