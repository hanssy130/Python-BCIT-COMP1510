import random


def rock_paper_scissors():
    """
    Computer randomly chooses between Rock, Paper, or Scissors and passes into the game calculator.

    :return: Passes "rock", "paper", or "scissors" to the game calculator function.
    """
    result = random.randint(0, 2)
    if result == 0:
        handresult = "rock"
    elif result == 1:
        handresult = "paper"
    elif result == 2:
        handresult = "scissors"
    userplays(handresult)


def userplays(handresult):
    """
    Calculates result after asking user for "Rock", "Paper", or "Scissors".

    :param handresult: str
    :precondition: User must enter Rock Paper of Scissors.
    :postcondition: Input will be matched against the computer's input.
    :return: The result of the RPS match.
    """
    action = input("Rock, Paper, or Scissors? ").strip().lower()
    print(handresult)
    if action == handresult:
        print("Tie.")
    elif action == "rock":
        if handresult == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif action == "paper":
        if handresult == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif action == "scissors":
        if handresult == "rock":
            print("You lose!")
        else:
            print("You win!")


def main():
    """
    Drives the main function.
    """
    rock_paper_scissors()
    rock_paper_scissors()
    rock_paper_scissors()
    rock_paper_scissors()
    rock_paper_scissors()


if __name__ == "__main__":
    main()

"""
decomposition: I turned this to two functions. One generates a random result. The other one takes that random result and
the user's input and prints the result.
patternmatching: The pattern is that you either win or lose (if you haven't tied) depending on the input.
abstraction: Rather than making ties a possible result, I took it outside to be checked first.
algorithm: Used a lot of if else. I could've switched between checking the computer first before the hand result. Either
way would lead to a result.
"""