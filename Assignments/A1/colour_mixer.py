def colour_mixer(primary1, primary2):
    """
    Combines 2 primary colours into 1 secondary colour.

    :param primary1: str
    :param primary2: str
    :precondition: The strings must be either red, blue, or yellow.
    :postcondition: A secondary colour or error response will be created.
    :return: Print a secondary colour or error message.

    >>> colour_mixer("red", "red") #tested same colour
    They're the same colour. DON'T ENTER THE SAME COLOUR.
    >>> colour_mixer("blue", "yellow") #tested colour combination
    Green
    >>> colour_mixer("dog", "cat") #tested non-colours
    Please enter either Red, Blue, or Yellow.
    """
    if primary1 == "red" and primary2 == "red" or primary1 == "blue" and primary2 == "blue" or primary1 == "yellow" and \
            primary2 == "yellow":
        print("They're the same colour. DON'T ENTER THE SAME COLOUR.")
    elif primary1 == "red" and primary2 == "blue" or primary1 == "blue" and primary2 == "red":
        print("Purple")
    elif primary1 == "blue" and primary2 == "yellow" or primary1 == "yellow" and primary2 == "blue":
        print("Green")
    elif primary1 == "red" and primary2 == "yellow" or primary1 == "yellow" and primary2 == "red":
        print("Orange")
    else:
        print("Please enter either Red, Blue, or Yellow.")


def main():
    """
    Drives the main function.
    """
    primary1 = input("Please enter the first primary colour: ").strip().lower()
    primary2 = input("Please enter the second primary colour: ").strip().lower()
    colour_mixer(primary1, primary2)


if __name__ == "__main__":
    main()

"""
decomposition: No decomposition was used as I took two inputs right away to calculate the new colour.
patternmatching: Blue and Yellow make green, and vice versa. Other primary colours ahve their own combo.
abstraction: I checked if they share the same colour first.
algorithm: Function checks if either colour is present in a combination. Algorithm solves for the secondary colour
assuming the correct primary colours are given.
"""