# Smart Study Planner using OOP

class Task:
    def __init__(self, title, subject, priority):
        self.title = title
        self.subject = subject
        self.priority = priority
        self.completed = False

    def mark_done(self):
        self.completed = True

    def display(self, index):
        status = "✅ Done" if self.completed else "⏳ Pending"
        print(f"{index}. {self.title} | {self.subject} | Priority: {self.priority} | {status}")


class StudyPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        subject = input("Enter subject: ")
        priority = input("Priority (High/Medium/Low): ")
        task = Task(title, subject, priority)
        self.tasks.append(task)
        print("✅ Task Added Successfully!\n")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\n📚 Your Study Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            task.display(i)
        print()

    def complete_task(self):
        self.show_tasks()
        if self.tasks:
            num = int(input("Enter task number to mark complete: "))
            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1].mark_done()
                print("🎉 Task Completed!\n")
            else:
                print("Invalid number!\n")

    def progress(self):
        if not self.tasks:
            print("No tasks yet.\n")
            return

        done = sum(task.completed for task in self.tasks)
        total = len(self.tasks)
        print(f"📊 Progress: {done}/{total} tasks completed\n")


# Main Program
planner = StudyPlanner()

while True:
    print("====== SMART STUDY PLANNER ======")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. View Progress")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        planner.add_task()
    elif choice == "2":
        planner.show_tasks()
    elif choice == "3":
        planner.complete_task()
    elif choice == "4":
        planner.progress()
    elif choice == "5":
        print("Good luck with your studies! 🚀")
        break
    else:
        print("Invalid choice!\n")