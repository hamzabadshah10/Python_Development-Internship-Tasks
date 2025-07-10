print("Promotion Eligibility Checker")

try:
    attendance = float(input("Enter attendance percentage: "))
    final_marks = float(input("Enter final marks: "))

    if attendance >= 75 and final_marks >= 50:
        print("Status: Promoted")
        
    else:
        print("Status: Not Promoted")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
