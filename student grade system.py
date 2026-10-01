def calculate_grade(score):
    # Outer if: Check if the score is within the valid range (1 to 100)
    if 1 <= score <= 100:
        # Nested if-else statements for grading
        if score >= 90:
            return "Grade A (Excellent)"
        else:
            if score >= 80:
                return "Grade B (Very Good)"
            else:
                if score >= 70:
                    return "Grade C (Good)"
                else:
                    if score >= 60:
                        return "Grade D (Pass)"
                    else:
                        return "Grade F (Fail)"
    else:
        return "Invalid input! Please enter a score between 1 and 100."

# Taking user input
try:
    user_score = float(input("Enter the student's score (1-100): "))
    result = calculate_grade(user_score)
    print(result)
except ValueError:
    print("Please enter a valid number.")
