"""
Daily OOP Task: Course Registration System

Concepts:
- Classes and objects
- Constructors
- Encapsulation
- Instance methods
- Object interaction
- Input validation
"""


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"Student ID: {self.student_id} | Name: {self.name}")


class Course:
    def __init__(self, course_name, instructor, capacity):
        self.course_name = course_name
        self.instructor = instructor
        self.capacity = capacity
        self.__students = []

    def enroll_student(self, student):
        for enrolled_student in self.__students:
            if enrolled_student.student_id == student.student_id:
                print(f"{student.name} is already enrolled.")
                return

        if len(self.__students) >= self.capacity:
            print(f"Sorry! {self.course_name} is full.")
            return

        self.__students.append(student)
        print(f"{student.name} enrolled successfully in {self.course_name}.")

    def remove_student(self, student_id):
        for student in self.__students:
            if student.student_id == student_id:
                self.__students.remove(student)
                print(f"{student.name} has been removed from the course.")
                return

        print("Student ID not found in this course.")

    def show_course_details(self):
        print("\n========== COURSE DETAILS ==========")
        print(f"Course: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Available seats: {self.capacity - len(self.__students)}")
        print(f"Enrolled students: {len(self.__students)}")

        if not self.__students:
            print("No students enrolled yet.")
        else:
            print("\nStudent List:")
            for student in self.__students:
                student.display()


if __name__ == "__main__":
    python_course = Course("Python Full Stack", "Mr. Sharma", 3)

    student1 = Student(101, "Aarav")
    student2 = Student(102, "Priya")
    student3 = Student(103, "Rohan")
    student4 = Student(104, "Meera")

    python_course.enroll_student(student1)
    python_course.enroll_student(student2)
    python_course.enroll_student(student3)
    python_course.enroll_student(student1)  # Duplicate check
    python_course.enroll_student(student4)  # Capacity check

    python_course.show_course_details()

    python_course.remove_student(102)
    python_course.enroll_student(student4)

    python_course.show_course_details()
