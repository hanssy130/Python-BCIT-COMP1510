def im_not_sleepy():
    tenshours = 1
    tensminutes = 5
    onesminutes = 9
    pointsdict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

    def hours():
        highestpoints = 0
        for i in range(0, tenshours + 1):
            if i == 0:
                oneshours = 9
            elif i == 1:
                oneshours = 2
            for j in range(0, oneshours + 1):
                time = [i, j]
                points = 0
                for t in time:
                    for key in pointsdict:
                        if t == key:
                            points += pointsdict[key]
                if i == 0:
                    points -= pointsdict[0]  # cancels out the 0's value of points.
                if points > highestpoints:
                    highestpoints = points
                    highesttime = time
        return highesttime

    def minutes():
        highestpoints = 0
        for i in range(0, tensminutes + 1):
            for j in range(0, onesminutes + 1):
                time = [i, j]
                points = 0
                for t in time:
                    for key in pointsdict:
                        if t == key:
                            points += pointsdict[key]
                if points > highestpoints:
                    highestpoints = points
                    highesttime = time
        return highesttime

    hours = hours()
    minutes = minutes()
    print("The time that requires the highest amount of bars is " + str(hours[0]) + str(hours[1]) + ":" + str(
        minutes[0]) + str(minutes[1]) + ".")


def main():
    im_not_sleepy()


if __name__ == "__main__":
    main()
