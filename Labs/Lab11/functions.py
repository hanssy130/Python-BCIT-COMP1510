import time
import doctest


def timer(func):
    """
    Calculates the time & prints to the results.

    :param func: function
    :precondition: Must be a valid function name with any necessary parameters
    :postcondition: Calculates the amount of time taken to complete a function
    :return: Prints result in results.txt
    """

    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        filename = "results.txt"
        with open(filename, 'a') as file_object:
            file_object.write(f"\nFinished {func.__name__!r} in {run_time:.10f} secs. Calculating {func.__name__}")
        return value

    return wrapper_timer


@timer
def factorial(value):
    """
    Calculates the factorial of a given value.
    :param value: int
    :precondition: value must be greater than 0.
    :postcondition: the factorial total
    :return: the factorial total

    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    if value == 0:
        return 1
    result = 1
    for i in range(0, value):
        result = result * value
        value -= 1

    return result

@timer
def recursiveFactorial(n):
    """Asks helper function to calculate factorial."""
    # if n == 1:
    #     return n
    # else:
    #     return n * recursiveFactorial(n - 1)
    # result = recursiveFactorial_helper()
    return recursiveFactorial_helper(n)


def recursiveFactorial_helper(n):
    """
    Calculates the factorial of a given value.
    :param value: int
    :precondition: value must be greater than 0.
    :postcondition: the factorial total
    :return: the factorial total

    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    if n == 1:
        return n
    else:
        return n * recursiveFactorial_helper(n - 1)



def testRegularLoop():
    """
    Loops through factorial()
    """
    for i in range(1, 101):
        printer(i)
        factorial(i)
    return


def testRecursion():
    """
    Loops through recursiveFactorial()
    """
    for i in range(1, 101):
        printer(i)
        recursiveFactorial(i)
    return


def printer(factorial):
    filename = "results.txt"
    with open(filename, 'a') as file_object:
        file_object.write(f"\nCalculating factorial for " + str(factorial))
    return

# Based on our findings in results.txt, Justin Majam and Hans Sy conclude that recursion is slower than non-recursion
# when calculating factorials in PyCharm. Recursion requires more iterations.


def main():
    testRegularLoop()
    testRecursion()
    # doctest.testmod()


if __name__ == "__main__":
    main()
