#!/usr/bin/env python
#Enxhi Merkaj 11/18/2023

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

def perform_task(character, task, required_items, forbidden_debuff):
    print(f"\nAttempting task: {task}")

    # Check if the character has all the required items
    if all(item in character.get_weapons() for item in required_items):
        print("Task requirements met: All items are available.")
    else:
        print("Task failed: Missing required items.")

    # Check if the character has the forbidden debuff
    if forbidden_debuff in character.get_weaknesses():
        print(f"Task failed: Character has the forbidden debuff: {forbidden_debuff}.")
    else:
        print("Task requirements met: Character does not have the forbidden debuff.")

# Create a character instance
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Game tasks
tasks = {
    "Climb a mountain": (["rope", "coat", "first aid kit"], "slow"),
    "Cook a meal": (["pan", "groceries"], "small"),
    "Write a book": (["pen", "paper", "idea"], "confusion")
}

# Perform tasks
for task, (required_items, forbidden_debuff) in tasks.items():
    perform_task(player1, task, required_items, forbidden_debuff)
