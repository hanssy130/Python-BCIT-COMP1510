import doctest


def number_translator(number):
    """
    Assigns every character to a variable. Prints translated number after passing to converter().

    :param number: str
    :precondition: String must be entered in the format XXX-XXX-XXXXX
    :postcondition: Translated string in the format of only #s.
    :return: The string in the format of #s.

    >>> number_translator("101-123-1234") #Ones and Zeros test
    101-123-1234
    >>> number_translator("ABC-DEF-GHIJ") #letter test
    222-333-4445
    >>> number_translator("XXXXXXXXXXX") #error test
    Please enter your phone number in the format: XXX-XXX-XXXX
    """
    number = number.upper()
    if len(number) < 11:
        print("Please enter your phone number in the format: XXX-XXX-XXXX")
    elif number[3] != "-" or number[7] != "-":
        print("Please enter your phone number in the format: XXX-XXX-XXXX")
    else:
        a = number[0]
        b = number[1]
        c = number[2]
        d = number[4]
        e = number[5]
        f = number[6]
        g = number[8]
        h = number[9]
        i = number[10]
        j = number[11]
        print(converter(a)
               + converter(b) + converter(c) + "-" + converter(d) + converter(e) + converter(f) + "-" +
               converter(g) + converter(h) + converter(i) + converter(j)
              )
        # if number[0].__class__ == str:
        #     print("it's a str")
        #
        #     number[3] = "yes"
        #     print(number)
        # else:
        #     print("it's not a str")
        #
        #     number[3] = "x"
        #     print(number)


def converter(x):
    """
    Converts input into the approprite #.

    :param x: str
    :precondition: Must be an alphabetical or numerical number.
    :postcondition: Promises the appropriate numerical value.
    :return: Returns the translated numerical value.

    >>> converter("0") #tested zeros
    '0'
    >>> converter("1") #tested ones
    '1'
    >>> converter("D") #tested letters
    '3'
    """
    if x == "1":
        return "1"
    if x == "A" or x == "B" or x == "C" or x == "2":
        return "2"
    if x == "D" or x == "E" or x == "F" or x == "3":
        return "3"
    if x == "G" or x == "H" or x == "I" or x == "4":
        return "4"
    if x == "J" or x == "K" or x == "L" or x == "5":
        return "5"
    if x == "M" or x == "N" or x == "O" or x == "P" or x == "6":
        return "6"
    if x == "Q" or x == "R" or x == "S" or x == "7":
        return "7"
    if x == "T" or x == "U" or x == "V" or x == "8":
        return "8"
    if x == "W" or x == "X" or x == "Y" or x == "Z" or x == "9":
        return "9"
    if x == "0":
        return "0"


def main():
    """
    Drives the main function.
    """
    number = input("Enter a 10-character telephone number in the format XXX-XXX-XXX: ")
    number = number.strip()
    number_translator(number)
    doctest.testmod()


if __name__ == "__main__":
    main()

"""
decomposition: I broke it down into two parts. One function separates every character of the string into a variable. 
The other function takes each variable and processes it into the translated character.
patternmatching: Every translation is similar in process, just different values at the end. Every character in the 
initial string needs to be translated the same way. We repeat the process 10 times for every character in the phone number.
abstraction: Perhaps 0 and 1 don't really count as they're not part of the map, but they needed to be addressed when 
translating ensuring that they don't get lost.
algorithms: A process was created to translate the characters to their corresponding number according to the instructions.
"""