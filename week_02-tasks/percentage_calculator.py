# Marks Percentage Calculator

Subject1 = int(input("Enter marks for Subject 1: "))
Subject2 = int(input("Enter marks for Subject 2: "))
Subject3 = int(input("Enter marks for Subject 3: "))
Subject4 = int(input("Enter marks for Subject 4: "))
Subject5 = int(input("Enter marks for Subject 5: "))

TotalMarks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
Percentage = (TotalMarks / 500) * 100 

print("\n----- Result Report -----")
print(f"Total Marks: {TotalMarks} out of 500")
print(f"Percentage: {Percentage:.2f}%")
