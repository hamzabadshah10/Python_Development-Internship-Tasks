print("Grade Calculator")

try:
    subject_1 = float(input("Enter marks for Subject 1: "))
    subject_2 = float(input("Enter marks for Subject 2: "))
    subject_3 = float(input("Enter marks for Subject 3: "))

    total_obtained_marks = subject_1 + subject_2 + subject_3
    percentage = (total_obtained_marks / 300) * 100  

    if percentage >= 85:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 50:
        grade = "C"
        
    else:
        grade = "Fail"

    print("\n--- Result ---")
    print("Total Obtained Marks:", total_obtained_marks)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

except ValueError:
    print("Invalid input. Please enter numeric values only.")
