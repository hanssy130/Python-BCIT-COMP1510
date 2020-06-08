# I can not always present an equal length between the summed sparsed vector
# and the parameters used in addition.
# This is because if any of the keys summation equals zero, it will not
# be included in the final summation, due to how sparse_add was programmed:
# I would need to ask my team lead if I should redesign sparse_add,
# or create a new function that accounts for the 0s that were summed
# to get a clear response on the length of the summed sparse vector.


import doctest


def sparse_add(vector1, vector2):
    '''
    A function that creates new dictionary representing the sum of two vectors.

    :param vector1: dictionary of integers
    :param vector2: dictionary of integers
    :precondition: numbers must be greater than 0
    :postcondition: calcualtes the correct sum into a new dictionary
    :return: dictionary representing the sum of two vectors
    >>> sparse_add({0:4, 1:5, 2:7}, {0:3, 1:4, 3:9})
    {0: 7, 1: 9, 2: 7, 3: 9}
    >>> sparse_add({0:5, 1:5, 2:5}, {0:1, 1:2, 2:3})
    {0: 6, 1: 7, 2: 8}
    '''
    sum = {}
    for i in vector1.keys():
        sum[i] = vector1[i]
    for i in vector2.keys():
        sum[i] = vector2[i]
    for i in vector1.keys():
        for j in vector2.keys():
            if i == j:
                sum[i] = vector1[i] + vector2[j]
                if sum[i] == 0:
                    sum.pop(i)
    else:
        return sum


def main():
    doctest.testmod()
    print(sparse_add({0:-5, 1:3}, {0:5, 1:1}))


if __name__=="__main__":
    main()