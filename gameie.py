import time
import sys

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def start_game():
    # Player ki shuruati conditions
    health = 3
    inventory = []
    intro(health, inventory)

def intro(health, inventory):
    type_effect("\n--- THE TEMPLE OF PYTHON (v2.0) ---", 0.05)
    type_effect(f"❤️ Health: {health}/3 | 🎒 Inventory: {inventory}")
    time.sleep(1)
    type_effect("\nYou wake up in the dark chamber again. But this time, you spot a shiny object on the floor.")
    type_effect("Do you [1] Pick up the Rusty Sword, or [2] Ignore it and go to the doors?")
    
    choice = input("\nYour choice (1 or 2): ")
    if choice == "1":
        inventory.append("Rusty Sword")
        type_effect("\n⚔️ You picked up the Rusty Sword! Added to your inventory.")
    else:
        type_effect("\nYou decided to leave it behind.")

    time.sleep(1)
    type_effect("\nIn front of you are the two heavy wooden doors.")
    type_effect("Door [1]: Leads to the Left (Growling sound).")
    type_effect("Door [2]: Leads to the Right (Silent).")
    
    door_choice = input("\nWhich door? (1 or 2): ")
    if door_choice == "1":
        left_room(health, inventory)
    elif door_choice == "2":
        right_room(health, inventory)
    else:
        type_effect("\nYou wasted time wandering around. Lose 1 Health! ❤️ -> 💔")
        health -= 1
        check_health(health, inventory)

def left_room(health, inventory):
    type_effect("\nYou step into the left room...")
    time.sleep(1)
    type_effect("The giant digital Python snake appears! 🐍")
    
    if "Rusty Sword" in inventory:
        type_effect("\nYour Rusty Sword glows! You scare the snake away with your weapon. No riddle needed!")
        type_effect("Behind the snake is a chest full of diamond code. YOU WIN! 🏆")
    else:
        type_effect("\nYou have no weapon! The snake traps you and snaps: 'Answer my riddle or lose health!'")
        type_effect("'What is 5 + 5 * 0?'")
        answer = input("\nYour answer: ")
        if answer == "5":
            type_effect("\n'Correct!' The snake slithers away. You find a treasure chest. YOU WIN! 🏆")
        else:
            type_effect("\n'WRONG!' The snake bites you! Lose 1 Health. 💔")
            health -= 1
            check_health(health, inventory, "left")

def right_room(health, inventory):
    type_effect("\nYou slip into the silent right room...")
    time.sleep(1)
    type_effect("A robotic laser grid activates! You must hack it or jump through.")
    type_effect("Do you [1] Guess the password 'admin', or [2] Try to jump through the lasers?")
    
    choice = input("\nYour choice (1 or 2): ")
    if choice == "1":
        type_effect("\n'ACCESS GRANTED.' A secret hatch opens to safety! YOU WIN! 🚀")
    elif choice == "2":
        type_effect("\nOuch! The lasers singe your clothes. Lose 1 Health. 💔")
        health -= 1
        check_health(health, inventory, "right")
    else:
        type_effect("\nInvalid choice. The system panics. Lose 1 Health.")
        health -= 1
        check_health(health, inventory, "right")

def check_health(health, inventory, room="intro"):
    if health <= 0:
        type_effect("\n💀 HEALTH DEPLETED. GAME OVER! 💀")
        play_again = input("\nWant to try again? (yes/no): ")
        if play_again.lower() == "yes":
            start_game()
    else:
        type_effect(f"\nYou still have {health} health left. Continuing the adventure...")
        time.sleep(1)
        if room == "left" or room == "right":
            type_effect("\nYou manage to escape back to the main chamber.")
            intro(health, inventory)
        else:
            intro(health, inventory)

if __name__ == "__main__":
    start_game()