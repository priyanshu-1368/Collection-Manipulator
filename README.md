# Student Data Organizer

A CLI-based Python application designed to manage student records, track subject enrollments, and support full CRUD operations with data integrity checks and runtime error handling.

---

## Features

* **Add Student:** Register students with unique IDs, demographics, and a custom list of subjects.
* **Display All Records:** Structured tabular output for viewing all active student profiles.
* **Update Records:** Field-level modification (Name, Age, Grade, DOB, and Subjects) by Student ID.
* **Delete Record:** Instant record removal across dictionary and list data structures.
* **Subjects Directory:** Dynamic set aggregation displaying distinct subjects offered across active enrollments.
* **Fault-Tolerant CLI:** Input validation guards against invalid data types and missing lookup keys.

---

## Preview

![Add Student](Screenshots/img1.png)
![Display All Students](Screenshots/img2.png)
![Delete Student](Screenshots/img3.png)

---

## Output

```
==================================================
     Welcome to the Student Data Organizer!
==================================================

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice (1-6): 1

==================================================
              --- Add Student ---
==================================================

Enter student details:
Student ID: 101
Name: Rahul Sharma
Age: 20
Grade: A
Date of Birth (YYYY-MM-DD): 2004-05-15
Subjects (comma-separated): Math, Physics, Computer Science

Student added successfully!

==================================================

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice (1-6): 2

==================================================
          --- Display All Students ---
--------------------------------------------------
Student ID: 101 | Name: Rahul Sharma | Date of Birth: 2004-05-15 | Age: 20 | Grade: A | Subjects: Math, Physics, Computer Science
==================================================

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice (1-6): 3

==================================================
        --- Update Student Information ---
==================================================

Enter the Student ID to update: 101

Student Found
Student ID: 101
Student Name: Rahul Sharma

What would you like to update?
1. Name
2. Age
3. Grade
4. Date of Birth
5. Subjects
6. Cancel

Enter your choice (1-6): 3
Enter new grade: A+

Student's grade updated successfully!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice (1-6): 6

==================================================
Exiting the Student Data Organizer. Goodbye!

==================================================
```

