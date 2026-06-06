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
    score = 0  # Score system shuru
    intro(health, inventory, score)

def intro(health, inventory, score):
    type_effect(f"\n--- THE TEMPLE OF PYTHON (v4.0 - SCORE UPDATE) ---", 0.05)
    type_effect(f"❤️ Health: {health}/3 | 🎒 Inventory: {inventory} | 🌟 Score: {score}")
    time.sleep(1)
    type_effect("\nYou wake up in the dark chamber. A shiny object on the floor.")
    type_effect("Do you [1] Pick up the Rusty Sword, or [2] Ignore it?")
    
    choice = input("\nYour choice (1 or 2): ")
    if choice == "1":
        inventory.append("Rusty Sword")
        score += 10 # Reward
        type_effect("\n⚔️ Sword picked! (+10 Score)")
    
    type_effect("\nTwo doors ahead. [1] Left, [2] Right.")
    door = input("\nWhich door? (1 or 2): ")
    
    if door == "1":
        left_room(health, inventory, score)
    else:
        right_room(health, inventory, score)

def left_room(health, inventory, score):
    type_effect("\nThe digital Python snake blocks your path! 🐍")
    if "Rusty Sword" in inventory:
        type_effect("\nYou scare the snake! (+20 Score)")
        score += 20
        inventory.append("Golden Key")
        boss_room(health, inventory, score)
    else:
        ans = input("Riddle: 5 + 5 * 0? ")
        if ans == "5":
            score += 30
            type_effect("\nCorrect! (+30 Score)")
            inventory.append("Golden Key")
            boss_room(health, inventory, score)
        else:
            health -= 1
            type_effect("\nWrong! Lose 1 Health.")
            check_health(health, inventory, score, "left")

def right_room(health, inventory, score):
    type_effect("\nLaser grid ahead!")
    choice = input("Guess password 'admin' or [2] Jump? ")
    if choice == "1":
        score += 40
        type_effect("\nACCESS GRANTED! (+40 Score)")
        inventory.append("Golden Key")
        boss_room(health, inventory, score)
    else:
        health -= 1
        type_effect("\nOuch! Lasers burned you. Lose 1 Health.")
        check_health(health, inventory, score, "right")

def boss_room(health, inventory, score):
    type_effect("\n--- BOSS FIGHT: THE ULTIMATE BUG 👾 ---")
    boss_hp = 2
    while boss_hp > 0 and health > 0:
        attack = input(f"\n⚡ HP: {health} | 👾 BOSS HP: {boss_hp} | [1] Patch Code [2] Reboot: ")
        if attack == "1":
            boss_hp -= 1
            score += 50
            type_effect("Patch applied! (+50 Score)")
        else:
            if random.choice([True, False]):
                boss_hp -= 1
                score += 50
                type_effect("Reboot successful! (+50 Score)")
            else:
                health -= 1
                type_effect("Crash! Lose 1 HP.")
    
    if health > 0:
        type_effect(f"\n🏆 VICTORY! Final Score: {score} 🏆")
    else:
        check_health(health, inventory, score)

def check_health(health, inventory, score, room="intro"):
    if health <= 0:
        type_effect(f"\n💀 GAME OVER. Final Score: {score}")
    else:
        intro(health, inventory, score)

if __name__ == "__main__":
    start_game()