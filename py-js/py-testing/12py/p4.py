# rock paper scissors
import random

choices = ["r", "p", "s"]


def play():
    user = input("'r' for rock, 'p', for paper, 's' for scissors: \n")
    computer = random.choice(choices)

    if user == computer:
        return "it's a tie"

    if is_win(user, computer):
        return "you won!"
    return "You lost!"


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True

print(play())