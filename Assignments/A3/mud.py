import doctest
import random
from A3.character import make_character, make_character_health


def game():
    """
    Runs the game and all helper functions.
    """
    intro()
    board = make_board()
    character = make_character()
    character_health = make_character_health()
    location = locate(board, character)
    found_exit = False
    while not found_exit:
        board_printer(location, character_health)
        direction = get_user_choice()
        if direction == "quit":
            print("\nYour journey ends here.")
            break
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            location = locate(board, character)
            checkMonster = monster_roll()
            if checkMonster:
                decision = fight_or_flee()
                if decision == "quit":
                    print("\nYour journey ends here.")
                    break
                elif decision == "fight":
                    character_health = combat_round(character_health)
                    if character_health < 1:
                        print("\nYour journey ends here.")
                        break
                elif decision == "flee":
                    character_health -= flee()
            else:
                character_health = heal_char(character_health)


def intro():
    """
    Prints the intro of the game.
    """
    print("A Dust Bunny doesn't have many desires, but you, on the other hand, CRAVE for battle.\nTo satisfy your "
          "craving of destruction and rage, you set off on your adventure in Unduh Da Kaotch.\nExplore the area and "
          "fight unsuspecting dust mites!\nGood luck Dust Bunny!\n\n[At anytime, type 'quit' to quit.]")


def make_board():
    """
    Creates the dungeon as a list.

    :return: A list containing all coordinates.
    """
    coordinates = []
    for i in range(0, 5):
        for j in range(0, 5):
            coordinates.append((i, j))
    return coordinates


def locate(board: list, character: list):
    """
    Creates a dictionary that shows where the character is.

    :param board: a list
    :param character: a list
    :precondition: board and character must both be a list
    :postcondition: a dictionary is given. If character matches any board list values, then assigns the value as True.
    :return: A dictionary where the matching coordinate key's value is True.
    """
    location = {}
    for i in board:
        if character[0] == i[0]:
            if character[1] == i[1]:
                location[i] = True
            else:
                location[i] = False
        else:
            location[i] = False
    return location


def board_printer(location: dict, character_health: int):
    """
    Prints the board and character health. If the value for the key is true, the board displays the character's location.

    :param location: a dict
    :param character_health: an int
    :precondition: location must be a dictionary, character_health must be an int.
    :postcondition: each key is printed and for the key that is assigned True as a value, it prints the character
    :return: printed board displaying character's location & current health
    """
    print("\nCurrent location:")
    for k, j in location:
        if not location[k, j]:
            if j == 4:
                print("[ ]")
            else:
                print("[ ]", end='')
        else:
            if j == 4:
                print("[*]")
            else:
                print("[*]", end='')
    hearts = "♥ " * character_health
    emptyHearts = "♡ " * (10 - character_health)
    print("Health Points [" + str(character_health) + "/10] " + hearts + emptyHearts)


def fight_or_flee():
    """
    Takes user's choice to fight, flee, or quit program.

    :return: a string based on the input.
    """
    invalidChoice = True
    while invalidChoice:
        choice = input("\nYou've found a Dust Mite! (1) Fight or (2) flee?: ")
        if choice == "1":
            return "fight"
        elif choice == "2":
            return "flee"
        elif choice == "quit":
            return "quit"


def flee():
    """
    Flees from the monster. There is a 10% chance of the monster dealing 1-6 damage.

    :return: The amount of damage dealt.
    """
    result = random.randint(1, 10)
    if result == 1:
        damage = random.randint(1, 4)
        print("\nYou got away, but the Dust Mite barely scratches you for " + str(damage) + " damage!")
        return damage
    else:
        print("\nYou got away safely!")
        damage = 0
        return damage


def get_user_choice():
    """
    Asks the user for input on which direction to move in the dungeon.

    :return: the direction as a string.
    """
    check_choice = False
    direction = input("\nWhich way do you want to go? (w) Up (s) Down (a) Left (d) Right: ")
    if direction == "w" or direction == "s" or direction == "a" or direction == "d":
        check_choice = True
    if direction == "quit":
        check_choice = True
    while not check_choice:
        print("\n!!! Invalid choice. !!!")
        direction = input("\n[Type 'quit' to quit.]"
                          "\nWhich way do you want to go? (w, s, a, d): ")
        if direction == "w" or direction == "s" or direction == "a" or direction == "d":
            check_choice = True
    return direction


def validate_move(character: list, direction: str):
    """
    Checks if the given direction is valid, based on the character's current position.

    :param character: a list
    :param direction: a string
    :precondition: character is a list & direction is a string
    :postcondition: calculates if the direction if valid, based on the character's current position.
    :return: True or prints error message depending on input.
    >>> validate_move((0, 0), "s")
    True
    >>> validate_move((0, 0), "w")
    <BLANKLINE>
    !!! Invalid movement !!!
    False
    """
    if direction == "w":
        check = character[0] - 1
    elif direction == "s":
        check = character[0] + 1
    elif direction == "a":
        check = character[1] - 1
    elif direction == "d":
        check = character[1] + 1

    if check < 0 or check > 4:
        print("\n!!! Invalid movement !!!")
        return False
    else:
        return True


def move_character(character: list, direction: str):
    """
    The function updates the character with the direction.

    :param character: a list
    :param direction: a string
    :precondition: character is a list & direction is a string
    :postcondition: updates character depending on direction
    :return: updates character depending on direction
    >>> move_character([0, 0], "s")
    [1, 0]
    >>> move_character([3, 3], "a")
    [3, 2]
    """
    if direction == "w":
        character[0] = character[0] - 1
    elif direction == "s":
        character[0] = character[0] + 1
    elif direction == "a":
        character[1] = character[1] - 1
    elif direction == "d":
        character[1] = character[1] + 1
    return character


def monster_roll():
    """
    Checks if there's a monster. 25% chance of encounter.

    :return: True or False if a monster is found.
    """
    result = random.randint(1,4)
    if result == 1:
        return True
    else:
        return False


def combat_round(character_health: int):
    """
    Runs the combat against a monster. Prints combat results. Updates character's health.

    :param character_health: an int
    :precondition: character_health must be an int.
    :postcondition: combat will process against the monster.
    :return: updates the character's health.
    """
    DustMiteHP = 5
    print("\nYour HP [" + str(character_health) + "/10]")
    print("Dust Mite HP [5/5]")
    whoFirst = random.randint(1,2)
    if whoFirst == 1:
        print("\nYou strike first.")
    else:
        print("\nThe Dust Mite attacks first.")
    while character_health > 0 and DustMiteHP > 0:
        if whoFirst == 1:
            damage = random.randint(1,6)
            DustMiteHP -= damage
            print("You attack the Dust Mite for " + str(damage) + " damage!")
            whoFirst = 2
        else:
            damage = random.randint(1,6)
            character_health -= damage
            print("The Dust Mite hits you for " + str(damage) + " damage!")
            whoFirst = 1
    if DustMiteHP < 1:
        print("\nThe Dust Mite has died!")
    else:
        print("\nYou died :(\nYour HP [0/10]")
    return character_health


def heal_char(character_health: int):
    """
    Heals the character for 2 health to a maximum of 10.

    :param character_health: an int
    :precondition: character_health must be an int
    :postcondition: character_health increases by two, but not greater than 10.
    :return: updated character_health
    >>> heal_char(5)
    7
    >>> heal_char(9)
    10
    """
    character_health += 2
    if character_health > 10:
        character_health = 10
    return character_health


def main():
    """
    Drives the main function.
    """
    game()


if __name__ == "__main__":
    doctest.testmod()
    main()


