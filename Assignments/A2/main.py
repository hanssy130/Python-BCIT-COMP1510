from A2.dungeonsanddragons import combat_round, create_character, choose_inventory, print_character


def main():
    print("\nWelcome to Hans' program!\n\nI'll be demonstrating how my code works.\n\nWhat we're going to do is:\n"
          "1. Create a character\n2. Select items from the shop.\n3. Make him fight against a slime monster!")
    print("\nWe're going to create a character first.")
    print("His name is going to be generated randomly.")
    print("\nMay you please enter the number of syllables desired for your character? ")
    Syllables = int(input("Enter here: "))
    print("\nGreat! Let's continue creating our character.\n")
    Hero = create_character(Syllables)
    print_character(Hero)
    print("\nWow, look at yourself! You're a real gem, aren't ya!")
    print("\nYou can see all of your randomly generated stats, as well as the class & race you picked for yourself.")
    print("\nWhen you're ready, let's head to the Edgar's to equip ourselves.")
    Continue = input("Enter OK to continue: ")
    while Continue.upper() != "OK":
        Continue = input("Enter OK to continue: ")

    Inventory2 = choose_inventory(["Corbite Sword", "Gorgon Shield", "Shadow Daggers", "Slayer Axe", "Tidal Herbs"])
    Hero["Inventory"] = Inventory2
    print_character(Hero)
    if Hero["Inventory"] == []:
        print("\nNo items, but that's fine!")
    else:
        print("\nNice choice! You've got a good eye.")
    print("Looks like you're all ready to fight the slime.\nWhy don't we meet our opponent?\n\n")
    Continue = input("Enter OK to continue: ")
    while Continue.upper() != "OK":
        Continue = input("Enter OK to continue: ")
    LimeTheSlime = {'Name': 'Lime', 'Race': 'Swamp Slime', 'Class': 'Fighter', 'HP': [2, 2], 'Strength': 4, 'Dexterity': 10,
                    'Constitution': 5, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 4, 'XP': 13}
    print_character(LimeTheSlime)
    print("\nIt's Lime the Slime! A common beast, but nothing to be afraid of. Give her a strike, why don't ya!")
    Continue = input("Enter OK to continue: ")
    while Continue.upper() != "OK":
        Continue = input("Enter OK to continue: ")
    combat_round(Hero, LimeTheSlime)

    print("\nThat's all! Thank you for checking out my program.\nIt was a blast to create. Doctests... not so much.")


if __name__=="__main__":
    main()