# guess the number: computer
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        feedback = input(f"Is {guess} higher(H), lower(L), or correct?(C): ")
        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1

    print("well done!")


computer_guess(100)
