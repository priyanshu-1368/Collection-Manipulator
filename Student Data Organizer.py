student_list = []
student_by_id = {}
subject_set = set()

print("=" * 50)
print("     Welcome to the Student Data Organizer!")
print("=" * 50)

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = int(input("\nEnter your choice (1-6): "))
    
    print("\n" + "=" * 50)

    if choice == 1:
        print("              --- Add Student ---")
        print("=" * 50)
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
        subjects = [subject.strip() for subject in subjects]

        identity = (student_id, name)

        student = {
            "Student ID"    :    student_id,
            "Name"          :    name,
            "Age"           :    age,
            "Grade"         :    grade,
            "Date of Birth" :    dob,
            "Subjects"      :    subjects
        }

        student_list.append(student)
        student_by_id[student_id] = student
        subject_set.update(subjects)

        print("\nStudent added successfully!")
        print("\n" + "=" * 50)

    elif choice == 2:
        if student_list:
            print("           --- Display All Students ---")
            print("-" * 50)
            for student in student_list:
                subjects_str = ", ".join(student["Subjects"])
                print(f"Student ID: {student['Student ID']} | Name: {student['Name']} | Date of Birth: {student['Date of Birth']} | Age: {student['Age']} | Grade: {student['Grade']} | Subjects: {subjects_str}")
        else:
            print("              --- No data found ---")

        print("=" * 50)

    elif choice == 3:
        if student_list:
            print("        --- Update Student Information ---")
            print("=" * 50)
            var = student_by_id[student_id]
            student_id_inpt = input("\nEnter the Student ID to update: ")

            if student_id_inpt.isdigit():
                student_id = int(student_id_inpt)

                if student_id in student_by_id:
                    print("\nStudent Found")
                    print(f"Student ID: {var['Student ID']}")
                    print(f"Student Name: {var['Name']}")
                    print("\nWhat would you like to update?")
                    print("1. Name")
                    print("2. Age")
                    print("3. Grade")
                    print("4. Date of Birth")
                    print("5. Subjects")
                    print("6. Cancel")

                    update_choice = int(input("\nEnter your choice (1-6): "))

                    if update_choice == 1:
                        new_name = input("Enter new name: ")
                        var['Name'] = new_name
                        print("\nStudent's name updated successfully!")
                    elif update_choice == 2:
                        new_age = int(input("Enter new age: "))
                        var['Age'] = new_age
                        print("\nStudent's age updated successfully!")
                    elif update_choice == 3:
                        new_grade = input("Enter new grade: ")
                        var['Grade'] = new_grade
                        print("\nStudent's grade updated successfully!")
                    elif update_choice == 4:
                        new_dob = input("Enter new date of birth: ")
                        var['Date of Birth'] = new_dob
                        print("\nStudent's  date of birth updated successfully!")
                    elif update_choice == 5:
                        new_subjects = input("Enter new subjects (comma-separated): ").split(",")
                        var['Subjects'] = [subject.strip() for subject in new_subjects]
                        print("\nStudent's subjects updated successfully!")
                    elif update_choice == 6:
                        print("\nUpdate cancelled.")
                    else:
                        print("\nInvalid choice. Please select a valid option (1-6).")
            else:
                print(f"\nStudent with ID {student_id} not found.")
        else:
            print("              --- No data found ---")
            print("=" * 50)

    elif choice == 4:
        if student_list:
            print("             --- Delete Student ---")
            print("=" * 50)
            student_id = int(input("\nEnter the Student ID to delete: "))
            if student_id in student_by_id:
                student_list.remove(student_by_id[student_id])
                del student_by_id[student_id]
                print(f"\nStudent with ID {student_id} has been deleted successfully.")
            else:
                print(f"\nStudent with ID {student_id} not found.")
        else:
            print("              --- No data found ---")
            print("=" * 50)

    elif choice == 5:
        if student_list:
            print("        --- Display Subjects Offered ---")
            print("-" * 50)
            for subject in subject_set:
                print("-", subject)
        else:
            print("              --- No data found ---")
            print("=" * 50)

        print("=" * 50)

    elif choice == 6:
        print("Exiting the Student Data Organizer. Goodbye!")
        print("\n" + "=" * 50)
        break

    else:
        print("\nInvalid choice. Please select a valid option (1-6).")
        print("\n" + "=" * 50)