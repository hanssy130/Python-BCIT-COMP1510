def dijkstra(flags):
    """
    Rearranges a list of flag colours in the order of the Dutch national flag.
    :param flags: a list
    :precondition: flags must be a list of only the colours, red, white, or blue
    :postcondition: promises to rearrange the variable in the order of red, white, and blue.
    :return: Does not return anything.
    """
    count_r = count_w = count_b = 0
    for name in flags:
        if name == "red":
            count_r += 1
        elif name == "white":
            count_w += 1
        elif name == "blue":
            count_b += 1
    count_sort = 0
    for i in range(count_r):
        flags[i] = "red"
        count_sort += 1
    for i in range(count_sort, count_sort + count_w):
        flags[i] = "white"
        count_sort += 1
    for i in range(count_sort, count_sort + count_b):
        flags[i] = "blue"
        count_sort += 1


def main():
    dutch = ["white", "blue", "blue", "red", "white", "red", "white"]
    test2 = ["blue", "white"]
    dijkstra(dutch)
    dijkstra(test2)
    print(dutch)
    print(test2)


if __name__ == "__main__":
    main()
