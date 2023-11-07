import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    time.sleep(2)
    print("You find yourself standing at the entrance of a dense forest.")
    time.sleep(2)
    print("Your mission is to find the hidden treasure deep within the forest.")
    time.sleep(2)

def choose_path():
    choice = input("Do you want to go 'left' or 'right'? ").lower()
    if choice == "left":
        return "left_path"
    elif choice == "right":
        return "right_path"
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        return choose_path()

def left_path():
    print("You chose to go left and encounter a river.")
    time.sleep(2)
    print("You have two options: 'swim' across the river or 'build a bridge'.")
    choice = input("What will you do? ").lower()
    if choice == "swim":
        print("You tried to swim but got caught in a strong current. Game Over!")
    elif choice == "build a bridge":
        print("You build a bridge and safely cross the river.")
        time.sleep(2)
        print("You continue your journey deeper into the forest.")
        time.sleep(2)
        return "forest_path"
    else:
        print("Invalid choice. Please enter 'swim' or 'build a bridge'.")
        return left_path()

def right_path():
    print("You chose to go right and find a hidden cave entrance.")
    time.sleep(2)
    print("You enter the cave, and it leads you to a treasure chest!")
    time.sleep(2)
    print("Congratulations! You found the hidden treasure!")
    return "win"

def forest_path():
    print("You are deep in the forest, and you find two doors.")
    time.sleep(2)
    print("One door is 'red,' and the other door is 'blue.'")
    choice = input("Which door will you choose? ").lower()
    if choice == "red":
        print("You open the red door and find a dragon. Game Over!")
    elif choice == "blue":
        print("You open the blue door and discover more treasure!")
        time.sleep(2)
        print("Congratulations! You found even more treasure!")
        return "win"
    else:
        print("Invalid choice. Please enter 'red' or 'blue'.")
        return forest_path()

def main():
    introduction()
    path = choose_path()
    while path != "win":
        if path == "left_path":
            path = left_path()
        elif path == "right_path":
            path = right_path()
        elif path == "forest_path":
            path = forest_path()
    print("Thanks for playing the Mysterious Forest Adventure!")

if __name__ == "__main__":
    main()
