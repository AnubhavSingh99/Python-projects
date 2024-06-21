import random
class player:
    def __init__(self,fuel,position,resources):
        self.fuel = 100
        self.position = (0,0) #galaxy,planet
        self.resources = 20
    def generate_position(self):
        self.galaxy = random.randint
        self.planet = random.randint

    def move(self):
        if self.fuel > 0:
            self.fuel -= 10
            self.galaxy = random.randint(0,100)
            self.planet = random.randint(0,100)
            a=self.galaxy
            b=self.planet
            self.position = (a,b)
            print("You have moved to",self.position)
            self.randomevent()
        else:
            print("Not enough fuel")
    def randomevent(self):
        event = random.randint(1,3)
        if event == 1:
            self.resources += 10
            print("You found resources")
        elif event == 2:
            self.fuel += 10
            print("You found fuel")
        else:
            self.fuel -= 10
            print("You lost fuel")    
    def actions(self):
        print("1. Move")
        print("2. Mine")
        print("3. Refuel")
        print("4. Quit")
        action = input("Choose an action: ")
        if action == "1":
            self.move()
        elif action == "2":
            self.resources += 10
            print("You found resources")
        elif action == "3":
            self.resources -= 10
            self.fuel+=10
            print("You refueled")
        elif action == "4":
            quit()
        else:
            print("Invalid choice")
    def status(self):
        print("Fuel:",self.fuel)
        print("Position:",self.position)
        print("Resources:",self.resources)
def main():
    player1 = player(100,(0,0),20)
    print("=== Main Menu ===")
    print("1. Start Game")
    print("2. Show Status")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        player1.actions()
    elif choice == "2":
        player1.status()
    elif choice == "3":
        quit()
    else:
        print("Invalid choice")

while True:
    main()
    