class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculate_rank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"ID: {self.student_id}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}, "
                f"Rank: {self.calculate_rank()}")

class College:
    # Parameterized constructor for number of students
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []

    # AddStudent method
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full. Cannot add more students.")

    # GetStudent method (by student ID)
    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return "Student not found."

    # RemoveStudent method (by student ID)
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    # Override __str__ method
    def __str__(self):
        if not self.students:
            return "No students in the college."
        result = "College Students:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result

college = College(2)

s1 = Student(1, "Pratima", 26, 70)
s2 = Student(2, "Trisha", 18, 95)

college.add_student(s1)
college.add_student(s2)

print(college)

print(college.get_student(1))

college.remove_student(1)
print(college)
