import doctest


def selection_sort(items):
    """
    Sorts the list from smallest to greatest.

    :param items: must be a list
    :precondition: items must be a list of ints.
    :postcondition: promises to sort the list in ascending order.
    :return: a list

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]
    >>> selection_sort(["a", "B", "A"])
    ['A', 'B', 'a']
    """
    if not items:
        raise ValueError(f"The list cannot be blank!")
    for i in range(len(items)):
        minimum = i
        for j in range(i, len(items)):
            if items[j] < items[minimum]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]
    return items


def main():
    unsorted = ["apple", "cat", 5]
    sorted_copy = selection_sort(unsorted)
    print(sorted_copy)
    doctest.testmod()


if __name__ == "__main__":
    main()
