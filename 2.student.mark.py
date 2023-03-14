class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            student_id = input("Enter the student ID: ")
            student_name = input("Enter the student name: ")
            student_dob = input("Enter the student date of birth ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_grades(self):
        course_id = input("Enter the course ID: ")
        course = self.course_checking(course_id)
        if not course:
            print("Invalid course ID")
            return
        for student in self.students:
            grade = input(f"Enter the grade for student {student.name} (NO GRADE LEAVE BLANK): ")
            if grade:
                course.students[student.id] = grade
                student.courses[course_id] = grade

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"{course.id}: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"{student.id}: {student.name}")

    def show_grades(self):
        course_id = input("Enter the course ID: ")
        course = self.course_checking(course_id)
        if not course:
            print("Invalid course ID")
            return
        print(f"Grades for course {course.name}:")
        for student_id, grade in course.students.items():
            student = self.student_checking(student_id)
            if not student:
                print(f"Unknown student ID {student_id}")
                continue
            print(f"{student.name}: {grade}")

    def course_checking(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def student_checking(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def execute(self):
        self.input_students()
        self.input_courses()
        while True:
            print()
            print("CHoose:")
            print("1. Input grades")
            print("2. List courses")
            print("3. List students")
            print("4. Show grades")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_grades()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_grades()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

if __name__ == '__main__':
    school = School()
    school.execute()
