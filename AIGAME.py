import random

# --- Character Classes ---
classes = {
    "Homeowner": {"Strength": 7, "Agility": 5, "Persuasion": 3},
    "Lawyer": {"Strength": 3, "Agility": 4, "Persuasion": 9},
    "Rebel": {"Strength": 5, "Agility": 8, "Persuasion": 4}
}

# --- Character Creation ---
def create_character():
    print("Choose your class: Homeowner, Lawyer, Rebel")
    choice = input("> ").capitalize()
    if choice in classes:
        stats = classes[choice].copy()
        print(f"You are a {choice} with stats: {stats}")
        return {"Class": choice, "Stats": stats, "HP": 20, "Inventory": []}
    else:
        print("Invalid choice, defaulting to Homeowner.")
        return {"Class": "Homeowner", "Stats": classes["Homeowner"].copy(), "HP": 20, "Inventory": []}

# --- Inventory System ---
def add_item(player, item):
    player["Inventory"].append(item)
    print(f"🎒 You obtained: {item}")

def use_item(player):
    if not player["Inventory"]:
        print("Your inventory is empty!")
        return False
    print("Choose an item to use:")
    for i, item in enumerate(player["Inventory"], 1):
        print(f"{i}. {item}")
    choice = input("> ")
    if choice.isdigit() and 1 <= int(choice) <= len(player["Inventory"]):
        item = player["Inventory"].pop(int(choice) - 1)
        print(f"You used {item}!")
        # Item effects
        if item == "Secret BBQ Sauce":
            boost = random.randint(2, 5)
            print(f"🔥 Persuasion boosted by {boost} for this turn!")
            return ("Persuasion", boost)
        elif item == "Legal Brief":
            print("📚 You defend flawlessly, negating enemy damage this turn!")
            return ("Defend", None)
        elif item == "Sprinkler Malfunction":
            boost = random.randint(2, 5)
            print(f"💦 Agility boosted by {boost} for this turn!")
            return ("Agility", boost)
    else:
        print("Invalid choice.")
    return False

# --- Combat System ---
def combat(player, enemy):
    print(f"A {enemy['Name']} challenges you!")
    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\nYour HP: {player['HP']} | Enemy HP: {enemy['HP']}")
        print("Choose: Argue / Defend / Use Persuasion / Use Item")
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
        elif action == "use item":
            effect = use_item(player)
            if effect:
                if effect[0] == "Persuasion":
                    dmg = random.randint(1, player["Stats"]["Persuasion"] + effect[1])
                    enemy["HP"] -= dmg
                    print(f"Boosted persuasion deals {dmg} damage!")
                elif effect[0] == "Agility":
                    dmg = random.randint(1, player["Stats"]["Agility"] + effect[1])
                    enemy["HP"] -= dmg
                    print(f"Boosted agility deals {dmg} damage!")
                elif effect[0] == "Defend":
                    print("You avoided damage this turn!")
                    continue
        else:
            print("That’s not a valid command.")

        # Enemy counterattack
        if enemy["HP"] > 0:
            dmg = random.randint(1, enemy["Strength"])
            player["HP"] -= dmg
            print(f"The {enemy['Name']} hits you with HOA rules for {dmg} damage!")

    if player["HP"] <= 0:
        print("💀 You have been defeated by the HOA...")
        return False
    else:
        print(f"🎉 You defeated the {enemy['Name']}!")
        return True

# --- Story Stages ---
def stage_one(player):
    print("\n👀 Stage 1: The Nosy Neighbor confronts you at the Neighborhood Watch!")
    if combat(player, {"Name": "Nosy Neighbor", "HP": 10, "Strength": 4}):
        add_item(player, "Secret BBQ Sauce")
        stage_two(player)

def stage_two(player):
    print("\n📋 Stage 2: The HOA President blocks your path at the Board Meeting!")
    if combat(player, {"Name": "HOA President", "HP": 12, "Strength": 5}):
        add_item(player, "Legal Brief")
        stage_three(player)

def stage_three(player):
    print("\n💰 Stage 3: The HOA Treasurer attacks with spreadsheets of doom!")
    if combat(player, {"Name": "HOA Treasurer", "HP": 14, "Strength": 6}):
        add_item(player, "Sprinkler Malfunction")
        final_stage(player)

def final_stage(player):
    print("\n🏠 Final Stage: The HOA Council gathers for the ultimate showdown!")
    if combat(player, {"Name": "HOA Council", "HP": 18, "Strength": 7}):
        print("\n🎉 Victory! You defeated the entire HOA and liberated the neighborhood!")

# --- Main Game Loop ---
def main():
    print("Welcome to the HOA Showdown!")
    player = create_character()
    stage_one(player)

if __name__ == "__main__":
    main()