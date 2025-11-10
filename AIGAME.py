import random
# --- Character Classes ---
classes = {
    "Warrior": {"Strength": 8, "Agility": 5, "Magic": 2},
    "Mage": {"Strength": 3, "Agility": 4, "Magic": 9},
    "Rogue": {"Strength": 5, "Agility": 8, "Magic": 3}
}

# --- Character Creation ---
def create_character():
    print("Choose your class: Warrior, Mage, Rogue")
    choice = input("> ").capitalize()
    if choice in classes:
        stats = classes[choice].copy()
        print(f"You are a {choice} with stats: {stats}")
        return {"Class": choice, "Stats": stats, "HP": 20, "Inventory": []}
    else:
        print("Invalid choice, defaulting to Warrior.")
        return {"Class": "Warrior", "Stats": classes["Warrior"].copy(), "HP": 20, "Inventory": []}

# --- World Navigation ---
def haunted_forest(player):
    print("\n🌲 You enter the Haunted Forest. A shadowy wolf appears!")
    combat(player, {"Name": "Shadow Wolf", "HP": 10, "Strength": 4})

def enchanted_castle(player):
    print("\n🏰 You arrive at the Enchanted Castle. A guard blocks your path!")
    combat(player, {"Name": "Castle Guard", "HP": 12, "Strength": 5})

# --- Combat System ---
def combat(player, enemy):
    print(f"A {enemy['Name']} challenges you!")
    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\nYour HP: {player['HP']} | Enemy HP: {enemy['HP']}")
        print("Choose: Attack / Defend / Use Magic")
        action = input("> ").lower()

        if action == "attack":
            dmg = random.randint(1, player["Stats"]["Strength"])
            enemy["HP"] -= dmg
            print(f"You strike for {dmg} damage!")
        elif action == "defend":
            print("You brace yourself, reducing damage.")
            continue
        elif action == "use magic":
            dmg = random.randint(1, player["Stats"]["Magic"])
            enemy["HP"] -= dmg
            print(f"You cast a spell for {dmg} damage!")
        else:
            print("That’s not a valid command.")

        if enemy["HP"] > 0:
            dmg = random.randint(1, enemy["Strength"])
            player["HP"] -= dmg
            print(f"The {enemy['Name']} hits you for {dmg} damage!")

    if player["HP"] <= 0:
        print("💀 You have been defeated...")
    else:
        print(f"🎉 You defeated the {enemy['Name']}!")

# --- Main Game Loop ---
def main():
    print("Welcome to the AI-Generated Adventure!")
    player = create_character()

    print("\nWhere will you go? Haunted Forest or Enchanted Castle?")
    choice = input("> ").lower()
    if "forest" in choice:
        haunted_forest(player)
    elif "castle" in choice:
        enchanted_castle(player)
    else:
        print("You wander aimlessly and the adventure ends.")

if __name__ == "__main__":
    main()