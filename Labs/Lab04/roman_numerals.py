import doctest


def convert_to_roman_numeral(positive_int):
    """
    Converts a decimal number to Roman numerals.

    :param positive_int: int
    :PRECONDITION: Enter an integer between 1 to 10,000.
    :POSTCONDITION: The function will convert the number into roman numerals.
    :return: Returns a Roman numeral string translated from the input.

    >>> convert_to_roman_numeral(1) #tested minimum
    I
    >>> convert_to_roman_numeral(10000) #tested maximum
    MMMMMMMMMM
    >>> convert_to_roman_numeral(4440) #tested fours and 0 ones.
    MMMMCDXL
    >>> convert_to_roman_numeral(9909) #tested nines and 0 tens.
    MMMMMMMMMCMIX
    >>> convert_to_roman_numeral(6066) #tested sixes and 0 hundreds.
    MMMMMMLXVI
    """
    if positive_int >= 1000:
        thousands = int(positive_int / 1000)
        thousands = thousands * "M"
        remainder = positive_int % 1000
        if remainder >= 100:
            hundreds = int(remainder / 100)
            if hundreds == 9:
                hundreds = "CM"
            elif 4 < hundreds < 9:
                hundreds = "D" + (hundreds - 5) * "C"
            elif hundreds == 4:
                hundreds = "CD"
            else:
                hundreds = hundreds * "C"
            remainder = remainder % 100
            if remainder >= 10:
                tens = int(remainder / 10)
                if tens == 9:
                    tens = "XC"
                elif 4 < tens < 9:
                    tens = "L" + (tens - 5) * "X"
                elif tens == 4:
                    tens = "XL"
                else:
                    tens = tens * "X"
                remainder = remainder % 10
                if remainder >= 1:
                    if remainder == 9:
                        ones = "IX"
                    elif 4 < remainder < 9:
                        ones = "V" + (remainder - 5) * "I"
                    elif remainder == 4:
                        ones = "IV"
                    else:
                        ones = remainder * "I"
                    print(str(thousands) + str(hundreds) + str(tens) + str(ones))
                else:
                    print(str(thousands) + str(hundreds) + str(tens))
            else:
                if remainder == 9:
                    ones = "IX"
                elif 4 < remainder < 9:
                    ones = "V" + (remainder - 5) * "I"
                elif remainder == 4:
                    ones = "IV"
                else:
                    ones = remainder * "I"
                print(str(thousands) + str(hundreds) + str(ones))
        elif remainder >= 10:
            tens = int(remainder / 10)
            if tens == 9:
                tens = "XC"
            elif 4 < tens < 9:
                tens = "L" + (tens - 5) * "X"
            elif tens == 4:
                tens = "XL"
            else:
                tens = tens * "X"
            remainder = remainder % 10
            if remainder >= 1:
                if remainder == 9:
                    ones = "IX"
                elif 4 < remainder < 9:
                    ones = "V" + (remainder - 5) * "I"
                elif remainder == 4:
                    ones = "IV"
                else:
                    ones = remainder * "I"
                print(str(thousands) + str(tens) + str(ones))
            else:
                print(str(thousands) + str(tens))
        else:
            if remainder == 9:
                ones = "IX"
            elif 4 < remainder < 9:
                ones = "V" + (remainder - 5) * "I"
            elif remainder == 4:
                ones = "IV"
            else:
                ones = remainder * "I"
            print(str(thousands) + str(ones))
    elif positive_int >= 100:
        hundreds = int(positive_int / 100)
        if hundreds == 9:
            hundreds = "CD"
        elif 4 < hundreds < 9:
            hundreds = "D" + (hundreds - 5) * "C"
        elif hundreds == 4:
            hundreds = "CD"
        else:
            hundreds = hundreds * "C"
        remainder = positive_int % 100
        if remainder >= 10:
            tens = int(remainder / 10)
            if tens == 9:
                tens = "XC"
            elif 4 < tens < 9:
                tens = "L" + (tens - 5) * "X"
            elif tens == 4:
                tens = "XL"
            else:
                tens = tens * "X"
            remainder = remainder % 10
            if remainder >= 1:
                if remainder == 9:
                    ones = "IX"
                elif 4 < remainder < 9:
                    ones = "V" + (remainder - 5) * "I"
                elif remainder == 4:
                    ones = "IV"
                else:
                    ones = remainder * "I"
                print(str(hundreds) + str(tens) + str(ones))
            else:
                print(str(hundreds) + str(tens))
        else:
            if remainder == 9:
                ones = "IX"
            elif 4 < remainder < 9:
                ones = "V" + (remainder - 5) * "I"
            elif remainder == 4:
                ones = "IV"
            else:
                ones = remainder * "I"
            print(str(hundreds) + str(ones))
    elif positive_int >= 10:
        tens = int(positive_int / 10)
        if tens == 9:
            tens = "XC"
        elif 4 < tens < 9:
            tens = "L" + (tens - 5) * "X"
        elif tens == 4:
            tens = "XL"
        else:
            tens = tens * "X"
        remainder = positive_int % 10
        if remainder >= 1:
            if remainder == 9:
                ones = "IX"
            elif 4 < remainder < 9:
                ones = "V" + (remainder - 5) * "I"
            elif remainder == 4:
                ones = "IV"
            else:
                ones = remainder * "I"
            print(str(tens) + str(ones))
        else:
            print(str(tens))
    else:
        if positive_int == 9:
            ones = "IX"
        elif 4 < positive_int < 9:
            ones = "V" + (positive_int - 5) * "I"
        elif positive_int == 4:
            ones = "IV"
        else:
            ones = positive_int * "I"
        print(str(ones))


def main():
    """
    Drives the main function.
    """
    convert_to_roman_numeral(1)



if __name__=="__main__":
    main()
    doctest.testmod()


"""
decomposition: I kept it all in one function as passing on the number proved difficult for me. I wanted to isolate the thousands, then the hundreds, then the tens, and finally the ones. Then, I wanted to deal with the multiples of 5 (5, 50, and 500) within the ones, tens, and hundreds respectively.
patternmatching: Program is designed to check in order from thousands to hundreds to tens to ones in the same order. The checks are repeated in a cascading fashion.
absraction: Rather than take the number right away and translate it, I wanted to start with the thousands.
algorithms: The 5s get translated in a certain fashion that was usable at all powers of tens
"""