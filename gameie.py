import time
import sys
import random

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def start_game():
    health = 3
    inventory = []
    intro(health, inventory)

def intro(health, inventory):
    type_effect("\n--- THE TEMPLE OF PYTHON (v3.0 - THE BOSS UPDATE) ---", 0.05)
    type_effect(f"❤️ Health: {health}/3 | 🎒 Inventory: {inventory}")
    time.sleep(1)
    type_effect("\nYou wake up in the dark chamber. You spot a shiny object on the floor.")
    type_effect("Do you [1] Pick up the Rusty Sword, or [2] Ignore it and go to the doors?")
    
    choice = input("\nYour choice (1 or 2): ")
    if choice == "1":
        inventory.append("Rusty Sword")
        type_effect("\n⚔️ You picked up the Rusty Sword! This might help against big monsters.")
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
        type_effect("\nYou wasted time. Lose 1 Health! ❤️ -> 💔")
        health -= 1
        check_health(health, inventory)

def left_room(health, inventory):
    type_effect("\nYou step into the left room...")
    time.sleep(1)
    type_effect("The giant digital Python snake appears! 🐍")
    
    if "Rusty Sword" in inventory:
        type_effect("\nYour Rusty Sword glows! You scare the snake away with your weapon.")
        type_effect("The snake leaves behind a heavy 'Golden Key' before slithering away!")
        inventory.append("Golden Key")
        boss_room(health, inventory)
    else:
        type_effect("\nYou have no weapon! The snake traps you and snaps: 'Answer my riddle!'")
        type_effect("'What is 5 + 5 * 0?'")
        answer = input("\nYour answer: ")
        if answer == "5":
            type_effect("\n'Correct!' The snake slithers away and drops a 'Golden Key'.")
            inventory.append("Golden Key")
            boss_room(health, inventory)
        else:
            type_effect("\n'WRONG!' The snake bites you! Lose 1 Health. 💔")
            health -= 1
            check_health(health, inventory, "left")

def right_room(health, inventory):
    type_effect("\nYou slip into the silent right room...")
    time.sleep(1)
    type_effect("A robotic laser grid activates! You see a 'Golden Key' on the other side.")
    type_effect("Do you [1] Guess the password 'admin', or [2] Try to jump through the lasers?")
    
    choice = input("\nYour choice (1 or 2): ")
    if choice == "1":
        type_effect("\n'ACCESS GRANTED.' You safely grab the 'Golden Key'!")
        inventory.append("Golden Key")
        boss_room(health, inventory)
    elif choice == "2":
        type_effect("\nOuch! The lasers singe you. Lose 1 Health. 💔")
        health -= 1
        check_health(health, inventory, "right")
    else:
        type_effect("\nInvalid choice. Lose 1 Health.")
        health -= 1
        check_health(health, inventory, "right")

def boss_room(health, inventory):
    type_effect("\n---------------------------------------------------")
    type_effect("🔒 You approach a massive iron gate. Your Golden Key fits perfectly!")
    type_effect("The gate opens... Welcome to the CHIEF BUG CHAMBER! 👾")
    time.sleep(1)
    type_effect("The Ultimate Bug Monster appears! It has 2 lives and is ready to corrupt your code!")
    
    boss_hp = 2
    while boss_hp > 0 and health > 0:
        type_effect(f"\n⚡ YOUR HEALTH: {health} | 👾 BOSS HEALTH: {boss_hp}")
        type_effect("How do you attack the Bug? [1] Write a Clean Code patch, [2] Force Restart the system")
        
        attack = input("\nYour attack (1 or 2): ")
        if attack == "1":
            type_effect("\n🔥 It's super effective! The Bug loses 1 HP!")
            boss_hp -= 1
        elif attack == "2":
            # 50% chance of success
            if random.choice([True, False]):
                type_effect("\n💥 The system rebooted successfully! The Bug takes heavy damage! -1 HP")
                boss_hp -= 1
            else:
                type_effect("\n❌ The system crashed! The Bug counter-attacks! You lose 1 Health! 💔")
                health -= 1
        else:
            type_effect("\nYou hesitated! The Bug zaps you. Lose 1 Health! 💔")
            health -= 1
            
    if health <= 0:
        check_health(health, inventory)
    elif boss_hp == 0:
        type_effect("\n🏆🏆 CONGRATULATIONS! 🏆🏆")
        type_effect("You defeated THE ULTIMATE BUG and saved your code! YOU WIN THE GAME! 🚀🎉")

def check_health(health, inventory, room="intro"):
    if health <= 0:
        type_effect("\n💀 HEALTH DEPLETED. GAME OVER! 💀")
        play_again = input("\nWant to try again? (yes/no): ")
        if play_again.lower() == "yes":
            start_game()
    else:
        type_effect(f"\nYou still have {health} health left. Continuing...")
        time.sleep(1)
        intro(health, inventory)

if __name__ == "__main__":
    start_game()