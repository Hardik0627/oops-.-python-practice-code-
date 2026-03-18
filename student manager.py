# SMART STUDENT MANAGER (OOP PROJECT)

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(f"\nRoll No: {self.roll}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = list(map(int, input("Enter 3 marks separated by space: ").split()))

        student = Student(roll, name, marks)
        self.students.append(student)
        print("✅ Student Added Successfully!")

    def show_all(self):
        if not self.students:
            print("No students available.")
            return

        for s in self.students:
            s.display()

    def find_topper(self):
        if not self.students:
            print("No data available.")
            return

        topper = max(self.students, key=lambda s: s.average())
        print("\n🏆 Topper Details:")
        topper.display()


# -------- MAIN PROGRAM --------

manager = StudentManager()

while True:
    print("\n===== SMART STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.show_all()
    elif choice == "3":
        manager.find_topper()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")