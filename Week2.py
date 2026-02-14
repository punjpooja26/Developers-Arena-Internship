# Student Grade Calculator

def calculate_grade(marks):
    """Function to return grade and message based on marks"""
    if 90 <= marks <= 100:
        return "A", "Excellent Work! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! Keep improving! 😊"
    elif 60 <= marks <= 69:
        return "D", "You passed! Work a bit harder! 💪"
    else:
        return "F", "Don't give up! Try again! 📚"

# Input: Student Name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid! Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Invalid input! Please enter numeric value.")

# Function call
grade, message = calculate_grade(marks)

# Output Result
print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
