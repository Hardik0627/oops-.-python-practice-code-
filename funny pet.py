# Funny Robot Pet using OOP

class RobotPet:
    
    def __init__(self, name):
        self.name = name
        self.energy = 50

    def eat(self):
        self.energy += 10
        print(self.name, "ate pizza 🍕 and gained energy!")

    def sleep(self):
        self.energy += 20
        print(self.name, "is sleeping... 😴")

    def talk(self):
        print(self.name, "says: I need WiFi not water 🤖")

    def status(self):
        print("Energy Level:", self.energy)


# Main Program
pet = RobotPet("Robo")

while True:
    print("\n1.Eat  2.Sleep  3.Talk  4.Status  5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        pet.eat()
    elif choice == "2":
        pet.sleep()
    elif choice == "3":
        pet.talk()
    elif choice == "4":
        pet.status()
    elif choice == "5":
        print("Robot shutting down... Bye 😂")
        break
    else:
        print("Robot confused 😵")