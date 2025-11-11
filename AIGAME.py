import random  # Import the random module to generate unpredictable outcomes in combat

# --- Character Classes ---
# Define available character classes with their base stats.
# Each class has Strength, Agility, and Persuasion attributes that affect gameplay.
classes = {
    "Homeowner": {"Strength": 7, "Agility": 5, "Persuasion": 3},
    "Lawyer": {"Strength": 3, "Agility": 4, "Persuasion": 9},
    "Rebel": {"Strength": 5, "Agility": 8, "Persuasion": 4}
}

# --- Character Creation ---
def create_character():
    """
    Allows the player to choose a character class.
    If the input is valid, assigns the chosen class and stats.
    If invalid, defaults to Homeowner.
    Returns a dictionary representing the player with class, stats, HP, and inventory.
    """
    print("Choose your class: Homeowner, Lawyer, Rebel")
    choice = input("> ").capitalize()  # Normalize input to match class names
    if choice in classes:
        stats = classes[choice].copy()
        print(f"You are a {choice} with stats: {stats}")
        return {"Class": choice, "Stats": stats, "HP": 20, "Inventory": []}
    else:
        print("Invalid choice, defaulting to Homeowner.")
        return {"Class": "Homeowner", "Stats": classes["Homeowner"].copy(), "HP": 20, "Inventory": []}

# --- World Navigation ---
def hoa_board_meeting(player):
    """
    Represents the HOA Board Meeting location.
    Introduces an enemy encounter with the HOA President.
    """
    print("\n📋 You enter the HOA Board Meeting. The HOA President glares at you!")
    combat(player, {"Name": "HOA President", "HP": 12, "Strength": 5})

def neighborhood_watch(player):
    """
    Represents the Neighborhood Watch location.
    Introduces an enemy encounter with a Nosy Neighbor.
    """
    print("\n👀 You walk into the Neighborhood Watch gathering. A Nosy Neighbor confronts you!")
    combat(player, {"Name": "Nosy Neighbor", "HP": 10, "Strength": 4})

# --- Combat System ---
def combat(player, enemy):
    """
    Handles turn-based combat between the player and an enemy.
    Player can choose to Argue, Defend, or Use Persuasion.
    Enemy attacks automatically if still alive.
    Combat continues until either the player or enemy HP reaches zero.
    """
    print(f"A {enemy['Name']} challenges you!")
    while player["HP"] > 0 and enemy["HP"] > 0:
        # Display current health values
        print(f"\nYour HP: {player['HP']} | Enemy HP: {enemy['HP']}")
        print("Choose: Argue / Defend / Use Persuasion")
        action = input("> ").lower()

        # Player actions
        if action == "argue":
            dmg = random.randint(1, player["Stats"]["Strength"])
            enemy["HP"] -= dmg
            print(f"You argue fiercely, dealing {dmg} damage!")
        elif action == "defend":
            print("You brace yourself, reducing damage.")
            continue
        elif action == "use persuasion":
            dmg = random.randint(1, player["Stats"]["Persuasion"])
            enemy["HP"] -= dmg
            print(f"You make a convincing point, dealing {dmg} damage!")
        else:
            print("That’s not a valid command.")

        # Enemy counterattack if still alive
        if enemy["HP"] > 0:
            dmg = random.randint(1, enemy["Strength"])
            player["HP"] -= dmg
            print(f"The {enemy['Name']} hits you with HOA rules for {dmg} damage!")

    # Outcome of combat
    if player["HP"] <= 0:
        print("💀 You have been defeated by the HOA...")
    else:
        print(f"🎉 You defeated the {enemy['Name']}! The neighborhood breathes easier.")

# --- Main Game Loop ---
def main():
    """
    Entry point of the game.
    Handles character creation and initial world navigation choice.
    """
    print("Welcome to the HOA Showdown!")
    player = create_character()

    # Prompt player to choose a location
    print("\nWhere will you go? HOA Board Meeting or Neighborhood Watch?")
    choice = input("> ").lower()
    if "meeting" in choice:
        hoa_board_meeting(player)
    elif "watch" in choice:
        neighborhood_watch(player)
    else:
        print("You wander aimlessly, and the HOA fines you for loitering. The adventure ends.")

# Run the game if executed directly
if __name__ == "__main__":
    main()