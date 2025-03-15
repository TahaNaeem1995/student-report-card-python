# Function to interactively collect student data
def collect_student_data():
    while True:
        # Collecting student details
        name = input("Enter the student's name: ")
        roll_no = input("Enter the student's roll number: ")
        
        # Collecting marks for subjects
        subjects = {}
        num_subjects = int(input("Enter the number of subjects: "))
        for _ in range(num_subjects):
            subject = input("Enter subject name: ")
            marks = float(input(f"Enter marks for {subject}: "))
            subjects[subject] = marks
        
        # Yielding collected student data
        yield name, roll_no, subjects

        # Ask if user wants to enter more student data
        cont = input("Do you want to enter data for another student? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

# Function to calculate total, average, and grade
def calculate_report_card(name, roll_no, subjects):
    total_marks = sum(subjects.values())
    average_marks = total_marks / len(subjects)
    
    # Grade calculation based on average marks
    if average_marks >= 90:
        grade = 'A+'
    elif average_marks >= 80:
        grade = 'A'
    elif average_marks >= 70:
        grade = 'B'
    elif average_marks >= 60:
        grade = 'C'
    elif average_marks >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # Generate formatted report card
    print("\nStudent Report Card")
    print(f"Name: {name}")
    print(f"Roll No: {roll_no}")
    print("\nSubjects & Marks:")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    
    print("\nSummary:")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")
    print("="*30)

# Main function to drive the program
def main():
    print("Welcome to the Student Report Card Generator!\n")
    
    # Generator to collect and process student data
    for name, roll_no, subjects in collect_student_data():
        calculate_report_card(name, roll_no, subjects)
        print("\n")  # New line for separation between students

# Run the program
if __name__ == "__main__":
    main()
