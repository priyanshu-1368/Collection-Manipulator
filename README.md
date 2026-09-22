# 🎓 Student Data Organizer

A lightweight, CLI-based Python application to efficiently manage student records. This project demonstrates core CRUD (Create, Read, Update, Delete) operations and practical memory management using Python's fundamental data structures.

## 🚀 Features

* **Add Students:** Register new students with their ID, Name, Age, Grade, DOB, and Subjects.
* **View Records:** Display a beautifully formatted list of all registered students.
* **Smart Update System:** Search students by ID instantly and update specific fields (Name, Age, Grade, DOB, or Subjects) without rewriting the whole record.
* **Delete Records:** Safely remove a student's data from the database using their ID.
* **Unique Subjects Tracker:** Automatically extracts and displays a list of all unique subjects offered across the entire student body.

## 🧠 Data Structures Used

This program is optimized for performance by using the right data structures for the right jobs:
* **`Lists`**: To maintain the chronological order of student entries.
* **`Dictionaries`**: To enable **O(1) fast lookups**, allowing instant access, updates, and deletion by `Student ID`.
* **`Sets`**: To automatically filter out duplicate subjects and maintain a clean list of unique courses offered.

## 🛠️ Usage

1. Make sure you have Python installed on your system (Python 3.x recommended).
2. Clone this repository or download the script.
3. Open your terminal or command prompt.
4. Run the script using the following command:

```bash
python student_data_organizer.py