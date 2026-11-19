# Digital Diary / Notes Manager

## Project Information
- **Project Number:** PS No. 38
- **Project Title:** Digital Diary / Notes Manager
- **Language:** Python 3
- **Application Type:** Console-Based Application
- **Storage:** Text File Handling

## 1. Project Description
The Digital Diary / Notes Manager is a console-based Python application that allows users to create, view, search and delete personal diary notes.

Each note contains a date and text. All notes are stored in a text file so that the information remains available even after the program is closed.

## 2. Features
- Add new notes with dates.
- View all saved notes.
- Search notes using keywords.
- Case-insensitive keyword searching.
- Delete notes using their assigned numbers.
- Validate date formats.
- Prevent empty notes.
- Handle invalid inputs.
- Automatically number notes starting from 1.

## 3. Technologies Used
- Python 3
- File Handling
- String Manipulation
- Functions
- Loops and Conditional Statements
- Exception Handling
- Datetime Module

## 4. Project Structure
- Codebase/ — Contains the Python source code and generated diary file.
- Testcases/ — Contains screenshots of the program's test-case outputs.
- README.md — Project documentation.
- .gitignore — Specifies files Git should ignore.

## 5. How to Run
1. Install Python 3.
2. Download or clone the repository.
3. Open the Codebase folder in the terminal.
4. Run the following command:

`python digital_diary.py`

## 6. Menu Options
1. Add Note
2. View All Notes
3. Search Notes
4. Delete Note
5. Exit

## 7. Data Storage
All diary entries are stored in `diary.txt`.

Each entry follows this format:

`YYYY-MM-DD|Note Text`

## 8. Testing
The project is tested using four test scenarios:
- TC1: Normal Input
- TC2: Boundary / Minimum Input
- TC3: Invalid Input
- TC4: Different Valid Scenario

## 9. Conclusion
The Digital Diary / Notes Manager demonstrates the practical use of Python fundamentals, functions, string operations, file handling and exception handling in developing a simple console-based application.
