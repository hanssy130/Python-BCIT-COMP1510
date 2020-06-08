import doctest


def game():
    """
    Runs the game and all helper functions.
    """
    board = make_board()
    character = make_character()
    location = locate(board, character)
    found_exit = False
    while not found_exit:
        board_printer(location)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            location = locate(board, character)
        if character == [4, 4]:
            found_exit = True
    board_printer(location)
    print("\nYou've won, you found the exit!")


def make_board():
    """
    Creates the board as a list.

    :return: A list containing all coordinates.
    """
    coordinates = []
    for i in range(0, 5):
        for j in range(0, 5):
            coordinates.append((i, j))
    return coordinates


def make_character():
    """
    Creates the character at the starting position.

    :return: The starting position at [0, 0].
    """
    return [0, 0]


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


def board_printer(location: dict):
    """
    Prints the board. If the value for the key is true, the board displays the character's location.

    :param location: a dict
    :precondition: location must be a dictionary
    :postcondition: each key is printed and for the key that is assigned True as a value, it prints the character
    :return: printed board displaying character's location.
    """
    print("\nYou are currently here:")
    for k, j in location:
        if not location[k, j]:
            if j == 4:
                print("[ ]")
            else:
                print("[ ]", end='')
        else:
            if j == 4:
                print("[X]")
            else:
                print("[X]", end='')


def get_user_choice():
    """
    Asks the user for input on which direction.

    :return: the direction as a string.
    """
    check_choice = False
    direction = input("Which way do you want to go? (w, s, a, d): ")
    if direction == "w" or direction == "s" or direction == "a" or direction == "d":
        check_choice = True
    while not check_choice:
        print("\n!!! Invalid choice. !!!")
        direction = input("\nWhich way do you want to go? (w, s, a, d): ")
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


def main():
    """
    Drives the main function.
    """
    game()


if __name__ == "__main__":
    doctest.testmod()
    main()

