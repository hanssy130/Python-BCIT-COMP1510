def time_calculator(seconds):
    """
    Converts seconds into days, hours, minutes, seconds in order.

    :param seconds: int
    :precondition: Seconds must be an integer.
    :postcondition: The converted time is all in integers.
    :return: The converted time.

    >>> time_calculator(999999) #generic test
    11 days, 13 hours, 46 minutes, and 39 seconds.
    >>> time_calculator(86400) #test 1 day
    1 days, 0 hours, 0 minutes, and 0 seconds.
    >>> time_calculator(3600) #test 1 hour
    0 days, 1 hours, 0 minutes, and 0 seconds.
    >>> time_calculator(60) #test 1 minute
    0 days, 0 hours, 1 minutes, and 0 seconds.
    >>> time_calculator(1) #test 1 second
    0 days, 0 hours, 0 minutes, and 1 seconds.

    """
    days = str(int(seconds / 86400))
    timeleft1 = seconds % 86400
    hours = str(int(timeleft1 / 3600))
    timeleft2 = timeleft1 % 3600
    minutes = str(int(timeleft2 / 60))
    timeleft3 = timeleft2 % 60
    finalseconds = (str(int(timeleft3)))
    print(days + " days, " + hours + " hours, " + minutes + " minutes, and " + finalseconds + " seconds.")

"""
decomposition: I used one function. This takes the number and divides it down accordingly into appropriate time categories
patternmatching: I repeated the same process to take the integer of the division and its 
abstraction: I use modulo to keep breaking down the initial number into the appropriate categories.
algorithm: Using the conversion rates, I was able to break down the initial number.
"""