import doctest
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Rolls the dice according to # of rolls and # of sides.

    :param number_of_rolls: an int
    :param number_of_sides: an int
    :precondition: variables must be a positive int
    :postcondition: convert sum int into string
    :return: rolls the dice and returns the total sum.
    >>> roll_die(0,0) # If you enter 0 as any parameter, it will return 0.
    0
    """
    if number_of_rolls == 0 or number_of_sides == 0:
        return 0
    else:
        roll_result_list = []
        for roll in range(0, number_of_rolls):
            roll_result_list.append(random.randint(1, number_of_sides))
        return sum(roll_result_list)


def generate_vowel():
    """
    Randomly generates a vowel

    :return: a random vowel
    """
    vowel = random.choice(["a", "e", "i", "o", "u", "y"])
    return vowel


def generate_consonant():
    """
    Randomly generates a consonant

    :return: a random consonant
    """
    consonant = random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
                           "x", "y", "z"])
    return consonant


def generate_syllable():
    """
    Combines a random consonant with a random vowel

    :return: a random syllable
    """
    consonant = generate_consonant()
    vowel = generate_vowel()
    return (consonant + vowel)


def generate_name(syllables):
    """
    Generates a string formed up of syllables based on how many inputted.

    :param syllables: an int
    precondition: int must be positive
    postcondition: combines multiple syllables into one string
    :return: a name
    """
    name = ""
    for i in range(0, syllables):
        name = name + generate_syllable()
    return name.capitalize()


def create_character(name_length):
    """
    Creates a random character.

    :param name_length: an int
    :precondition: int must be positive
    :postcondition: uses int to create a name, and randomly creates stats
    :return: A list that includes the generated name and randomly generated stats
    """
    character = {}
    while int(name_length) <= 0:
        name_length = input("Invalid. Enter a positive number.")
    Name = generate_name(int(name_length))
    character["Name"] = Name
    character["Race"] = select_race()
    character["Class"] = select_class()
    HP = Hit_Dice(character["Class"])
    character["HP"] = [HP, HP]
    Stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for i in Stats:
        character[i] = roll_die(3,6)
    character["XP"] = 0
    return character


def Hit_Dice(Class):
    '''
    Returns a random dice roll, based on the class.

    :param Class: a String
    :precondition: Must be passed one of the DnD classes
    :postcondition: Promises to return a roll for the appropriate dice for the class
    :return: A random result from a class' dice
    '''
    if Class == "Barbarian":
        Hit_Value = roll_die(1, 12)
    elif Class == "Fighter" or Class == "Paladin" or Class == "Ranger":
        Hit_Value = roll_die(1, 10)
    elif Class == "Bard" or Class == "Cleric" or Class == "Druid" or Class == "Monk" or Class == "Rogue" or Class == \
            "Warlock":
        Hit_Value = roll_die(1, 8)
    elif Class == "Wizard":
        Hit_Value = roll_die(1, 6)
    return Hit_Value


def select_class():
    '''
    User picks a DnD class

    :return: a Class
    '''
    print("Please choose a class from among the following:")
    Classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
               "Warlock", "Wizard"]
    print(Classes)
    SelectedClass = input("").strip().lower().capitalize()
    while SelectedClass not in Classes:
        SelectedClass = input("Invalid. Please enter a valid class. ").strip().capitalize()
    return SelectedClass


def select_race():
    '''
    User picks a DnD race.

    :return: a race.
    '''
    print("Please choose a race from among the following:")
    Races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Halfling", "Half-orc", "Human", "Tiefling"]
    print(Races)
    SelectedRace = input("").strip().lower().capitalize()
    while SelectedRace not in Races:
        SelectedRace = input("Invalid. Please enter a valid race. ").strip().capitalize()
    return SelectedRace


def print_character(character):
    '''
    Prints a character based on their output
    :param character: Dictionary
    :precondition: Parameter must be a dictionary that includes the user's attributes, created from create_character
    :postocondition: Promises to print user's attributes in a friendly format
    :return: printed list of attributes
    '''
    print("")
    for key, value in character.items():
        if isinstance(value, list):
            if key == "HP":
                print(str(key) + ": ", end='')
                print(*character[key], sep="/")
            if key == "Inventory":
                print(str(key) + ": ", end='')
                print(*character[key], sep=", ")
        else:
            print(str(key) + ": " + str(character[key]))


def choose_inventory(inventory):
    """
    Chooses a selection of items from a given inventory.

    :param inventory: a list
    :param selection: a positive integer
    :precondition: both variables must be positive
    :postcondition: correct calculations
    :return: selects the correct number of inventory into a new list
    """
    print("\nMy guest, welcome to Edgar's Emporium, hey ho!\n\nHere is what we have for sale, oh ho:")
    for i in range(0, len(inventory)):
        print(str(i + 1) + ". " + inventory[i])
    selected = []
    selection = input("\nWhat would you *hic* like to buy? (-1 to finish): ")
    while selection != "-1":
        if selection.isdigit():
            if 0 < int(selection) <= len(inventory):
                selected.append(inventory[int(selection)-1])
                for i in range(0, len(inventory)):
                    print(str(i + 1) + ". " + inventory[i])
                selection = (input(flavourtext()))
            else:
                selection = (input("Invalid. Select an item between 1 and " + str(len(inventory)) + ": "))
        else:
            selection = (input("Invalid. Select an item between 1 and " + str(len(inventory)) + ": "))
    return selected


def flavourtext():
    '''
    Randomly picks a line of flavour text to make the assignment more interest.
    Please try it out as you go through the shop!
    '''
    flavour1 = "Good *hic* choice! Anything else? (-1 to finish): "
    flavour2 = "Coming right up, how about another? (-1 to finish): "
    flavour3 = "I've got it right here. Pick another! (-1 to finish): "
    flavourlist = [flavour1, flavour2, flavour3]
    return random.choice(flavourlist)


def combat_round(opponent_one, opponent_two):
    '''
    Processes the combat using helper functions.

    :param opponent_one: dict
    :param opponent_two: dict
    :precondition: opponents must be established dictionaries with dexterity stats, HP and classes
    :postcondition: runs calculations necessary for the printer
    :return: passes results to combat printer
    '''
    firststrike = first_strike()
    if firststrike[0] > firststrike[1]:
        firstdex = dex_check(opponent_two)
        seconddex = dex_check(opponent_one)
        firstdamage = Hit_Dice(opponent_one["Class"])
        seconddamage = Hit_Dice(opponent_two["Class"])
        combat_printer(opponent_one, opponent_two, firstdex, seconddex, firstdamage, seconddamage)
    else:
        firstdex = dex_check(opponent_one)
        seconddex = dex_check(opponent_two)
        firstdamage = Hit_Dice(opponent_two["Class"])
        seconddamage = Hit_Dice(opponent_one["Class"])
        combat_printer(opponent_two, opponent_one, firstdex, seconddex, firstdamage, seconddamage)


def first_strike():
    '''
    Randomly selects who goes first.

    :return: a list of a lower and higher number, randomly generated.
    '''
    ones_roll = roll_die(1, 20)
    twos_roll = roll_die(1, 20)
    while ones_roll == twos_roll:
        ones_roll = roll_die(1, 20)
        twos_roll = roll_die(1, 20)
    return [ones_roll, twos_roll]


def dex_check(defender):
    '''
    Checks if the attack lands.

    :param defender: dictionary
    :precondition: must have the key, Dexterity, in the dict
    :postcondition: promises to use it for calculating if the attack lands
    :return: 1 or 0, depending on if the roll is higher than the parameter's dexterity
    '''
    attack_roll = roll_die(1, 20)
    if attack_roll > defender["Dexterity"]:
        return 1
    else:
        return 0


def combat_printer(player1, player2, firstdex, seconddex, firstdamage, seconddamage):
    '''
    Prints the results of combat.

    :param player1: dict
    :param player2: dict
    :param firstdex: int
    :param seconddex: int
    :param firstdamage: int
    :param seconddamage: int
    :precondition: dict must have the key "HP", dex must be int to tell if attack landed, damage must be in to print damage inflicted
    :postcondition: proises to deliver print statements for death, damage inflicted, and missing
    :return: Printed summary of combat
    '''
    print("---FIGHT!---")
    print(player1["Name"] + " goes first!")
    if firstdex == 1:
        player2["HP"][1] = player2["HP"][1] - firstdamage
        print(player1["Name"] + " inflicts " + str(firstdamage) + "!")
        if player2["HP"][1] <= 0:
            print(player2["Name"] + " has been slain!")
        else:
            if seconddex == 1:
                player1["HP"][1] = player1["HP"][1] - seconddamage
                print(player2["Name"] + " inflicts " + str(seconddamage) + "!")
                if player1["HP"][1] <= 0:
                    print(player1["Name"] + " has been slain!")
            else:
                print(player2["Name"] + " missed!")
    else:
        print(player1["Name"] + " missed!")
        if seconddex == 1:
            player1["HP"][1] = player1["HP"][1] - seconddamage
            print(player2["Name"] + " inflicts " + str(seconddamage) + "!")
            if player1["HP"][1] <= 0:
                print(player1["Name"] + " has been slain!")
        else:
            print(player2["Name"] + " missed!")


def main():
    """
    Drives the main function. Takes the user through an adventure.
    """
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
    doctest.testmod()
