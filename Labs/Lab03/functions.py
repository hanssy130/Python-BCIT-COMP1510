import random

def roll_die(number_of_rolls,number_of_sides):
    """
    Return 0 if number of rolls is outside parameters.

    :param number_of_rolls: an int
    :param number_of_sides: an int
    :precondition: Number of rolls should be 1-3.
    :postcondition: Prints 0.
    :return: Print 0 to represent an error if the rolls are beyond precondition, then passes to rolling function.
    """
    if number_of_rolls < 1:
        print(0)
    elif number_of_rolls > 3:
        print(0)
    else:
        rolling(number_of_rolls, number_of_sides)

def rolling(number_of_rolls, number_of_sides):
    """
    Rolls the dice according to # of rolls and # of sides.

    :param number_of_rolls: an int
    :param number_of_sides: an int
    :precondition: variables must be an int
    :postcondition: convert sum int into string
    :return: rolls the dice and returns the total sum.
    """
    number_of_rolls = int(number_of_rolls)
    rollresult = random.randint(1, number_of_sides)
    rollresult2 = 0
    rollresult3 = 0
    if number_of_rolls >= 2:
        rollresult2 = random.randint(1, number_of_sides)
    if number_of_rolls == 3:
        rollresult3 = random.randint(1, number_of_sides)
    print("Total Sum: " + str(rollresult + rollresult2 + rollresult3))

def create_name(length):
    """
    Returns "None" if negative, otherwise prints Error.

    :param length: An int
    :precondition: Length must be between 0 and 5.
    :postcondition: Returns strings if there are errors.
    :return: Returns "Error" statement if outside parameters, otherwise it passes to the nameprinter function.
    """
    if length == 0:
        print("Error, pick a positive number.")
    elif length > 5:
        print("Error, pick a number less than 6.")
    elif length < 0:
        print("None.")
    else:
        nameprinter(length)

def nameprinter(length):
    """
    Generates a random name.

    :param length: an int
    :precondition: Length must be 1-5 characters
    :postcondition: Capitalized string name
    :return: The function returns a randomly generated capitalized string name.
    """
    chr1 = chr(random.randint(97, 122))
    chr2 = " "
    chr3 = " "
    chr4 = " "
    chr5 = " "
    if length >= 2:
        chr2 = chr(random.randint(97, 122))
    if length >= 3:
        chr3 = chr(random.randint(97, 122))
    if length >= 4:
        chr4 = chr(random.randint(97, 122))
    if length == 5:
        chr5 = chr(random.randint(97, 122))
    fullname = chr1 + chr2 + chr3 + chr4 + chr5
    print(fullname.capitalize())

def main():
    """
    Drive the program.
​
    Tests the functions in this module.
    """
    #testing dice. Notice that if the number of sides is 1, then the number of rolls adds up.
    #If the number of rolls is 1, then we can keep testing until we verify the number of sides is correct too.
    roll_die(1,1)
    roll_die(2,1)
    roll_die(3,1)
    roll_die(0,1)
    roll_die(1,2)
    roll_die(4,3)
    create_name(-2)
    create_name(0)
    create_name(1)
    create_name(5)
    create_name(8)

if __name__ == "__main__":
    main()
