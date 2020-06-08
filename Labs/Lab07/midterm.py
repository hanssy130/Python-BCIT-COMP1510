import doctest
import random


def list_tagger(batch):
    """
    Adds the length of list to the front of the list.

    :param batch: a list
    :precondition: batch is a list
    :postcondition: insert the length at the first index
    :return: prepends the length of the list to the front
    >>> list_tagger([1, 2, 3])
    [3, 1, 2, 3]
    >>> list_tagger([])
    [0]
    """
    batch.insert(0, len(batch))
    return batch


def cutoff(intlist, multiple):
    """
    Returns a count of the number of integers in given list that are a multiple of a given number.

    :param intlist: a list
    :param multiple: a positive integer
    :precondition: intlist is a list and multiple is an integer greater than 0
    :postcondition: counts the number of list items whose remainder when divided by the integer is 0
    :return: counts the number of integers in list that are multiples
    >>> cutoff([3,6,10],3)
    2
    """
    if multiple == 0:
        return 0
    counter = 0
    for value in intlist:
        if value == 0:
            counter += 0
        elif value % multiple == 0:
            counter += 1
    return counter


def prepender(stringlist, extrastring):
    """
    Modifies the list by prepending a string to the front of each item in a list.

    :param stringlist: a list of strings
    :param extrastring: a string
    :precondition: stringlist must be a list of strings. extrastring must be a string.
    :postcondition: extrastring will be prepended in front of every string in stringlist.
    :return: does not return anything
    """
    for i in range(0, len(stringlist)):
        stringlist[i] = extrastring + stringlist[i]


def name_list():
    """
    Asks the user to enter names. Creates a dictionary based on the length of the name.

    :return: Returns a dictionary based on how many characters for every name entered.
    """
    namedict = {}
    name = input("Enter a name(type 'quit' to exit): ")
    while name != "quit":
        if name == "quit":
            break
        namelength = len(list(name))
        if namelength not in namedict:
            namedict[namelength] = name
        else:
            addname = [namedict[namelength]]
            addname.append(name)
            namedict[namelength] = addname
        name = input("Enter a name(type 'quit' to exit): ")
    return namedict


def multiples_of_3(upper_bound):
    """
    Sums the positive multiples of 3 below a given upper bound.

    :param upper_bound: an int
    :precondition: upper_bound must be greater than 1.
    :postcondition: adds all of the multiples of 3 between 1 and the upper_bound
    :return: returns the sum of positive multiples of 3 between 1 and the upper_bound
    >>> multiples_of_3(10)
    18
    """
    sum = 0
    for threes in range(0, upper_bound, 3):
        sum += threes
    return sum


def dice_input():
    """
    User is asked for the number of dice rolls and sides on a dice. Dice is rolled.

    :precondition: User must enter integer.
    :postcondition: Dices are rolled and passed to the interpreter.
    :return: A list of dice roll results and the number of sides to the interpreter.
    """
    x = int(input("How many times do you want to roll your dice? "))
    y = int(input("How many sides does your dice have? "))
    dice = [x, y]
    if x == 1:
        print(f"You are rolling a {dice[1]}-sided dice {dice[0]} time!")
    else:
        print(f"You are rolling a {dice[1]}-sided dice {dice[0]} times!")
    count = 0
    resultlist = []
    while count < dice[0]:
        result = random.randint(1, dice[1])
        resultlist.append(result)
        count += 1
    resultdict([resultlist, dice[1]])


def resultdict(resultlistandsides):
    """
    Prints the results of how many times each side of a dice is rolled.

    :param resultlistandsides: a list
    :precondition: resultslistandsides must be a list that contains the results and the number of sides of the dice.
    :postcondition: prints the results of which sides were rolled how many times.
    :return: prints the results of which sides were rolled how many times.
    """
    resultlist = resultlistandsides[0]
    resultsides = resultlistandsides[1]
    resultdict = {}
    for x in range(1, resultsides + 1):
        resultdict[x] = 0
    for value in resultlist:
        if value in resultdict:
            resultdict[value] += 1
    for key in resultdict:
        if resultdict[key] == 0:
            print(f"You never rolled a {key}.")
        elif resultdict[key] == 1:
            print(f"The times you rolled a {key} is {resultdict[key]} time!")
        else:
            print(f"The times you rolled a {key} is {resultdict[key]} times!")


def main():  # Each function is featured here in main().

    # List Tagger function
    print(list_tagger([1, 2, 3]))
    # Cutoff function
    midlifecrisis = [51, 52, 55, 56, 58]
    print(cutoff(midlifecrisis, 2))
    print(cutoff([0], 5))
    # Prepender function
    stringlist = ["cat", "dog", "blue"]
    prepender(stringlist, "red")
    print(stringlist)
    print(name_list())
    # Multiples of 3 function
    print(multiples_of_3(10))
    # Dice Input function
    dice_input()

    doctest.testmod()


if __name__ == "__main__":
    main()
