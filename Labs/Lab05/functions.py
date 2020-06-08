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
    Generates a string formed up of syllables based on how many inputted

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
    Name = generate_name(name_length)
    STR = ["Strength", roll_die(3,6)]
    DEX = ["Dexterity", roll_die(3,6)]
    CON = ["Constitution", roll_die(3,6)]
    INT = ["Intelligence", roll_die(3,6)]
    WIS = ["Wisdom", roll_die(3,6)]
    CHA = ["Charisma", roll_die(3,6)]
    character = [Name, STR, DEX, CON, INT, WIS, CHA]
    return character


def print_character(character):
    """
    Prints the character's information.

    :param character: a list
    :precondition: List must have the character's name first, then the attributes
    :postcondition: Prints the character in a nice format
    :return: Prints the character's information
    """
    print("Adventurer: " + (character[0]))
    STR = character[1]
    print(STR[0] + ": " + str(STR[1]))
    DEX = character[2]
    print(DEX[0] + ": " + str(DEX[1]))
    CON = character[3]
    print(CON[0] + ": " + str(CON[1]))
    INT = character[4]
    print(INT[0] + ": " + str(INT[1]))
    WIS = character[5]
    print(WIS[0] + ": " + str(WIS[1]))
    CHA = character[6]
    print(CHA[0] + ": " + str(CHA[1]))


def choose_inventory(inventory, selection):
    """
    Chooses a selection of items from a given inventory.

    :param inventory: a list
    :param selection: a positive integer
    :precondition: both variables must be positive
    :postcondition: correct calculations
    :return: selects the correct number of inventory into a new list
    """
    if len(inventory) == 0 and selection == 0:
        return inventory
    elif selection < 0:
        print("Selection cannot be negative!")
        return []
    elif selection > len(inventory):
        print("Selection is larger than inventory size. Unable to select that many items.")
        return sorted(inventory[:])
    elif selection == len(inventory):
        return sorted(inventory[:])
    else:
        selected = []
        for i in range(0, selection):
            chosen = random.choice(inventory)
            selected.append(chosen)
        return sorted(selected)
