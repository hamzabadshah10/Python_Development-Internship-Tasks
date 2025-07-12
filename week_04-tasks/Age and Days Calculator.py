import datetime  

year = int(input("Enter your birth year:"))
month = int(input("Enter your birth month:"))
day = int(input("Enter your birth day:"))

date_of_birth = datetime.date(year, month, day)
today = datetime.date.today()

age_years = today.year - date_of_birth.year
if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
    age_years -= 1

days_lived = (today - date_of_birth).days

print("\nYou are", age_years, "years old.")
print("You have lived for", days_lived, "days.")
