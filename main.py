"""
SMART STUDENT PERFORMANCE ANALYZER
Pure Python project — no external libraries required.
Compatible with Python 3.11 and IDLE.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "students.json"
SUBJECTS = ["Python", "Mathematics", "English", "Computer Science", "Electronics"]


def load_students():
    """Load saved student records from a JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved data. Starting with an empty list.")
        return []


def save_students(students):
    """Save records using Python's built-in JSON and file handling."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError as error:
        print(f"Could not save records: {error}")


def calculate_result(marks):
    total = sum(marks.values())
    maximum = len(marks) * 100
    percentage = total / maximum * 100 if maximum else 0

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Needs Improvement"

    return total, percentage, grade


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    student_id = input("Enter a unique student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if any(s["student_id"].lower() == student_id.lower() for s in students):
        print("That student ID already exists.")
        return

    marks = {}
    print("\nEnter marks out of 100:")
    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total, percentage, grade = calculate_result(marks)
    student = {
        "student_id": student_id,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }
    students.append(student)
    save_students(students)
    print(f"\nRecord saved for {name}. Percentage: {percentage:.2f}% | Grade: {grade}")


def show_student(student):
    print("\n" + "-" * 45)
    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print("Marks:")
    for subject, mark in student["marks"].items():
        print(f"  {subject:<22} {mark:>6.1f}/100")
    print(f"Total      : {student['total']:.1f}/{len(student['marks']) * 100}")
    print(f"Percentage : {student['percentage']:.2f}%")
    print(f"Grade      : {student['grade']}")
    print("-" * 45)


def list_students(students):
    if not students:
        print("No student records found.")
        return
    print("\nSTUDENT SUMMARY")
    print("-" * 70)
    print(f"{'ID':<14}{'NAME':<24}{'PERCENTAGE':>14}{'GRADE':>16}")
    print("-" * 70)
    for student in sorted(students, key=lambda s: s["percentage"], reverse=True):
        print(f"{student['student_id']:<14}{student['name'][:22]:<24}"
              f"{student['percentage']:>13.2f}%{student['grade']:>16}")
    print("-" * 70)


def search_student(students):
    query = input("Enter student ID or name: ").strip().lower()
    matches = [
        s for s in students
        if s["student_id"].lower() == query or query in s["name"].lower()
    ]
    if not matches:
        print("No matching student found.")
        return
    for student in matches:
        show_student(student)


def show_class_analytics(students):
    if not students:
        print("Add student records first.")
        return

    average = sum(s["percentage"] for s in students) / len(students)
    topper = max(students, key=lambda s: s["percentage"])
    print("\nCLASS ANALYTICS")
    print(f"Number of students : {len(students)}")
    print(f"Class average      : {average:.2f}%")
    print(f"Highest performer  : {topper['name']} ({topper['percentage']:.2f}%)")

    print("\nSubject averages:")
    for subject in SUBJECTS:
        subject_average = sum(s["marks"][subject] for s in students) / len(students)
        print(f"  {subject:<22} {subject_average:.2f}/100")

    pass_count = sum(1 for s in students if s["percentage"] >= 40)
    print(f"\nStudents at or above 40%: {pass_count}/{len(students)}")


def delete_student(students):
    student_id = input("Enter the ID of the student to delete: ").strip().lower()
    for student in students:
        if student["student_id"].lower() == student_id:
            confirm = input(f"Delete {student['name']}'s record? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.remove(student)
                save_students(students)
                print("Record deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Student ID not found.")


def export_report(students):
    """Export a readable report using only built-in file handling."""
    if not students:
        print("No records to export.")
        return

    report_path = Path(__file__).resolve().parent / "student_report.txt"
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write("SMART STUDENT PERFORMANCE REPORT\n")
            file.write("=" * 45 + "\n\n")
            for student in sorted(students, key=lambda s: s["percentage"], reverse=True):
                file.write(f"Name: {student['name']}\n")
                file.write(f"Student ID: {student['student_id']}\n")
                file.write(f"Percentage: {student['percentage']:.2f}%\n")
                file.write(f"Grade: {student['grade']}\n")
                file.write("Marks:\n")
                for subject, mark in student["marks"].items():
                    file.write(f"  {subject}: {mark}/100\n")
                file.write("-" * 45 + "\n")
        print(f"Report exported to: {report_path}")
    except OSError as error:
        print(f"Could not export report: {error}")


def main():
    students = load_students()
    while True:
        print("\n" + "=" * 48)
        print("  SMART STUDENT PERFORMANCE ANALYZER")
        print("=" * 48)
        print("1. Add student and marks")
        print("2. View all students (ranked)")
        print("3. Search student")
        print("4. View class analytics")
        print("5. Delete student record")
        print("6. Export report to TXT")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_class_analytics(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            export_report(students)
        elif choice == "7":
            print("Thank you for using the Student Performance Analyzer!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
