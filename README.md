# Smart Student Performance Analyzer

A command-line student marks and performance analysis system built with **pure Python 3.11**.

## No external dependencies
Uses only Python's built-in features and standard library: functions, loops, lists, dictionaries, sorting, exception handling, `json`, and `pathlib`.

## Features
- Add student records and marks across five subjects
- Validate input and prevent duplicate student IDs
- Calculate total, percentage, and grade
- Rank students by percentage
- Search records by student name or ID
- Show class average, topper, and subject averages
- Delete records with confirmation
- Save records persistently to `students.json`
- Export a readable report to `student_report.txt`

## Run in IDLE 3.11
1. Extract the ZIP file.
2. Open IDLE (Python 3.11).
3. Select **File → Open** and choose `main.py`.
4. Select **Run → Run Module** or press **F5**.
5. Use menu option 1 to add a student.

No `pip install` is needed.

## Suggested test
Add two fictional students with different marks, list all students, view class analytics, search by ID, export the report, then close and reopen the app to verify that records persist.

## Files
- `main.py` — full application
- `README.md` — setup and project details
- `.gitignore` — excludes generated records and reports
- `LINKEDIN_POST.txt` — suggested LinkedIn caption

## GitHub note
Before publishing, use fictional test data and do not commit personal student information from `students.json`.
